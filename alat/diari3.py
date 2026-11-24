# Diari Duit Tunas Ep 5–7 (minggu 23 Nov 2026). Hook pada frame 0, 18 s, satu idea.
# Watak, kedai & harga rekaan. Angka contoh. Bahan pendidikan, bukan nasihat pelaburan.
from diari2 import *  # helper, CSS X, latar
import os

Y = """
.papan{left:90px;width:900px;top:690px;background:#2A2116;color:#FCEFC7;border:9px solid #1E1712;border-radius:40px;padding:34px 40px 40px;box-shadow:0 14px 0 #F5C04A}
.papan h3{margin:0 0 6px;text-align:center;font-family:Fredoka,sans-serif;font-size:54px;color:#F5C04A}
.papan .s{text-align:center;font-size:30px;color:#BFAE8C;margin-bottom:22px}
.papan .r{display:flex;justify-content:space-between;align-items:center;font-size:50px;padding:20px 8px;border-top:3px dashed #5A4A33}
.papan .r b{font-family:Fredoka,sans-serif;font-size:70px}
.papan .j b{color:#FF8A7A} .papan .bb b{color:#86C65A}
.chart{left:70px;width:940px;top:640px;height:900px;background:#fff;border:8px solid #1E1712;border-radius:40px;box-shadow:0 14px 0 #1E1712;padding:26px 30px}
.chart .t{font-size:40px;color:#5E4B37}
.chart .t b{color:#1E1712}
.stamp{left:0;right:0;text-align:center;font-family:Fredoka,sans-serif;font-size:96px}
"""
def P2(items, bgs): return P(items, bgs).replace('</style>', Y + '</style>', 1)
T = 18

# ---------- Ep 5: emas & DUA harga ----------
PAPAN = ('<h3>KEDAI EMAS CAHAYA</h3><div class="s">kedai & harga rekaan · emas 999 · per gram</div>'
         '<div class="r j"><span>Harga JUAL<br><small style="font-size:30px;color:#BFAE8C">(anda beli)</small></span><b>RM460</b></div>'
         '<div class="r bb"><span>Harga BELI BALIK<br><small style="font-size:30px;color:#BFAE8C">(anda jual semula)</small></span><b>RM425</b></div>')
V5 = {}
V5['diari-duit-tunas-ep5'] = P2([
    ep(T, 'Diari Duit Tunas · Ep 5'),
    hook(3.4, 'Jangan beli emas<br>sebelum tanya<br>DUA harga ni.', 'Tunas hampir terlepas 😬'),
    item(0, 9.4, PAPAN, '', 'papan', 'none'),
    item(5.6, 9.4, 'Beza RM35/g = <b style="color:#F5C04A">7.6%</b><br>hilang sebaik keluar kedai', 'left:60px;right:60px;top:1450px;font-size:58px;line-height:1.2;color:#FCEFC7', 'big', 'up'),
    item(9.4, 14.0, 'Saya ingat beli emas<br>= terus "untung".<br>Rupanya harga kena naik<br><b>±8% dulu</b> baru<br>pulang modal. 😮', '', 'diari', 'up'),
    emo(9.6, 14.0, '🪙', 760, 1240, 200),
    item(14.0, 16.0, '<h3>Sebelum beli</h3>Tanya: harga jual?<br>Harga beli balik?<br><b style="color:#C8473B">Beza ÷ harga jual</b> = kos anda', '', 'les', 'pop'),
    endc(16.0, T, 'Cuba 3 hari<br>PERCUMA 🌱<br>Link di bio'),
    nx(16.4, T, 'Ep 6: carta yang "menipu" mata 📈'),
    note(0, 9.4, True, 'Kedai & harga rekaan · Angka contoh · Bukan nasihat pelaburan'),
    note(9.4, T),
], [[0, DARK], [9.4, PAPER], [14.0, GOLD], [16.0, GREEN]])

# ---------- Ep 6: carta zoom-out (A/B hook) ----------
# Garis harga REKAAN. Minggu: naik. 5 tahun: jatuh jauh dari puncak.
WEEK = 'M40,560 L150,520 L260,540 L370,450 L480,470 L590,360 L700,300 L820,200'
YEARS = ('M40,120 L90,150 L140,110 L190,170 L240,230 L290,210 L340,300 L390,350 L440,330 L490,420 '
         'L540,470 L590,450 L640,520 L690,560 L740,540 L780,580 L800,560 L820,530')
def svg(path, col, dl=0.3, d=2.4):
    return (f'<svg width="880" height="680" viewBox="0 0 860 660" style="display:block;margin-top:20px">'
            f'<g stroke="#EADFC8" stroke-width="2">' + ''.join(f'<line x1="20" x2="840" y1="{y}" y2="{y}"/>' for y in (100, 250, 400, 550)) +
            f'</g><path d="{path}" fill="none" stroke="{col}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" data-draw="{d}" data-dl="{dl}"/></svg>')

