# Jadual Robot Post (dibaca terus oleh Robot.gs)

Robot Post (Apps Script) baca fail dalam folder ini setiap jam (melalui raw.githubusercontent.com) dan masukkan baris baharu ke tab JadualPost. Tak perlu browser atau laptop.

## jadual.json (fail bergulir)
Senarai baris: `["YYYY-MM-DD HH:MM", "ig|fb|th", "<url video raw atau kosong>", "<kapsyen>", "<komen pertama atau kosong>"]`
- Masa waktu Malaysia. URL video mesti bermula `https://raw.githubusercontent.com/kimieventures/gengsibenih/`.
- Hanya baris yang masanya AKAN DATANG dimasukkan. Baris berganda (masa + platform sama dengan yang dah ada dalam sheet) diabaikan, jadi selamat ulang.
- Tambah baris baharu ke hujung senarai; baris lama boleh dibuang selepas masanya lepas. Masukkan sekurang-kurangnya 2 jam sebelum masa post (robot semak setiap jam).
- Untuk betulkan baris yang SUDAH masuk sheet: tak boleh dari sini (berganda diabaikan) — guna gantian.json atau minta Azizul.

## gantian.json
`[{"dari": "nama.mp4", "ke": "nama-hook.mp4", "kapDepan": "teks di depan kapsyen (pilihan)"}]`
Robot tukar video (dan tambah teks depan kapsyen) semasa post. Dibaca semula setiap jam.

Garis merah pematuhan & label wajib kekal: lihat alat/README.md dan projek Claude.
