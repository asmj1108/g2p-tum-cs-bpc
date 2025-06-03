# Our Results

| Language                 | Pair n-gram Model<br/>(baseline 2020) | Transformer<br/>(baseline 2020) | Neural transducer<br/>(baseline 2021/22) | hard_attention_GRU<br/>(baseline 2024) |
|--------------------------|---------------------------------------|---------------------------------|------------------------------------------|----------------------------------------|
| Adyghe                   | 27.00                                 | 39.00                           | 20.00                                    | 41.00                                  |
| Armenian (Eastern)       | 17.00                                 | 16.00                           | 15.00                                    | 58.00                                  |
| Arabic                   | 43.00                                 | 43.00                           | 53.00                                    | 58.00                                  |
| Assamese                 | 14.00                                 | 15.00                           | 7.00                                     | 15.00                                  |
| Belarusian               | 7.00                                  | 6.00                            | 2.00                                     | 10.00                                  |
| Bengali                  | 70.00                                 | 78.00                           | 68.00                                    | 80.00                                  |
| Bulgarian                | 37.00                                 | 30.00                           | 32.00                                    | 50.00                                  |
| Cebuano                  | 22.00                                 | 26.00                           | 20.00                                    | 53.00                                  |
| Central Khmer            | 56.00                                 | 43.00                           | 31.00                                    | 52.00                                  |
| Dutch                    | 32.00                                 | 29.00                           | 24.00                                    | 37.00                                  |
| Eastern Lawa             | 44.00                                 | 24.00                           | 8.00                                     | 47.00                                  |
| English                  | 70.00                                 | 70.00                           | 63.00                                    | 73.00                                  |
| French                   | 31.00                                 | 29.00                           | 23.00                                    | 46.00                                  |
| Georgian                 | 0.00                                  | 4.00                            | 0.00                                     | 9.00                                   |
| German                   | 49.00                                 | 56.00                           | 46.00                                    | 64.00                                  |
| Greek                    | 27.00                                 | 26.00                           | 20.00                                    | 41.00                                  |
| Hindi                    | 23.00                                 | 24.00                           | 11.00                                    | 39.00                                  |
| Hungarian                | 9.00                                  | 11.00                           | 7.00                                     | 17.00                                  |
| Icelandic                | 35.00                                 | 24.00                           | 12.00                                    | 36.00                                  |
| Indonesian               | 58.00                                 | 52.00                           | 64.00                                    | 62.00                                  |
| Irish                    | 57.00                                 | 46.00                           | 43.00                                    | 53.00                                  |
| Italian                  | 22.00                                 | 21.00                           | 15.00                                    | 30.00                                  |
| Japanese (Hiragana)      | 23.00                                 | 20.00                           | 10.00                                    | 21.00                                  |
| Korean                   | 81.00                                 | 89.00                           | 23.00                                    | 98.00                                  |
| Latvian                  | 51.00                                 | 51.00                           | 51.00                                    | 54.00                                  |
| Lithuanian               | 32.00                                 | 35.00                           | 33.00                                    | 44.00                                  |
| Macedonian               | 6.00                                  | 5.00                            | 5.00                                     | 17.00                                  |
| Maltese (Latin)          | 27.00                                 | 24.00                           | 17.00                                    | 31.00                                  |
| Norwegian Nynorsk        | 61.00                                 | 69.00                           | 66.00                                    | 68.00                                  |
| Pashto                   | 70.00                                 | 68.00                           | 67.00                                    | 68.00                                  |
| Persian (Classical)      | 51.00                                 | 58.00                           | 57.00                                    | 60.00                                  |
| Persian (Iranian)        | 66.00                                 | 63.00                           | 65.00                                    | 69.00                                  |
| Romanian                 | 10.00                                 | 17.00                           | 9.00                                     | 32.00                                  |
| Russian                  | 31.00                                 | 21.00                           | 23.00                                    | 35.00                                  |
| Serbo-Croatian (Latin)   | 84.00                                 | 69.00                           | 64.00                                    | 72.00                                  |
| Shan                     | 6.00                                  | 10.00                           | 5.00                                     | 21.00                                  |
| Slovenian                | 73.00                                 | 52.00                           | 56.00                                    | 62.00                                  |
| Spanish                  | 3.00                                  | 10.00                           | 4.00                                     | 18.00                                  |
| Swedish                  | 67.00                                 | 68.00                           | 59.00                                    | 68.00                                  |
| Tagalog                  | 11.00                                 | 17.00                           | 13.00                                    | 20.00                                  |
| Thai                     | 70.00                                 | 49.00                           | 39.00                                    | 62.00                                  |
| Ukrainian                | 27.00                                 | 26.00                           | 19.00                                    | 23.00                                  |
| Urdu                     | 67.00                                 | 66.00                           | 72.00                                    | 81.00                                  |
| Vietnamese (Hanoi)       | 44.00                                 | 20.00                           | 5.00                                     | 12.00                                  |
| Welsh                    | 33.00                                 | 20.00                           | 12.00                                    | 27.00                                  |
| Welsh (Southern Dialect) | 28.00                                 | 18.00                           | 13.00                                    | 27.00                                  |
| **Macro-average WER**    | **38.53**                             | **36.13**                       | **29.79**                                | **44.98**                              |