def ep6(hk, sub):
    return P2([
        ep(T, 'Diari Duit Tunas · Ep 6'),
        hook(3.4, hk, sub),
        item(0, 6.4, '<div class="t"><b>Saham Contoh Bhd</b> (rekaan) · 1 MINGGU</div>' + svg(WEEK, '#3E9B2F', -1, 0.05), '', 'chart', 'none'),
        item(2.2, 6.4, '+20% 🚀', 'top:1580px;color:#3E7D1F', 'stamp', 'pop', 'pulse'),
        item(6.4, 10.8, '<div class="t"><b>Saham Contoh Bhd</b> (rekaan) · 5 TAHUN</div>' + svg(YEARS, '#C8473B', 0.2, 2.6), '', 'chart', 'none'),
        item(8.4, 10.8, 'Masih −60% dari puncak 😶', 'top:1580px;color:#C8473B;font-size:72px', 'stamp', 'pop'),
        item(10.8, 14.6, 'Carta sama. Cerita lain.<br>Yang ubah cuma<br><b>skala masa.</b><br>Saya hampir percaya<br>"+20%" tu. 😅', '', 'diari', 'up'),
        emo(11.0, 14.6, '🔍', 760, 1240, 200),
        item(14.6, 16.2, '<h3>Sebelum percaya carta</h3>Tanya: tempoh<br><b>berapa lama?</b><br>Zoom out dulu.', '', 'les', 'pop'),
        endc(16.2, T, 'Cuba 3 hari<br>PERCUMA 🌱<br>Link di bio'),
        nx(16.6, T, 'Ep 7: RM10 sehari ☕'),
        note(0, 10.8, False, 'Carta & syarikat rekaan · Bukan nasihat pelaburan'),
        note(10.8, T),
    ], [[0, PAPER], [10.8, PAPER], [14.6, GREEN], [16.2, GOLD]])

V5['diari-duit-tunas-ep6-a'] = ep6('Carta ni nampak naik.<br>Tunggu sampai hujung.', 'Saya hampir tertipu 👀')
V5['diari-duit-tunas-ep6-b'] = ep6('Naik 20% minggu ni.<br>Tapi tengok 5 tahun…', 'Zoom out 👇')

# ---------- Ep 7: RM10 sehari ----------
CALC7 = ('<div class="ln"><span>☕ Teh tarik + kuih</span><b>RM10 / hari</b></div>'
         '<div class="ln"><span>× 30 hari</span><b>RM300</b></div>'
         '<div class="ln"><span>× 365 hari</span><b>RM3,650</b></div>'
         '<div class="tot"><span>5 tahun</span><span>RM18,250</span></div>'
         '<div class="vs" style="font-size:40px;color:#BFAE8C"><span>tanpa sebarang pulangan, kira mudah</span><span></span></div>')
V5['diari-duit-tunas-ep7'] = P2([
    ep(T, 'Diari Duit Tunas · Ep 7'),
    hook(3.4, 'RM10 sehari.<br>Tak nampak banyak,<br>kan? ☕', 'Tunas kira sekali… 😳'),
    item(0, 9.4, CALC7, '', 'calc', 'none'),
    item(5.4, 9.4, 'Hampir <b style="color:#F5C04A">RM3,650</b> setahun.<br>Lebih sebulan gaji saya.', 'left:60px;right:60px;top:1500px;font-size:56px;line-height:1.2;color:#FCEFC7', 'big', 'up'),
    item(9.4, 14.2, 'Bukan nak berhenti<br>minum teh tarik. 😅<br>Saya cuma nak <b>pilih</b><br>ke mana RM10 tu pergi.', '', 'diari', 'up'),
    emo(9.6, 14.2, '📓', 760, 1240, 200),
    item(14.2, 16.0, '<h3>Cuba minggu ni</h3>Catat belanja kecil<br>7 hari.<br><span class="n" style="font-size:96px">1</span> kategori je.', '', 'les', 'pop'),
    endc(16.0, T, 'Korang belanja kecil<br>paling kerap apa? 👇'),
    nx(16.5, T, 'Ep 8: nombor yang tak boleh bagi 🔒'),
    note(0, 9.4, True, 'Watak rekaan · Angka contoh · Bahan pendidikan'),
    note(9.4, T),
], [[0, DARK], [9.4, PAPER], [14.2, GREEN], [16.0, GOLD]])

if __name__ == '__main__':
    os.makedirs(os.path.join(BASE, 'html'), exist_ok=True)
    os.makedirs(os.path.join(BASE, 'out'), exist_ok=True)
    for k, h in V5.items():
        open(os.path.join(BASE, 'html', f'{k}.html'), 'w').write(h)
    print(list(V5))
