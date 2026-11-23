# Fail Duit Tunas — templat "scrapbook berita"

Kes sebenar (berita) → pengajaran Tunas → CTA. Contoh lengkap: `kes01.py` + `fd1.json` (video: `../../video/fail-duit-tunas-kes01.mp4`).

1. Pilih kes dari berita bersumber (Kosmo/BH/Bernama/The Star). Catat URL + tarikh dalam json `sumber`. Tiada nama suspek/mangsa, tiada nama saham/broker.
2. Tulis `fdN.json` (baris K = Kuntum narator, T = Tunas pengajaran). `python3 ../tts.py fdN.json`
3. Salin `kes01.py` → `kesNN.py`, tukar babak. `python3 kesNN.py` → `fdN.html` + audio.
4. Semak: `node ../still.js $PWD/fdN.html 0 20 60` ; render: `node ../render.js $PWD/fdN.html $PWD/fdN_video.mp4 <T>` ; mux: `ffmpeg -i fdN_video.mp4 -i fdN_audio.m4a -c copy -shortest ../../video/fail-duit-tunas-kesNN.mp4`.
Label wajib: rumusan berita · watak rekaan · ilustrasi · suara AI · bahan pendidikan, bukan nasihat pelaburan.
