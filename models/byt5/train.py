import argparse
import os
import evaluate
import functools

from transformers import (
    AutoTokenizer,
    T5ForConditionalGeneration,
    T5Config,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    EarlyStoppingCallback,
    set_seed,
)

from data_utils import load_pronunciation_dictionary, load_all_pronunciation_dictionaries


def preprocess_function(examples, tokenizer, max_length=128):
    """
    Tokenizes the input words and target pronunciations.
    This function is applied to the dataset using .map() for efficiency.
    """
    # Tokenize the input words (graphemes)
    inputs = tokenizer(
        examples["word"],
        max_length=max_length,
        truncation=True,
        padding=False # Padding will be handled by the DataCollator
    )

    # Tokenize the target pronunciations (phonemes) for the labels
    # The 'as_target_tokenizer' context manager ensures correct tokenization for labels
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            examples["pron"],
            max_length=max_length,
            truncation=True,
            padding=False # Padding will be handled by the DataCollator
        )

    inputs["labels"] = labels["input_ids"]
    return inputs


def compute_metrics(pred, tokenizer, cer_metric, wer_metric):
    """
    Computes Character Error Rate (CER) and Word Error Rate (WER).
    Note: 'tokenizer' is now passed explicitly to this function.
    """
    labels_ids = pred.label_ids
    pred_ids = pred.predictions

    # Decode predictions and labels
    pred_str = tokenizer.batch_decode(pred_ids, skip_special_tokens=True)

    # Replace -100 in labels_ids with the pad_token_id for decoding
    labels_ids[labels_ids == -100] = tokenizer.pad_token_id
    label_str = tokenizer.batch_decode(labels_ids, skip_special_tokens=True)

    # Compute metrics
    cer = cer_metric.compute(predictions=pred_str, references=label_str)
    wer = wer_metric.compute(predictions=pred_str, references=label_str)

    return {"cer": cer, 'wer': wer}


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Fine-tune a ByT5 model for Grapheme-to-Phoneme (G2P)")

    # --- Data and Model Paths ---
    parser.add_argument('--model_name',type=str,default='google/byt5-small', help='Hugging Face model identifier (e.g., google/byt5-small).')
    parser.add_argument('--train_data',type=str,default='data/train', help="Path to the training data directory or file.")
    parser.add_argument('--dev_data',type=str,default='data/dev', help="Path to the development data directory or file.")
    parser.add_argument('--test_data',type=str,default='data/test', help="Path to the test data directory or file.")
    parser.add_argument('--output_dir',type=str,required=True, help="Directory to save checkpoints and final model.")
    parser.add_argument('--checkpoint',default=None,type=str, help="Path to a checkpoint for evaluation or resuming training.")
    parser.add_argument('--language',default=None,type=str, help="Specify a single language to train on (e.g., 'ady'). If not set, trains on all .tsv files in data dirs.")

    # --- Task Control ---
    parser.add_argument('--train',action='store_true', help="Flag to run training.")
    parser.add_argument('--evaluate',action='store_true', help="Flag to run evaluation on the test set.")
    parser.add_argument('--resume_from_checkpoint',action='store_true', help="Resume training from the specified checkpoint.")

    # --- Training Hyperparameters ---
    parser.add_argument('--fp16', action='store_true', default=False, help="Enable mixed-precision training (FP16).")
    parser.add_argument('--train_batch_size',type=int,default=32)
    parser.add_argument('--eval_batch_size',type=int,default=128)
    parser.add_argument('--learning_rate',type=float,default=3e-3)
    parser.add_argument('--warmup_steps',type=int,default=1100)
    parser.add_argument('--lr_scheduler_type',type=str,default='cosine_with_restarts')
    parser.add_argument('--epochs',type=int,default=60)
    parser.add_argument('--gradient_accumulation',type=int,default=2)
    parser.add_argument('--weight_decay',type=float,default=0.01)
    parser.add_argument('--label_smoothing_factor',type=float,default=0.1)
    parser.add_argument('--early_stopping_patience',type=int,default=4)
    parser.add_argument('--logging_steps',type=int,default=400)
    parser.add_argument('--save_steps',type=int,default=800)
    parser.add_argument('--eval_steps',type=int,default=800)
    parser.add_argument('--unk_prob',type=float,default=0.15, help="Probability of masking the language token with '<unk>:' during multi-language training.")
    parser.add_argument('--max_seq_length', type=int, default=128, help="Maximum sequence length for tokenization.")

    # --- Model Configuration ---
    parser.add_argument('--use_pretrained_model', action='store_true', help="Flag to load a pretrained model from Hugging Face hub. If not set, initializes a new model.")
    parser.add_argument('--num_encoder_layers',type=int,default=8) # byt5-small default
    parser.add_argument('--num_decoder_layers',type=int,default=8) # byt5-small default
    parser.add_argument('--d_model',type=int,default=1472) # byt5-small default
    parser.add_argument('--d_kv',type=int,default=64)
    parser.add_argument('--d_ff',type=int,default=3584) # byt5-small default

    args = parser.parse_args()
    set_seed(42)

    # --- Load Evaluation Metrics ---
    cer_metric = evaluate.load("cer")
    wer_metric = evaluate.load("wer")

    # --- Main Logic: Training ---
    if args.train:

        # --- 1. Load and Preprocess Data ---
        print("Loading and preprocessing data...")
        if not args.language:
            # Multi-language training
            train_data = load_all_pronunciation_dictionaries(args.train_data, prefix=True, mask_prob=args.unk_prob)
            dev_data = load_all_pronunciation_dictionaries(args.dev_data, prefix=True)
            print(f"Loaded all: {train_data} -> {dev_data}")
        else:
            # Single-language training
            train_tsv = os.path.join(args.train_data, args.language+".tsv")
            dev_tsv = os.path.join(args.dev_data, args.language+".tsv")
            train_data = load_pronunciation_dictionary(path=train_tsv, language=args.language, prefix=True)
            dev_data = load_pronunciation_dictionary(path=dev_tsv, language=args.language, prefix=True)
            print(f"Loaded: {train_tsv} -> {dev_tsv}")

        tokenizer = AutoTokenizer.from_pretrained(args.model_name)

        # Apply the preprocessing function to the entire dataset
        train_dataset = train_data.map(
            preprocess_function,
            batched=True,
            fn_kwargs={'tokenizer': tokenizer, 'max_length': args.max_seq_length},
            remove_columns=train_data.column_names
        )
        dev_dataset = dev_data.map(
            preprocess_function,
            batched=True,
            fn_kwargs={'tokenizer': tokenizer, 'max_length': args.max_seq_length},
            remove_columns=dev_data.column_names
        )
        print(f"Training on {len(train_dataset)} examples, validating on {len(dev_dataset)} examples.")

        # --- 2. Initialize Model and Data Collator ---
        if args.use_pretrained_model:
            print(f'Loading pretrained model: {args.model_name}')
            model = T5ForConditionalGeneration.from_pretrained(args.model_name)
        else:
            print('Initializing a new ByT5 model from scratch with custom config...')
            config = T5Config.from_pretrained(args.model_name)
            # Override config with provided arguments
            config.num_layers = args.num_encoder_layers
            config.num_decoder_layers = args.num_decoder_layers
            config.d_kv = args.d_kv
            config.d_model = args.d_model
            config.d_ff = args.d_ff
            model = T5ForConditionalGeneration(config)

        # The standard DataCollatorForSeq2Seq handles padding and creating decoder_input_ids
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

        # --- 3. Set up Trainer ---
        # Use functools.partial to pass the tokenizer to the metrics function
        compute_metrics_with_tokenizer = functools.partial(compute_metrics, tokenizer=tokenizer, cer_metric=cer_metric, wer_metric=wer_metric)

        training_args = Seq2SeqTrainingArguments(
            output_dir=args.output_dir,
            predict_with_generate=True,
            generation_num_beams=5,

            do_train=True,
            do_eval=True,
            evaluation_strategy="steps",

            per_device_train_batch_size=args.train_batch_size,
            per_device_eval_batch_size=args.eval_batch_size,
            gradient_accumulation_steps=args.gradient_accumulation,

            num_train_epochs=args.epochs,
            learning_rate=args.learning_rate,
            warmup_steps=args.warmup_steps,
            lr_scheduler_type=args.lr_scheduler_type,
            weight_decay=args.weight_decay,
            label_smoothing_factor=args.label_smoothing_factor,

            fp16=args.fp16,
            logging_steps=args.logging_steps,
            save_steps=args.save_steps,
            eval_steps=args.eval_steps,
            save_total_limit=2,
            load_best_model_at_end=True,
            metric_for_best_model="wer",
            greater_is_better=False,
        )

        trainer = Seq2SeqTrainer(
            model=model,
            tokenizer=tokenizer,
            args=training_args,
            compute_metrics=compute_metrics_with_tokenizer,
            train_dataset=train_dataset,
            eval_dataset=dev_dataset,
            data_collator=data_collator,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience)]
        )

        # --- 4. Train ---
        print("Starting training...")
        train_result = trainer.train(resume_from_checkpoint=args.resume_from_checkpoint or args.checkpoint)
        trainer.save_model()  # Saves the tokenizer too

        metrics = train_result.metrics
        trainer.log_metrics("train", metrics)
        trainer.save_metrics("train", metrics)
        trainer.save_state()
        print("Training finished.")

    # --- Main Logic: Evaluation ---
    elif args.evaluate:
        print("Starting evaluation...")
        if not args.checkpoint:
            raise ValueError("--checkpoint must be provided for evaluation.")

        # --- 1. Load Model, Tokenizer, and Data ---
        model = T5ForConditionalGeneration.from_pretrained(args.checkpoint)
        tokenizer = AutoTokenizer.from_pretrained(args.checkpoint)

        if not args.language:
            test_data = load_all_pronunciation_dictionaries(args.test_data, prefix=True)
        else:
            test_tsv = os.path.join(args.test_data, args.language+".tsv")
            test_data = load_pronunciation_dictionary(path=test_tsv, language=args.language, prefix=True)

        test_dataset = test_data.map(
            preprocess_function,
            batched=True,
            fn_kwargs={'tokenizer': tokenizer, 'max_length': args.max_seq_length},
            remove_columns=test_data.column_names
        )
        print(f"Evaluating on {len(test_dataset)} examples.")

        # --- 2. Set up Trainer for Prediction ---
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
        compute_metrics_with_tokenizer = functools.partial(compute_metrics, tokenizer=tokenizer, cer_metric=cer_metric, wer_metric=wer_metric)

        # Minimal training args needed for prediction
        eval_args = Seq2SeqTrainingArguments(
            output_dir=args.output_dir,
            predict_with_generate=True,
            generation_num_beams=5,
            per_device_eval_batch_size=args.eval_batch_size,
            fp16=args.fp16,
        )

        trainer = Seq2SeqTrainer(
            model=model,
            args=eval_args,
            tokenizer=tokenizer,
            compute_metrics=compute_metrics_with_tokenizer,
            data_collator=data_collator,
        )

        # --- 3. Get Predictions and Save ---
        predictions = trainer.predict(test_dataset)

        # Log and save metrics
        print("Evaluation Metrics:")
        print(predictions.metrics)
        trainer.log_metrics("eval", predictions.metrics)
        trainer.save_metrics("eval", predictions.metrics)

        # Decode predictions and save to file
        pred_str = tokenizer.batch_decode(predictions.predictions, skip_special_tokens=True)

        # Ensure output directory exists
        if not os.path.exists(args.output_dir):
            os.makedirs(args.output_dir)

        output_file = os.path.join(args.output_dir, f'predictions_{args.language or "all"}.tsv')
        with open(output_file, 'w', encoding='utf-8') as f:
            # f.write("Word\tTrue_Pronunciation\tPredicted_Pronunciation\n")
            for word, true_pron, pred_pron in zip(test_data['word'], test_data['pron'], pred_str):
                f.write(f"{word}\t{true_pron}\t{pred_pron}\n")

        print(f"Predictions saved to {output_file}")

    else:
        print("Please specify a task: --train or --evaluate")
