# Unified Dataset

### Note

1. Data from 2021 and 2022 were preprocessed using consistent methods and are of higher quality than 2020 data due to
   improved quality assurance procedures.
    - For languages present in both 2020 and 2021/22 datasets, the 2021/22 data is used.
    - For languages present in both 2021 and 2022 datasets, the data are merged, with 2022 data taking precedence for
      overlapping words due to its recency.
2. Data from 2024 were preprocessed using different methods than the 2021/22 data.
    - Manual comparison and selection of datasets is required for languages that appear in both 2024 and 2021/22
      collections.
3. All datasets are randomly split into 80% training data, 10% development data, and 10% test data.
4. For ben/bur/ger/gle/ita/per/swe/tha (some target languages from the 2022 task), the test set values were from a
   [public dataset](https://github.com/CUNY-CL/wikipron/tree/master/data/scrape) that uses the same tool as in the
   shared tasks
   ~~independently obtained by our team and processed to match the available train/dev set format as closely as
   possible.~~

---

| Language                 | Code     | Data Samples | Origin                            |
|--------------------------|----------|--------------|-----------------------------------|
| English                  | eng_us   | 41680        | 2021                              |
| Dutch                    | dut      | 10348        | 2021 + 2022                       |
| Armenian (Eastern)       | arm_e    | 10000        | 2021                              |
| French                   | fre      | 10000        | 2021                              |
| Georgian                 | geo      | 10000        | 2021                              |
| Serbo-Croatian (Latin)   | hbs_latn | 10000        | 2021                              |
| Hungarian                | hun      | 10000        | 2021                              |
| Japanese (Hiragana)      | jpn      | 10000        | 2021                              |
| Korean                   | kor      | 10000        | 2021                              |
| Vietnamese (Hanoi)       | vie      | 10000        | 2021                              |
| Hindi                    | hin      | 4500         | 2020                              |
| Lithuanian               | lit      | 4500         | 2020                              |
| Arabic                   | ara      | 3000         | 2024                              |
| Bulgarian                | bul      | 3000         | 2024                              |
| Indonesian               | ind      | 3000         | 2024                              |
| Macedonian               | mkd      | 3000         | 2024                              |
| Persian (Classical)      | fas      | 3000         | 2024                              |
| Russian                  | rus      | 3000         | 2024                              |
| Spanish                  | spa      | 3000         | 2024                              |
| Tagalog                  | tgl      | 3000         | 2024                              |
| Ukrainian                | ukr      | 3000         | 2024                              |
| Urdu                     | urd      | 3000         | 2024                              |
| Romanian                 | rum      | 1997         | 2021 + 2022                       |
| Italian                  | ita      | 1824         | 2021 + 2022                       |
| Adyghe                   | ady      | 1000         | 2021                              |
| Assamese                 | asm      | 1000         | 2022                              |
| Belarusian               | bel      | 1000         | 2022                              |
| Bengali                  | ben      | 1000         | 2022 (729) + scraped (271)        | 
| Burmese                  | bur      | 1000         | 2022                              |
| Cebuano                  | ceb      | 1000         | 2022 (126) + scraped (847)        | 
| Central Khmer            | khm      | 1000         | 2021                              |
| Eastern Lawa             | lwl      | 1000         | 2022 (253) + oversampled          |
| German                   | ger      | 1000         | 2022                              |
| Greek                    | gre      | 1000         | 2021                              |
| Irish                    | gle      | 1000         | 2022                              |
| Icelandic                | ice      | 1000         | 2021                              |
| Latvian                  | lav      | 1000         | 2021                              |
| Maltese (Latin)          | mlt_latn | 1000         | 2021                              |
| Norwegian Nynorsk        | nno      | 1000         | 2022                              |
| Pashto                   | pus      | 1000         | 2022 (721) + scraped (262) + o.s. | 
| Persian (Iranian)        | per      | 1000         | 2022 (565) + o.s.                 |
| Shan                     | shn      | 1000         | 2022 (841) + scraped (157)        | 
| Slovenian                | slv      | 1000         | 2021                              |
| Swedish                  | swe      | 1000         | 2022                              |
| Thai                     | tha      | 1000         | 2022                              |
| Welsh                    | wel      | 1000         | 2022                              |
| Welsh (Southern Dialect) | wel_sw   | 1000         | 2021                              |

Persian (Iranian)
Pashto Wiktionary Max Available 983
Eastern Lawa Wiktionary Max Available 255
