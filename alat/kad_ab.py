"""Kad akhir A/B (soalan debat 2 pilihan) untuk Diari Duit Tunas.
Ditindih atas kad akhir asal + dipanjangkan 1 s supaya sempat dibaca.
Guna: python3 alat/kad_ab.py  (keluarkan video/diari-duit-tunas-epN-ab.mp4)
"""
import subprocess, os
from PIL import Image, ImageDraw, ImageFont

F = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
DARK, YEL, RED, GRN = (59, 42, 26), (255, 214, 64), (212, 87, 75), (76, 160, 60)

EP = {
    'ep2': dict(mula=16.2, soalan=['Kalau korang', 'jadi Tunas?'],
                a='Bagi semua RM212', b='Bagi separuh, cakap jujur',
                bawah='Ep 3: kawan ajak "join"'),
    'ep3': dict(mula=15.5, soalan=['Kawan ajak join.', 'Korang buat apa?'],
                a='Cuba RM100 dulu', b='Tanya 3 soalan dulu',
                bawah='Modul anti-scam PERCUMA'),
    'ep4-a': dict(mula=15.5, soalan=['Saham RM50, kos RM9.', 'Korang pilih?'],
                  a='Beli juga 1 lot', b='Kumpul dulu, baru beli',
                  bawah='Cuba 3 hari PERCUMA · *angka contoh'),
}
EP['ep4-b'] = EP['ep4-a']


def font(s):
    return ImageFont.truetype(F, s)


def kad(c, out):
    im = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 70, 560, 1010, 1520
    d.rounded_rectangle((x0, y0 + 14, x1, y1 + 14), 48, fill=DARK)
    d.rounded_rectangle((x0, y0, x1, y1), 48, fill=(255, 255, 255), outline=DARK, width=8)
    # label pematuhan (kad akhir asal pudar, jadi tulis semula dengan jelas)
    lab = 'Watak & cerita rekaan · Bahan pendidikan, bukan nasihat pelaburan'
    f = font(28)
    w = d.textlength(lab, font=f)
    d.rounded_rectangle(((1080 - w) / 2 - 20, 1830, (1080 + w) / 2 + 20, 1885), 20, fill=(255, 248, 230))
    d.text(((1080 - w) / 2, 1838), lab, font=f, fill=DARK)
    y = y0 + 60
    for ln in c['soalan']:
        f = font(72)
        w = d.textlength(ln, font=f)
        d.text(((1080 - w) / 2, y), ln, font=f, fill=DARK)
        y += 92
    y += 40
    for huruf, teks, col in (('A', c['a'], RED), ('B', c['b'], GRN)):
        d.rounded_rectangle((120, y, 960, y + 150), 36, fill=(255, 248, 230), outline=DARK, width=6)
        d.ellipse((145, y + 25, 245, y + 125), fill=col, outline=DARK, width=5)
        f = font(64)
        d.text((195 - d.textlength(huruf, font=f) / 2, y + 30), huruf, font=f, fill=(255, 255, 255))
        f = font(50)
        d.text((275, y + 42), teks, font=f, fill=DARK)
        y += 185
    y += 15
    f = font(66)
    t = 'Komen A atau B'
    w = d.textlength(t, font=f)
    d.rectangle(((1080 - w) / 2 - 24, y + 8, (1080 + w) / 2 + 24, y + 92), fill=YEL)
    d.text(((1080 - w) / 2, y), t, font=f, fill=DARK, stroke_width=0)
    y += 120
    f = font(38)
    w = d.textlength(c['bawah'], font=f)
    d.text(((1080 - w) / 2, y), c['bawah'], font=f, fill=(110, 90, 70))
    im.save(out)


if __name__ == '__main__':
    os.makedirs('/tmp/kad_ab', exist_ok=True)
    for e, c in EP.items():
        png = f'/tmp/kad_ab/{e}.png'
        kad(c, png)
        src = f'video/diari-duit-tunas-{e}.mp4'
        dst = f'video/diari-duit-tunas-{e}-ab.mp4'
        st = c['mula']
        vf = (f"[0:v]tpad=stop_mode=clone:stop_duration=1[v];"
              f"[1:v]format=rgba,fade=in:st=0:d=0.25:alpha=1,setpts=PTS+{st}/TB[k];"
              f"[v][k]overlay=0:0:enable='gte(t,{st})':eof_action=repeat[o]")
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-loop', '1', '-t', '4', '-i', png,
                        '-filter_complex', vf, '-map', '[o]', '-map', '0:a',
                        '-af', 'apad=pad_dur=1,afade=out:st=18.2:d=0.8', '-t', '19',
                        '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-movflags', '+faststart', dst],
                       check=True)
        print('siap', dst)
