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

---

| **Family**              | **Latin**                                                                                                                                                                                                           | **Armenian**        | **Georgian** | **Cyrillic**                                           | **Hiragana**            | **Hangul** | **Devanagari** | **Arabic**                                            | **Bengali-Assamese** | **Burmese** | **Khmer**        | **Thai**         | **Greek** | **Shan** |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|--------------|--------------------------------------------------------|-------------------------|------------|----------------|-------------------------------------------------------|----------------------|-------------|------------------|------------------|-----------|----------|
| **Indo-European**       | English, Dutch, French, Serbo-Croatian (Latin), Hungarian, Lithuanian, Spanish, Romanian, Italian, Irish, Icelandic, Latvian, Norwegian Nynorsk, Slovenian, Swedish, Welsh, Welsh (Southern Dialect), German, Greek | Armenian (Eastern)  |              | Russian, Ukrainian, Bulgarian, Macedonian, Belarusian  |                         |            | Hindi          | Urdu, Persian (Classical), Persian (Iranian), Pashto  | Bengali, Assamese    |             |                  |                  | Greek     |          |
| **Kartvelian**          |                                                                                                                                                                                                                     |                     | Georgian     |                                                        |                         |            |                |                                                       |                      |             |                  |                  |           |          |
| **Japonic**             |                                                                                                                                                                                                                     |                     |              |                                                        | Japanese (Hiragana)     |            |                |                                                       |                      |             |                  |                  |           |          |
| **Koreanic**            |                                                                                                                                                                                                                     |                     |              |                                                        |                         | Korean     |                |                                                       |                      |             |                  |                  |           |          |
| **Austroasiatic**       | Vietnamese (Hanoi)                                                                                                                                                                                                  |                     |              |                                                        |                         |            |                |                                                       |                      |             | Central Khmer    | Eastern Lawa     |           |          |
| **Austronesian**        | Indonesian, Tagalog, Cebuano                                                                                                                                                                                        |                     |              |                                                        |                         |            |                |                                                       |                      |             |                  |                  |           |          |
| **Afro-Asiatic**        | Maltese (Latin)                                                                                                                                                                                                     |                     |              |                                                        |                         |            |                | Arabic                                                |                      |             |                  |                  |           |          |
| **Northwest Caucasian** |                                                                                                                                                                                                                     |                     |              | Adyghe                                                 |                         |            |                |                                                       |                      |             |                  |                  |           |          |
| **Sino-Tibetan**        |                                                                                                                                                                                                                     |                     |              |                                                        |                         |            |                |                                                       |                      | Burmese     |                  |                  |           |          |
| **Tai-Kadai**           |                                                                                                                                                                                                                     |                     |              |                                                        |                         |            |                |                                                       |                      |             |                  | Thai             |           | Shan     |
| **Uralic**              | Hungarian                                                                                                                                                                                                           |                     |              |                                                        |                         |            |                |                                                       |                      |             |                  |                  |           |          |

---
# Category

<table><thead>
  <tr>
    <th>Family/Script</th>
    <th>Branch</th>
    <th>Latin</th>
    <th>Greek</th>
    <th>Cyrillic</th>
    <th>Georgian</th>
    <th>Arabic</th>
    <th>Hiragana</th>
    <th>Hangul</th>
    <th>Devanagari</th>
    <th>Armenian</th>
    <th>Bengali-Assamese</th>
    <th>Mon-Burmese</th>
    <th>Khmer</th>
    <th>Thai</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="7">Indo-European</td>
    <td>Germanic</td>
    <td>English, Dutch, Icelandic, Norwegian Nynorsk, Swedish, German</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Italic</td>
    <td>French, Spanish, Romanian, Italian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Balto-Slavic</td>
    <td>Serbo-Croatian (Latin), Lithuanian, Latvian, Slovenian</td>
    <td></td>
    <td>Russian, Ukrainian, Bulgarian, Macedonian, Belarusian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Celtic</td>
    <td>Irish, Welsh, Welsh (Souther Dialect)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hellenic</td>
    <td></td>
    <td>Greek</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Armenian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Armenian (Eastern)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Indo-Iranian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Urdu, Persian (Classical | Iranian), Pashto</td>
    <td></td>
    <td></td>
    <td>Hindi</td>
    <td></td>
    <td>Bengali, Assamese</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Kartvelian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Georgian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Japonic</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Japanese (Hiragana)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Koreanic</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Korean</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Austroasiatic</td>
    <td></td>
    <td>Vietnamese (Hanoi)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Central Khmer</td>
    <td>Eastern Lawa</td>
  </tr>
  <tr>
    <td>Austronesian</td>
    <td></td>
    <td>Indonesian, Tagalog, Cebuano</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Afro-Asiatic</td>
    <td></td>
    <td>Maltese (Latin)</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Arabic</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Northwest Caucasian</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Adyghe</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Sino-Tibetan</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Burmese</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Tai-Kadai</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Shan</td>
    <td></td>
    <td>Thai</td>
  </tr>
  <tr>
    <td>Uralic</td>
    <td></td>
    <td>Hungarian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody></table>