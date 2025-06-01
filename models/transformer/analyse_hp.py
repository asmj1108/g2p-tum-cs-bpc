import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Replace wityour own result
data = {
    'batch_size': [256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256,
                   512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512,
                   1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024],
    'dropout': [0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3,
                0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3,
                0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3],
    'large_encoder': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
                      0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
                      0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    'large_decoder': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                      0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                      0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'WER': [37, 40, 34, 39, 41, 40, 37, 41, 37, 41, 36, 37,
            38, 44, 36, 38, 35, 39, 37, 35, 34, 39, 39, 37,
            41, 43, 38, 38, 39, 41, 39, 36, 39, 38, 34, 36]
}

df = pd.DataFrame(data)

# Calculate average WER for each parameter
batch_avg = df.groupby('batch_size')['WER'].mean().reset_index()
dropout_avg = df.groupby('dropout')['WER'].mean().reset_index()
encoder_avg = df.groupby('large_encoder')['WER'].mean().reset_index()
decoder_avg = df.groupby('large_decoder')['WER'].mean().reset_index()

# Find top 5 configurations
top_configs = df.sort_values('WER').head(5).reset_index(drop=True)

# Calculate interaction effects
encoder_decoder_avg = df.groupby(['large_encoder', 'large_decoder'])['WER'].mean().unstack()
batch_dropout_avg = df.groupby(['batch_size', 'dropout'])['WER'].mean().unstack()

print("Average WER by hyperparameter:")
print("Batch Size:\n", batch_avg)
print("\nDropout:\n", dropout_avg)
print("\nEncoder Size (0=small, 1=large):\n", encoder_avg)
print("\nDecoder Size (0=small, 1=large):\n", decoder_avg)

print("\nTop 5 Configurations:")
print(top_configs)

print("\nEncoder-Decoder Interaction:")
print(encoder_decoder_avg)

print("\nBatch Size-Dropout Interaction:")
print(batch_dropout_avg)

# Generate visualizations
plt.figure(figsize=(12, 8))

# Individual parameter effects
plt.subplot(2, 2, 1)
plt.bar(batch_avg['batch_size'].astype(str), batch_avg['WER'])
plt.title('Average WER by Batch Size')
plt.xlabel('Batch Size')
plt.ylabel('WER')

plt.subplot(2, 2, 2)
plt.bar(dropout_avg['dropout'].astype(str), dropout_avg['WER'])
plt.title('Average WER by Dropout Rate')
plt.xlabel('Dropout')
plt.ylabel('WER')

plt.subplot(2, 2, 3)
plt.bar(encoder_avg['large_encoder'].map({0: 'Small', 1: 'Large'}), encoder_avg['WER'])
plt.title('Average WER by Encoder Size')
plt.xlabel('Encoder Size')
plt.ylabel('WER')

plt.subplot(2, 2, 4)
plt.bar(decoder_avg['large_decoder'].map({0: 'Small', 1: 'Large'}), decoder_avg['WER'])
plt.title('Average WER by Decoder Size')
plt.xlabel('Decoder Size')
plt.ylabel('WER')

plt.tight_layout()
plt.savefig('hyperparameter_effects.png')
plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for decoder in [0, 1]:
    subset = df[df['large_decoder'] == decoder]
    group = subset.groupby('large_encoder')['WER'].mean()
    plt.plot(group.index, group.values, marker='o', label=f'Decoder {"Large" if decoder else "Small"}')
plt.xticks([0, 1], ['Small', 'Large'])
plt.title('Encoder-Decoder Interaction')
plt.xlabel('Encoder Size')
plt.ylabel('Average WER')
plt.legend()

plt.subplot(1, 2, 2)
for dropout in [0.1, 0.2, 0.3]:
    subset = df[df['dropout'] == dropout]
    group = subset.groupby('batch_size')['WER'].mean()
    plt.plot(group.index, group.values, marker='o', label=f'Dropout {dropout}')
plt.title('Batch Size-Dropout Interaction')
plt.xlabel('Batch Size')
plt.ylabel('Average WER')
plt.legend()

plt.tight_layout()
plt.savefig('interaction_effects.png')
plt.show()


print("\nVisualization paths saved:")
print("hyperparameter_effects.png")
print("interaction_effects.png")
