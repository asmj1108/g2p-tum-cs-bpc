# Our Results

|          | Transformer<br/>(baseline 2020) | Neural transducer<br/>(baseline 2021) | Yoyodyne<br/>(baseline 2024) |
|----------|---------------------------------|---------------------------------------|------------------------------| 
| Adyghe   |                                 | 22.00                                 |                              |
| French   | 6.89                            |                                       |                              |
| Greek    |                                 | 20.00                                 |                              |
| Icelandic|                                 | 11.00                                 |                              |
| Khmer    |                                 | 36.00                                 |                              |
| Latvian  |                                 | 54.00                                 |                              |
| Maltese_L|                                 | 18.00                                 |                              |
| Maori    |                                 |                                       | 41.30                        |
| Romanian |                                 | 10.00                                 |                              |
| Slovene  |                                 | 49.00                                 |                              |
| Welsh_sw |                                 | 13.00                                 |                              |

---
## Models

### 2022
**Baseline**: A neural transducer system using an imitation learning paradigm (dyNET framework)

**Submissions**:
1. Tü-G2P:
2. [Hammond](https://aclanthology.org/2023.sigmorphon-1.29.pdf) ([Repo](https://github.com/hammondm/g2p2022)): A 
non-neural system based on OpenFST and uses weighted finite-state transducers and expectation-maximization to compute 
the best many-to-many alignment of letters and phonetic symbol 
3. ~~[mSLAM](https://aclanthology.org/2023.sigmorphon-1.31.pdf): Non-archival; abstract only;~~ useless
4. ~~[NFST](https://aclanthology.org/2023.sigmorphon-1.30.pdf): Non-archival; abstract only;~~ useless

---

## Languages

### 2022
#### Reference Result:

- Baseline

| Language | Bengali | Burmese | German | Irish | Italian | Persian | Swedish | Tagalog | Thai  | Ukrainian | Macro-average |
|----------|---------|---------|--------|-------|---------|---------|---------|---------|-------|-----------|---------------|
| WER      | 67.12   | 29.00   | 42.00  | 38.00 | 15.00   | 59.65   | 45.00   | 20.00   | 21.00 | 32.00     | 36.88         |

- Hammond (trigram alignment)

| Language | Bengali | Burmese | German | Irish | Italian | Persian | Swedish | Tagalog | Thai  | Ukrainian | Macro-average |
|----------|---------|---------|--------|-------|---------|---------|---------|---------|-------|-----------|---------------|
| WER      | 68.49   | 48.00   | 61.00  | 51.00 | 25.00   | 67.86   | 55.00   | 18.00   | 72.00 | 50.00     | 51.63         |

---
## Models

### 2024
**Baseline**: attentive_gru, attentive_lstm, gru, hard_attention_gru, lstm, pointer_generator_gru, transducer_gru, transformer(20\40\60 epochs)


## Languages

### 2024
#### Reference Result(different results of abjad, a multilingual set):

- Baseline

| Models                | gru   | lstm  | attentive_gru | attentive_lstm | hard_attention_gru | hard_attention_gru (Arab) | pointer_generator_gru | transducer_gru | transformer_20 | transformer_40 | transformer_60 |
|-----------------------|-------|-------|---------------|----------------|--------------------|--------------------------|----------------------|----------------|----------------|----------------|----------------|
| Accuracy              | 56.25 | 55.75 | 36.92         | 52.75          | 59.33              | 68.67                    | 37.83                | 30.67          | 21.75          | 18.42          | 20.50          |