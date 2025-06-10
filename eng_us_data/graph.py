import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data setup
data_amounts = [1000, 1500, 2000, 3000, 4000, 5000, 10000, 20000, 40000]
transformer_wer = [70, 64, 58, 53.67, 49.5, 47.6, 46.1, 43.35, 40.1]
neural_wer = [63, 62, 54, 50.67, 47, 46.8, 45.6, 44.05, 42.38]
attentive_lstm_wer = [66, 62, 54, 53.2, 50, 46.3, 45.21, 44.13, 42.23]

# Logarithmic function for regression
def log_func(x, a, b, c):
    return a * np.log(x) + b * (1/x) + c

# Generate regression curves
x_smooth = np.linspace(1000, 40000, 500)
params_trans, _ = curve_fit(log_func, data_amounts, transformer_wer)
params_neural, _ = curve_fit(log_func, data_amounts, neural_wer)
params_atten, _ = curve_fit(log_func, data_amounts, attentive_lstm_wer)
trans_pred = log_func(x_smooth, *params_trans)
neural_pred = log_func(x_smooth, *params_neural)
atten_pred = log_func(x_smooth, *params_atten)

# Plot setup
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, trans_pred, 'b-', linewidth=2.5, alpha=0.7, label='Transformer (Regression)')
plt.plot(x_smooth, neural_pred, 'r-', linewidth=2.5, alpha=0.7, label='Neural Transducer (Regression)')
plt.plot(x_smooth, atten_pred, 'g-', linewidth=2.5, alpha=0.7, label='Attentive LSTM (Regression)')
plt.plot(data_amounts, transformer_wer, 'bo', markersize=8, label='Transformer Data')
plt.plot(data_amounts, neural_wer, 'rs', markersize=8, label='Neural Transducer Data')
plt.plot(data_amounts, attentive_lstm_wer, 'g^', markersize=8, label='Attentive LSTM Data')
# Formatting
plt.xscale('log', base=2)
plt.xticks(data_amounts, ['1k', '1.5k', '2k', '3k', '4k', '5k', '10k', '20k', '40k'], rotation=45)
plt.xlabel('Data Amount (hours)', fontsize=12)
plt.ylabel('Word Error Rate (WER)', fontsize=12)
plt.title('WER vs Data Amount: Neural Transducer vs Transformer vs Attentive_LSTM', fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.ylim(35, 75)
plt.tight_layout()

# Add regression equations
eq_text = (f'Transformer: WER = {params_trans[0]:.2f}·ln(x) + {params_trans[1]:.2f}/x + {params_trans[2]:.2f}\n'
           f'Neural Transducer: WER = {params_neural[0]:.2f}·ln(x) + {params_neural[1]:.2f}/x + {params_neural[2]:.2f}\n'
           f'Attentive LSTM: WER = {params_atten[0]:.2f}·ln(x) + {params_atten[1]:.2f}/x + {params_atten[2]:.2f}')
plt.annotate(eq_text, xy=(0.5, 0.02), xycoords='figure fraction', 
             ha='center', fontsize=9, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7))

# plt.savefig('graph.png')
plt.show()

