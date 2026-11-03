# Kempen 11.11 "Diari Duit Tunas" — hook pada frame 0, gaya skrin telefon + diari, 18 s.
from engine import *
import os

FONTC = '/home/claude/promo/node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2'
X = f"""
@font-face{{font-family:Caveat;font-weight:700;src:url(file://{FONTC})}}
.hook{{left:50px;right:50px;top:250px;background:#3B2A1A;color:#FFF6E5;border-radius:36px;padding:44px 40px;
  font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;font-size:84px;line-height:1.12;text-align:center;box-shadow:0 14px 0 #D4574B}}
.hook small{{display:block;font-size:46px;color:#F5C04A;margin-top:18px}}
.ep{{left:50px;top:110px;background:#5FA82E;color:#fff;border:5px solid #3B2A1A;border-radius:999px;padding:10px 28px;font-size:38px;font-weight:900}}
.ph{{left:150px;width:780px;top:560px;height:1040px;background:#1C1C1E;border:10px solid #3B2A1A;border-radius:70px;padding:46px 34px;color:#fff;overflow:hidden}}
.ph .bar{{display:flex;justify-content:space-between;font-size:30px;color:#bbb;margin-bottom:26px}}
.ph h4{{margin:0 0 18px;font-size:44px;color:#F5C04A}}
.row{{display:flex;justify-content:space-between;align-items:center;background:#2C2C2E;border-radius:22px;padding:22px 26px;margin-bottom:16px;font-size:40px}}
.row s{{color:#ff8a7a}}
.tot{{display:flex;justify-content:space-between;font-size:52px;font-weight:900;border-top:3px dashed #666;padding-top:22px;margin-top:10px}}
.diari{{left:70px;right:70px;top:560px;background:#FFFDF3;border:6px solid #3B2A1A;border-radius:24px;padding:40px 46px 50px 110px;
  background-image:repeating-linear-gradient(180deg,transparent 0 78px,#BFD8EE 78px 81px),linear-gradient(90deg,transparent 80px,#F2A7A0 80px 84px,transparent 84px);
  font-family:Caveat,'Noto Color Emoji',cursive;font-size:76px;line-height:81px;color:#22304A;box-shadow:0 12px 0 #3B2A1A}}
.diari b{{color:#C8473B}}
.card{{left:70px;right:70px;top:540px;background:#fff;border:7px solid #3B2A1A;border-radius:40px;padding:40px;box-shadow:0 14px 0 #3B2A1A;text-align:center}}
.card h3{{margin:0 0 14px;font-family:Fredoka,sans-serif;font-size:62px}}
.pr{{display:flex;justify-content:space-between;align-items:center;font-size:52px;padding:14px 6px;border-bottom:3px dashed #E5D7BF}}
.pr s{{color:#9b8b78;font-size:44px;margin-right:16px}} .pr b{{color:#3E9A57;font-size:66px}}
.kod{{margin-top:26px;display:inline-block;background:#F5C04A;border:6px dashed #3B2A1A;border-radius:24px;padding:16px 40px;font-family:Fredoka,sans-serif;font-size:76px;letter-spacing:.06em}}
.sah{{font-size:38px;color:#5E4B37;margin-top:18px}}
.endc{{left:60px;right:60px;top:1300px;text-align:center;font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;font-size:92px;color:#3B2A1A}}
.note{{left:0;right:0;bottom:70px;text-align:center;font-size:30px;color:#5E4B37}}
"""

def P(items, bgs):
    return page(items, bgs).replace('</style>', X + '</style>', 1)

def hook(t1, txt, sub=''):
    return item(0, t1, txt + (f'<small>{sub}</small>' if sub else ''), '', 'hook', 'none')
def ep(t1, txt): return item(0, t1, txt, '', 'ep', 'none')
def note(T): return item(0, T, 'Watak & cerita rekaan · Bahan pendidikan, bukan nasihat pelaburan', '', 'note', 'none')
def endc(t0, T, txt): return item(t0, T, txt, '', 'endc', 'pop', 'pulse')

PAPER = 'linear-gradient(180deg,#FCEFC7,#FFF6E5)'
NIGHT = 'linear-gradient(180deg,#2B3A55,#5A6B8C)'
GOLD = 'linear-gradient(180deg,#FFE9A3,#FFF6E5)'
GREEN = 'linear-gradient(180deg,#E4F3D6,#FFF6E5)'
RED = 'linear-gradient(180deg,#FBE1DD,#FFF6E5)'

HARGA = ('<h3>🌱 Promo 11.11 · Jimat RM11</h3>'
         '<div class="pr"><span>1 modul</span><span><s>RM50</s><b>RM39</b></span></div>'
         '<div class="pr"><span>Pakej 3in1</span><span><s>RM100</s><b>RM89</b></span></div>'
         '<div class="kod">GENG11</div><div class="sah">Sah hingga 12 Nov, 11:59 malam</div>')

V = {}
T = 18

