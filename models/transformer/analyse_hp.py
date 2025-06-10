import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

# 1) Build the parameter grid once
batch_sizes = [256, 512, 1024]
dropouts = [0.1, 0.2, 0.3]
encoders = [0, 1]
decoders = [0, 1]

param_list = list(itertools.product(batch_sizes, dropouts, encoders, decoders))
param_df = pd.DataFrame(param_list,
                        columns=['batch_size', 'dropout', 'large_encoder', 'large_decoder'])

# 2) Your WER vectors, in the same order as param_list for each language
wer_adyghe = [
    44, 44, 40, 38, 44, 42, 38, 38, 43, 40, 38, 40,
    42, 40, 39, 39, 42, 40, 38, 39, 41, 39, 39, 38,
    40, 42, 41, 39, 38, 39, 36, 40, 39, 40, 36, 40
]

wer_khmer = [
    44, 47, 49, 47, 44, 45, 44, 46, 42, 46, 42, 42,
    48, 47, 45, 45, 44, 46, 42, 43, 39, 45, 41, 43,
    46, 48, 44, 46, 45, 46, 42, 42, 41, 43, 41, 40
]

wer_urdu = [
    75, 77, 74, 75, 75, 72, 71, 72, 75, 74, 73, 72,
    73, 73, 72, 75, 76, 75, 71, 72, 75, 75, 70, 73,
    74, 75, 72, 74, 72, 76, 72, 72, 71, 74, 71, 70
]

wer_swedish = [
    55, 55, 57, 55, 54, 56, 57, 54, 56, 51, 55, 54,
    55, 53, 52, 51, 52, 54, 54, 54, 54, 54, 54, 52,
    54, 53, 56, 52, 54, 52, 55, 51, 53, 52, 56, 53
]

# 3) Turn each into a DataFrame and tag with language
df_adyghe = param_df.copy()
df_adyghe['WER'] = wer_adyghe
df_adyghe['language'] = 'Adyghe'
df_khmer = param_df.copy()
df_khmer['WER'] = wer_khmer
df_khmer['language'] = 'Khmer'
df_urdu = param_df.copy()
df_urdu['WER'] = wer_urdu
df_urdu['language'] = 'Urdu'
df_swedish = param_df.copy()
df_swedish['WER'] = wer_swedish
df_swedish['language'] = 'Swedish'

# 4) Concat into one big DataFrame
df = pd.concat([df_adyghe, df_khmer, df_urdu, df_swedish],
               ignore_index=True)

# 5) Compute averages by (language, hyperparameter)
batch_avg = df.groupby(['language', 'batch_size'])['WER'].mean().reset_index()
dropout_avg = df.groupby(['language', 'dropout'])['WER'].mean().reset_index()
encoder_avg = df.groupby(['language', 'large_encoder'])['WER'].mean().reset_index()
decoder_avg = df.groupby(['language', 'large_decoder'])['WER'].mean().reset_index()

# 6) Top‐5 lowest‐WER configs per language
top5 = df.groupby('language') \
    .apply(lambda d: d.nsmallest(5, 'WER')) \
    .reset_index(drop=True)

print("=== Average WER by Language & Hyperparameter ===\n")
for lang in df['language'].unique():
    print(f"--- {lang} ---")
    print("Batch size:\n", batch_avg[batch_avg.language == lang])
    print("Dropout:\n", dropout_avg[dropout_avg.language == lang])
    print("Encoder size:\n", encoder_avg[encoder_avg.language == lang])
    print("Decoder size:\n", decoder_avg[decoder_avg.language == lang])
    print()

print("=== Top 5 Configurations by Language ===")
print(top5[['language', 'batch_size', 'dropout', 'large_encoder', 'large_decoder', 'WER']])

# --- PLOTTING ---

languages = df['language'].unique()
vocab_sizes = {
    'Adyghe': '40×64',
    'Khmer': '64×56',
    'Urdu': '48×56',
    'Swedish': '32×56'
}

# A) Encoder–Decoder interaction, 2×2 subplots, independent Y‐axes
fig, axes = plt.subplots(2, 2, figsize=(12, 10), sharex=True)
for ax, lang in zip(axes.flatten(), languages):
    sub = df[df.language == lang]
    for dec in [0, 1]:
        grp = (sub[sub.large_decoder == dec]
               .groupby('large_encoder')['WER']
               .mean()
               .sort_index())
        ax.plot([0, 1], grp.values,
                marker='o',
                label=f'Decoder {"Large" if dec else "Small"}')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Small', 'Large'])
    ax.set_title(f'{lang} (Vocab Size: {vocab_sizes[lang]})')  # Added vocab size
    ax.set_xlabel('Encoder Size')
    ax.set_ylabel('WER')
    ax.legend()
plt.suptitle('Encoder–Decoder Interaction by Language (Graphemes×Phonemes)',
             y=0.97, fontsize=14)  # Lowered y position
plt.tight_layout(rect=[0, 0, 1, 0.97])  # Reserve space for title
plt.savefig('interaction_encoder_decoder.png')

# B) Batch Size–Dropout interaction, 2×2 subplots, independent Y‐axes
fig, axes = plt.subplots(2, 2, figsize=(12, 10), sharex=True)
for ax, lang in zip(axes.flatten(), languages):
    sub = df[df.language == lang]
    for dr in sorted(df.dropout.unique()):
        grp = (sub[sub.dropout == dr]
               .groupby('batch_size')['WER']
               .mean()
               .sort_index())
        ax.plot(grp.index, grp.values,
                marker='o',
                label=f'Dropout {dr}')
    ax.set_xscale('log', base=2)
    ax.set_xticks(batch_sizes)
    ax.set_xticklabels([str(b) for b in batch_sizes])
    ax.set_title(f'{lang} (Vocab Size: {vocab_sizes[lang]})')  # Added vocab size
    ax.set_xlabel('Batch Size')
    ax.set_ylabel('WER')
    ax.legend()
plt.suptitle('Batch Size–Dropout Interaction by Language (Graphemes×Phonemes)',
             y=0.97, fontsize=14)  # Lowered y position
plt.tight_layout(rect=[0, 0, 1, 0.97])  # Reserve space for title
plt.savefig('interaction_batch-size_dropout.png')
