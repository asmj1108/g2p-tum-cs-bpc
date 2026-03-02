# Multilingual Low-resource Grapheme-to-Phoneme Conversion

## Overview
This repository contains the datasets, training scripts, and numerical results for a project conducted as part of the **Bachelor Practical Course Projects in Natural Language Processing** at the Technical University of Munich (TUM) .

The project focuses on multilingual **Grapheme-to-Phoneme (G2P) conversion**—the computational process of mapping sequences of graphemes (written text) to sequences of phonemes (pronunciation)—specifically in **low-resource language settings**.

Through this project, we designed specific datasets and experiments to evaluate and compare the Word Error Rate (WER) of three robust NLP models. The main goal was to investigate how multilingual training strategies, language family relationships, and transliteration affect G2P performance when training data is severely limited (simulated by using only 1,000 words per language).

## Deliverables
Detailed analysis, methodology, and discussions of our experimental results can be found in the following project deliverables:
- [Poster](Poster.pdf) — A concise, visual overview of the project’s main goals, models, and key empirical findings.
- [Report](Report.pdf) — An in-depth academic document covering the methodology, experimental setup, detailed results, and comprehensive analysis and discussion.

## Evaluated Architectures
To conduct these experiments without needing to modify underlying theoretical architectures, we utilized published training frameworks and scripts for three distinct seq2seq models:
1. **Transformer:** A standard attention-based sequence-to-sequence model.
2. **Neural Transducer:** A model trained with imitation learning, incorporating a bidirectional LSTM encoder.
3. **Attentive LSTM:** A standard Long Short-Term Memory neural network equipped with a soft attention mechanism.

## Research Questions & Conducted Experiments
We compared the average WER of the three models under both monolingual and multilingual low-resource conditions. To deeply explore the multilingual capabilities, we designed five key experiments.

> **Note on Terminology:** *Similar languages* in the context of these experiments specifically refer to languages grouped by their **language family** and **script** (e.g., Germanic languages using Latin scripts, or Slavic languages using Cyrillic scripts).

### 1. Effect of Script-based Language Tags
**Question:** How does the script of an explicitly prepended language tag impact a model's predictive performance?
* **Experiment:** Manipulated language tags across different scripts (Uppercase Cyrillic, Uppercase Latin, Lowercase Latin, and No Tag) and compared the resulting WER.

### 2. Monolingual vs. Multilingual Performance
**Question:** Does training a model on a dataset grouped with "similar languages" yield better performance than training purely monolingual models?
* **Experiment:** Measured the performance improvement (WER reduction) of target languages when trained on datasets combining their data with internally similar languages, compared to their standalone monolingual baselines.

### 3. Impact of Dataset Size within Similar Languages
**Question:** How does scaling the number of similar languages in a multilingual training set affect overall performance?
* **Experiment:** Assessed the effect on WER by gradually varying the number of similar languages included in the multilingual target dataset.

### 4. Cross-Family Cultural Influence
**Question:** Can multilingual datasets successfully capture cross-lingual learning effects based on historical and cultural influences across *different* language families?
* **Experiment:** Investigated the historical transfer effect by co-training Uyghur (a Turkic language) and Classical Persian (an Indo-Iranian language), analyzing whether shared loanwords improve G2P metrics.

### 5. Native Script vs. Latin Transliteration
**Question:** Does harmonizing writing systems through transliteration improve G2P model performance?
* **Experiment:** Compared model performance using datasets in their original native scripts versus Latin transliterated configurations. We tested this in two scenarios:
  1. Mixing transliterated languages with natively similar Latin-script languages (e.g., Transliterated Cyrillic Slavic + Native Latin Slavic).
  2. A scenario where *all* similar languages in the dataset are purely transliterated (e.g., all Arabic-script languages transliterated to Latin to make omitted vowels explicit).

## Repository Structure
* **`/data`**: Monolingual datasets splits used for the baseline experiment and creating multilingual datasets.
* **`/multilingual_data`**: specially configured multilingual dataset splits used across all 5 experiments.
* **`/models`**: Published framework processing pipelines and training scripts utilized to train the Transformer, Transducer, and Attentive LSTM models.
* **`/results`**: Raw numerical outputs, baseline evaluations, and WER comparisons generated during evaluation.

## Acknowledgments
This project heavily relies on the resources provided by the **SIGMORPHON Shared Tasks on Grapheme-to-Phoneme Conversion** 
(from the years [2020](https://github.com/sigmorphon/2020/tree/master/task1), [2021](https://github.com/sigmorphon/2021-task1), [2022](https://github.com/sigmorphon/2022G2PST), and [2024](https://github.com/sigmorphon/2024G2PST)). 
We would like to express our gratitude for their training scripts for the three models used in this project.

As our data sources align with those used in the SIGMORPHON Shared Tasks, we also want to sincerely acknowledge the 
[WikiPron](https://github.com/CUNY-CL/wikipron) and [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary) 
for providing the raw pronunciation data that made these experiments possible.