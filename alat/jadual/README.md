# Jadual Robot Post (dibaca terus oleh Robot.gs)

Robot Post (Apps Script) semak folder ini setiap jam dan masukkan baris baharu ke tab JadualPost.
Tak perlu browser atau laptop.

## jadual-YYYY-MM-DD.json
Senarai baris: `["YYYY-MM-DD HH:MM", "ig|fb|th", "<url video raw atau kosong>", "<kapsyen>", "<komen pertama atau kosong>"]`
- Masa waktu Malaysia. URL video mesti bermula `https://raw.githubusercontent.com/kimieventures/gengsibenih/`.
- Setiap fail diproses SEKALI (ikut sha). Untuk tambah baris, cipta fail baharu (cth jadual-2026-12-07.json), jangan sunting fail lama.
- Baris berganda (masa + platform sama) diabaikan.

## gantian.json
`[{"dari": "nama.mp4", "ke": "nama-hook.mp4", "kapDepan": "teks di depan kapsyen (pilihan)"}]`
Robot tukar video (dan tambah teks depan kapsyen) semasa post. Dibaca semula setiap jam.

Garis merah pematuhan & label wajib kekal: lihat alat/README.md dan projek Claude.