---
## Models

### 2022
**Baseline**: A neural transducer system using an imitation learning paradigm (dyNET framework)

**Submissions**:
1. [Tü-G2P](https://aclanthology.org/2023.sigmorphon-1.28.pdf): A series of sequence labelling systems to G2P tasks, 
which use ​simpler alignment​ rather than dynamic transducer-based alignment.(Pytorch) 
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
#### Reference Result:

- Baseline

| Models                | gru   | lstm  | attentive_gru | attentive_lstm | hard_attention_gru | hard_attention_gru (Arab) | pointer_generator_gru | transducer_gru | transformer_20 | transformer_40 | transformer_60 |
|-----------------------|-------|-------|---------------|----------------|--------------------|--------------------------|----------------------|----------------|----------------|----------------|----------------|
| WER (%)               | 43.75 | 44.25 | 63.08         | 47.25          | 40.67              | 31.33                    | 62.17                | 69.33          | 78.25          | 81.58          | 79.50          |

- Best performance model on all datasets(hard_attenton_gru)

| Languages  | Arabic | Bulgarian | English | Persian | Indonesian | Macedonian | Pashto | Russian | Spanish | Tagalog | Ukrainian | Urdu |
|------------|--------|-----------|---------|---------|------------|------------|--------|---------|---------|---------|-----------|------|
| WER        | 31.33  | 20.00     | 58.00   | 29.67   | 55.33      | 3.67       | 44.33  | 10.33   | 5.00    | 40.33   | 15.67     | 64.00 |

- GRU、LSTM、Transformer on different languages
  
| Model/Languages   | English | Pashto | Russian | Spanish |
|-------------------|---------|--------|---------|---------|
| GRU               | 31.00   | 39.00  | 14.00   | 9.00    |
| LSTM              | 48.33   | 57.67  | 10.33   | 9.00    |
| Transformer       | 81.33   | 77.00  | 35.67   | 24.67   |



---

|          | Transformer<br/>(baseline 2020) | Neural transducer<br/>(baseline 2021) | Yoyodyne<br/>(baseline 2024) |
|----------|---------------------------------|---------------------------------------|------------------------------| 
| Adyghe   |                                 | 22.00                                 |                              |
| Bengali  |                                 | 67.12                                 |                              |
| French   | 6.89                            |                                       |                              |
| German   |                                 | 53.00                                 |                              |
| Greek    |                                 | 20.00                                 |                              |
| Icelandic|                                 | 11.00                                 |                              |
| Italian  |                                 | 17.00                                 |                              |
| Khmer    |                                 | 36.00                                 |                              |
| Latvian  |                                 | 54.00                                 |                              |
| Maltese_L|                                 | 18.00                                 |                              |
| Maori    |                                 |                                       | 41.30                        |
| Romanian |                                 | 10.00                                 |                              |
| Slovene  |                                 | 49.00                                 |                              |
| Welsh_sw |                                 | 13.00                                 |                              |
