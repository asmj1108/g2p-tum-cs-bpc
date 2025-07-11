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
3. For training, the data amount for each language is set to 1000 and the data samples are randomly selected if there are more available.
4. All datasets are randomly split into 80% training data, 10% development data, and 10% test data.
5. For ben/bur/ger/gle/ita/per/swe/tha (some target languages from the 2022 task), the test set values were from a
   [public dataset](https://github.com/CUNY-CL/wikipron/tree/master/data/scrape) that uses the same tool as in the
   shared tasks

---

| Language               | Code    | Data Samples | Origin                            |
|------------------------|---------|--------------|-----------------------------------|
| American English       | eng_us  | 41680        | 2021                              |
| Dutch                  | nld     | 10348        | 2021 + 2022                       |
| Eastern Armenian       | hye     | 10000        | 2021                              |
| French                 | fra     | 10000        | 2021                              |
| Georgian               | kat     | 10000        | 2021                              |
| Serbo-Croatian (Latin) | hbs     | 10000        | 2021                              |
| Hungarian              | hun     | 10000        | 2021                              |
| Japanese (Hiragana)    | jpn     | 10000        | 2021                              |
| Korean (Hangul)        | kor     | 10000        | 2021                              |
| Vietnamese (Hanoi)     | vie     | 10000        | 2021                              |
| Hindi                  | hin     | 4500         | 2020                              |
| Lithuanian             | lit     | 4500         | 2020                              |
| Arabic                 | arb     | 3000         | 2024                              |
| Bulgarian              | bul     | 3000         | 2024                              |
| Indonesian             | ind     | 3000         | 2024                              |
| Macedonian             | mkd     | 3000         | 2024                              |
| Classical Persian      | fas_cls | 3000         | 2024                              |
| Russian                | rus     | 3000         | 2024                              |
| Spanish                | spa     | 3000         | 2024                              |
| Tagalog                | tgl     | 3000         | 2024                              |
| Ukrainian              | ukr     | 3000         | 2024                              |
| Urdu                   | urd     | 3000         | 2024                              |
| Uyghur                 | uig     | 2158         | scraped                           |
| Romanian               | ron     | 1997         | 2021 + 2022                       |
| Italian                | ita     | 1824         | 2021 + 2022                       |
| Adyghe                 | ady     | 1000         | 2021                              |
| Assamese               | asm     | 1000         | 2022                              |
| Belarusian             | bel     | 1000         | 2022                              |
| Bengali                | ben     | 1000         | 2022 (729) + scraped (271)        | 
| Burmese                | mya     | 1000         | 2022                              |
| Cebuano                | ceb     | 1000         | 2022 (126) + scraped (847)        | 
| Central Khmer          | khm     | 1000         | 2021                              |
| Eastern Lawa           | lwl     | 1000         | 2022 (253) + oversampled          |
| German                 | deu     | 1000         | 2022                              |
| Greek                  | ell     | 1000         | 2021                              |
| Irish                  | gle     | 1000         | 2022                              |
| Icelandic              | isl     | 1000         | 2021                              |
| Latvian                | lav     | 1000         | 2021                              |
| Maltese (Latin)        | mlt     | 1000         | 2021                              |
| Norwegian Nynorsk      | nno     | 1000         | 2022                              |
| Pashto                 | pus     | 1000         | 2022 (721) + scraped (262) + o.s. | 
| Iranian Persian        | pes     | 1000         | 2022 (565) + o.s.                 |
| Polish                 | pol     | 1000         | scraped                           |
| Shan                   | shn     | 1000         | 2022 (841) + scraped (157)        | 
| Slovenian              | slv     | 1000         | 2021                              |
| Swedish                | swe     | 1000         | 2022                              |
| Thai                   | tha     | 1000         | 2022                              |
| Welsh                  | cym     | 1000         | 2022                              |

### Other Datasets

| Language                  | Code          | Data Samples | Origin                  |
|---------------------------|---------------|--------------|-------------------------|
| Arabic (Latin)            | arb_ept       | 1000         | Romanized using Epitran |
| Arabic (Latin)            | arb_latin     | 1000         | Romanized using uroman  |
| Bulgarian (Latin)         | bul_latin     | 1000         | Romanized using uroman  |
| Classical Persian (Latin) | fas_cls_ept   | 1000         | Romanized using Epitran |
| Classical Persian (Latin) | fas_cls_latin | 1000         | Romanized using uroman  |
| Eastern Armenian (Latin)  | hye_latin     | 1000         | Romanized using uroman  |
| Greek (Latin)             | ell_latin     | 1000         | Romanized using uroman  |
| Korean (Jamo)             | kor_jamo      | 1000         | Decomposed from Hangul  |
| Macedonian (Latin)        | mkd_latin     | 1000         | Romanized using uroman  |
| Pashto (Latin)            | pus_latin     | 1000         | Romanized using uroman  |
| Russian (Latin)           | rus_latin     | 1000         | Romanized using uroman  |
| Ukrainian (Latin)         | ukr_latin     | 1000         | Romanized using uroman  |
| Urdu (Latin)              | urd_ept       | 1000         | Romanized using Epitran |
| Urdu (Latin)              | urd_latin     | 1000         | Romanized using uroman  |
| Uyghur (Latin)            | uig_ept       | 1000         | Romanized using Epitran |
| Uyghur (Latin)            | uig_latin     | 1000         | Romanized using uroman  |

Used Tool:

- [Hangul syllable decomposition](https://github.com/JDongian/python-jamo)
- [uroman: Universal Romanizer](https://github.com/isi-nlp/uroman)
- [Epitran: Orthographic Text to IPA Transliteration](https://github.com/dmort27/epitran)

# Category

<table><thead>
  <tr>
    <th>Family/Script</th>
    <th>Branch</th>
    <th>Latin</th>
    <th>Cyrillic</th>
    <th>Arabic</th>
    <th>Georgian</th>
    <th>Greek</th>
    <th>Armenian</th>
    <th>Hangul</th>
    <th>Hiragana</th>
    <th>Devanagari</th>
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
    <td>Serbo-Croatian, Lithuanian, Latvian, Slovenian, Polish</td>
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
    <td></td>
  </tr>
  <tr>
    <td>Celtic</td>
    <td>Irish, Welsh</td>
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
    <td></td>
    <td></td>
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
  </tr>
  <tr>
    <td>Armenian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Eastern Armenian</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Indo-Iranian</td>
    <td></td>
    <td></td>
    <td>Urdu, Classical | Iranian Persian, Pashto</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Hindi</td>
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
    <td></td>
    <td></td>
    <td>Japanese</td>
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
    <td>Vietnamese</td>
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
    <td>Maltese</td>
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
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Northwest Caucasian</td>
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
  <tr>
    <td>Turkic</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Uyghur</td>
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
