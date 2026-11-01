# Alat video Geng Si Benih

Penjana video animasi 30 s (1080x1920, 30 fps) dan muzik latar asli.

1. `npm install` (fon), Playwright + Chromium + ffmpeg mesti tersedia.
2. Tulis babak baharu dalam fail seperti `videos2.py` (guna `engine.py`: cap, ch, bub, ntf, big, emo, item, ending).
3. `python3 videosN.py` -> `html/<nama>.html`
4. Semak frame: `node still.js $PWD/html/<nama>.html 3 10 20`
5. Render: `node render.js $PWD/html/<nama>.html $PWD/out/<nama>.mp4 30`
6. Muzik: `python3 muzik.py` (out/muzik-ceria.wav, out/muzik-nakal.wav), kemudian
   `ffmpeg -i out/<nama>.mp4 -i out/muzik-ceria.wav -map 0:v -map 1:a -c:v copy -af loudnorm=I=-16:TP=-1.5 -c:a aac -shortest ../video/<nama>.mp4`
7. Commit ke `video/`, guna URL raw dipin pada SHA commit untuk Metricool.

Watak & cerita rekaan. Bahan pendidikan, bukan nasihat pelaburan.
