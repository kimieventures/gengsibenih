# Siri: Dari Celik ke Sistem (Naluri vs Data)
Siri video pendidikan keluarga Geng Si Benih. Pipeline sama seperti video GSB lain (`alat/`).

## Struktur folder
| Folder | Isi |
|---|---|
| `00-konsep/` | Konsep siri, watak, format, garis merah |
| `01-skrip/` | Skrip TTS `epXX-<tajuk>.json` (N=Naluri/Osman, D=Data/Yasmin) |
| `02-storyboard/` | Storyboard `epXX-storyboard.html` (disemak Azizul sebelum gambar dijana) |
| `03-gambar/epXX/` | Gambar Gemini (nama fail ikut README dalam folder episod) |
| `04-audio/epXX/` | Hasil `alat/tts.py` |
| `05-babak/epXX/` | Skrip babak + HTML |
| `06-render/` | Video siap `dcks-epXX-<tajuk>.mp4` (salinan akhir juga ke `video/`) |
| `templat/` | Templat grafik dikongsi (carta purata, pai, kad soalan/jawapan, kad akhir) |

## Aliran kerja
1 Skrip → 2 Storyboard (semakan Azizul) → 3 Gambar (4 gambar, Gemini) → 4 Audio + babak → 5 Semak 4–6 frame → 6 Render sekali.

## Status episod
| EP | Tajuk | Bab | Skrip | Storyboard | Gambar | Video |
|---|---|---|---|---|---|---|
| 01 | Terlepas Bas | 5 | ✅ draf 3 | ✅ v2 | ➖ (gaya emoji) | ✅ emoji v2, menunggu semakan |
| 02 | Bila nak KELUAR? | 2 | ✅ | ➖ | ➖ | ✅ v1 |
| 03 | Strategi yang dibuang | 3 | ✅ | ➖ | ➖ | ✅ v1 |
| 04 | Butang kecemasan | 4 | ✅ | ➖ | ➖ | ✅ v1 |
| 05 | Kebal scam | 6 | ✅ | ➖ | ➖ | ✅ v1 |
| 06 | Tambah modal bila rugi | 1 | ✅ | ➖ | ➖ | ✅ v1 |

## Gaya visual (keputusan Azizul 26/11)
Watak emoji chat (set Noto, lesen terbuka): Naluri = emoji muka ikut emosi, Data = 🤖. Tanpa gambar CGI. Skrip babak masih menyokong `GAYA=foto` untuk ujian A/B.
V2: watak bergerak bila bercakap, reaksi emoji pada punchline, zoom + gegar, kesan bunyi, jeda lawak (krik krik).
