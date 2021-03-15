# conver_quran_txt_to_json

full quran text and UthmanicHafs.ttf font source: qurancomplex.gov.sa

goal of this python project is to convert fullQuran.txt to json array of object "surah"

- surah name and verses are object of language codes to allow for easy translation in future.
- basmalah should be first verse for Fatihah only.

Example
```json
[
  {
    "id": 0,
    "name": { 
      "en": "Fatihah",
      "ar": "الفاتحة"
    },
    "verses": [
      {
        "id": 0,
        "verse": {
          "ar": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
          "en": "In the Name of Allah—the Most Compassionate, Most Merciful.",
        }
      },
    ]
  },
  {
    "id": 113,
    "name": { 
      "en": "an-Nas",
      "ar": "الناس"
    },
    "verses": [
      {
        "id": 0,
        "verse": {
          "ar": "قُلۡ أَعُوذُ بِرَبِّ ٱلنَّاسِ",
          "en": "Say, ˹O Prophet,˺ “I seek refuge in the Lord of humankind,",
        }
      },
    ]
  }
]
```