# P1 — teaser (8 Nov)
V['p1-1111-tahun-lepas'] = P([
    ep(T, 'Diari Duit Tunas · 11.11'),
    hook(5.5, '11.11 tahun lepas:<br>RM347 habis.', 'Yang masih guna: 1 je 😅'),
    item(2.2, 9.5, '<div class="bar"><span>21:47</span><span>🛒 Troli saya</span></div><h4>Pesanan 11.11 (2025)</h4>'
         '<div class="row"><span>Lampu LED kucing</span><s>RM39</s></div>'
         '<div class="row"><span>Kasut "flash sale"</span><s>RM129</s></div>'
         '<div class="row"><span>Gajet dapur viral</span><s>RM89</s></div>'
         '<div class="row"><span>Earphone ke-3</span><s>RM90</s></div>'
         '<div class="tot"><span>Jumlah</span><span class="n"></span></div>', 'top:650px', 'ph', 'up', '', '0|347|2.5|RM'),
    item(9.5, 14.5, 'Tahun ni saya nak beli<br><b>satu benda je.</b><br>Yang naikkan nilai<br>diri sendiri. ✍️', '', 'diari', 'up'),
    ch(10.2, 14.5, 'T_idea', 600, 1240, 520, 'pop', 'bob'),
    item(14.5, T, 'Apa dia?<br>10 Nov saya reveal 👀', 'left:60px;right:60px;top:620px;font-family:Fredoka;font-size:110px;line-height:1.1', 'big', 'pop', 'pulse'),
    endc(15.4, T, 'Follow supaya<br>tak terlepas 🌱'),
    note(T),
], [[0, PAPER], [2.2, NIGHT], [9.5, PAPER], [14.5, GOLD]])

# P2 — pendedahan (10 Nov)
V['p2-1111-belian-berbaloi'] = P([
    ep(T, 'Diari Duit Tunas · 11.11'),
    hook(4.5, 'RM11 je beza.', 'Tapi ni belian 11.11 paling berbaloi Tunas 👀'),
    item(2.5, 9, 'Kasut flash sale:<br><b>rosak lepas 3 bulan.</b><br><br>Faham urus duit:<br>kekal dengan saya. 🌱', 'top:660px', 'diari', 'up'),
    ch(3.2, 9, 'T_thumb', 640, 1330, 480, 'pop', 'wig'),
    item(9, 15.5, HARGA, '', 'card', 'pop'),
    item(11.5, 15.5, 'Taip kod masa bayar ☝️', 'left:0;right:0;top:1420px;font-size:58px', 'big', 'up'),
    item(15.5, T, 'Belum pasti? Cuba<br>Hari 1–3 PERCUMA dulu.', 'left:60px;right:60px;top:560px;font-family:Fredoka;font-size:88px;line-height:1.15', 'big', 'pop'),
    endc(15.9, T, 'Link di bio 👆'),
    note(T),
], [[0, PAPER], [2.5, PAPER], [9, GOLD], [15.5, GREEN]])

# P3 — hari 11.11
V['p3-1111-checkout-ilmu'] = P([
    ep(T, 'Diari Duit Tunas · Hari 11.11'),
    hook(4.5, 'Hari ni 11.11.', 'Tunas tak checkout troli. Dia checkout ni 👇'),
    item(2.4, 8.5, '<div class="bar"><span>11:11</span><span>🔔</span></div><h4>Notifikasi</h4>'
         '<div class="row" style="background:#1F3A27"><span>✅ Modul "Mula Kecil di Bursa"</span></div>'
         '<div class="row"><span>Harga</span><span><s style="color:#999">RM50</s> RM39</span></div>'
         '<div class="row"><span>Kod</span><span>GENG11</span></div>', 'top:650px', 'ph', 'up'),
    item(8.5, 13.5, 'Hari 1 belajar:<br>rupanya 1 lot =<br><b>100 unit</b> saham.<br>Saya ingat 1 unit 😅', '', 'diari', 'up'),
    ch(9.2, 13.5, 'T_shock', 620, 1320, 480, 'pop', 'shake'),
    item(13.5, T, HARGA, '', 'card', 'pop'),
    endc(14.6, T, 'Link di bio 👆'),
    note(T),
], [[0, GOLD], [2.4, NIGHT], [8.5, PAPER], [13.5, GOLD]])

# P4 — panggilan akhir (12 Nov)
V['p4-1111-hari-akhir'] = P([
    ep(T, 'Diari Duit Tunas · 11.11'),
    hook(4.5, 'Esok harga<br>balik RM50.', 'Sekadar ingatkan, bukan desak 🙏'),
    item(2.6, 9, 'Kalau belum sedia,<br>tak apa.<br><b>Hari 1–3 tetap percuma</b><br>bila-bila masa. 🌱', 'top:660px', 'diari', 'up'),
    ch(3.4, 9, 'K_tunggu', 640, 1330, 480, 'pop', 'bob'),
    item(9, 15.5, HARGA, '', 'card', 'pop'),
    item(11.4, 15.5, 'Tamat malam ni, 11:59 ⏳', 'left:0;right:0;top:1420px;font-size:58px;color:#C8473B', 'big', 'up'),
    item(15.5, T, 'Kalau dah sedia:', 'left:60px;right:60px;top:600px;font-family:Fredoka;font-size:96px', 'big', 'pop'),
    endc(15.9, T, 'Link di bio 👆'),
    note(T),
], [[0, RED], [2.6, PAPER], [9, GOLD], [15.5, GREEN]])

if __name__ == '__main__':
    os.makedirs('/home/claude/sosmed/html', exist_ok=True)
    for k, h in V.items():
        open(f'/home/claude/sosmed/html/{k}.html', 'w').write(h)
    print(list(V))
