# Diari Duit Tunas Ep 2–4 (minggu 16 Nov 2026). Hook pada frame 0, POV skrin telefon + diari, 18 s.
# Watak & cerita rekaan. Angka contoh. Bahan pendidikan, bukan nasihat pelaburan.
from engine import *
import os

FONTC = os.path.join(BASE, 'node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2')
X = f"""
@font-face{{font-family:Caveat;font-weight:700;src:url(file://{FONTC})}}
.hook{{left:46px;right:46px;top:200px;background:#1E1712;color:#FFF6E5;border-radius:34px;padding:40px 38px;
  font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;font-size:86px;line-height:1.1;text-align:center;
  box-shadow:0 14px 0 #F5C04A}}
.hook small{{display:block;font-size:50px;color:#F5C04A;margin-top:18px}}
.ep{{left:46px;top:96px;background:#5FA82E;color:#fff;border:4px solid #1E1712;border-radius:999px;padding:8px 26px;font-size:36px;font-weight:900}}
.ph{{left:110px;width:860px;top:700px;height:1000px;background:#0B141A;border:10px solid #1E1712;border-radius:64px;padding:30px 28px;color:#E9EDEF;overflow:hidden}}
.ph .top{{display:flex;align-items:center;gap:20px;background:#1F2C33;margin:-30px -28px 24px;padding:30px 30px 22px;font-size:40px}}
.ph .av{{width:72px;height:72px;border-radius:50%;background:#7C8B95;display:flex;align-items:center;justify-content:center;font-size:44px}}
.ph .top small{{display:block;font-size:28px;color:#8696A0}}
.m{{position:absolute;max-width:640px;padding:20px 26px 30px;border-radius:24px;font-size:44px;line-height:1.25;font-weight:800}}
.m i{{position:absolute;right:18px;bottom:6px;font-style:normal;font-size:24px;color:#8696A0}}
.in{{left:150px;background:#202C33;color:#E9EDEF;border-top-left-radius:4px}}
.out{{right:150px;background:#005C4B;color:#E9EDEF;border-top-right-radius:4px}}
.typ{{left:150px;background:#202C33;color:#8696A0;padding:18px 30px;border-radius:24px;font-size:44px}}
.bank{{left:120px;right:120px;background:#F4F4F6;color:#111;border-radius:30px;padding:22px 28px;font-size:40px;line-height:1.25;box-shadow:0 10px 30px rgba(0,0,0,.45)}}
.bank b{{display:block;font-size:28px;color:#666;letter-spacing:.03em;font-weight:800}}
.diari{{left:70px;right:70px;top:640px;background:#FFFDF3;border:6px solid #1E1712;border-radius:24px;padding:40px 46px 50px 110px;
  background-image:repeating-linear-gradient(180deg,transparent 0 78px,#BFD8EE 78px 81px),linear-gradient(90deg,transparent 80px,#F2A7A0 80px 84px,transparent 84px);
  font-family:Caveat,'Noto Color Emoji',cursive;font-size:76px;line-height:81px;color:#22304A;box-shadow:0 12px 0 #1E1712}}
.diari b{{color:#C8473B}}
.les{{left:70px;right:70px;top:640px;background:#fff;border:7px solid #1E1712;border-radius:40px;padding:44px;box-shadow:0 14px 0 #5FA82E;text-align:center;font-size:56px;line-height:1.25}}
.les h3{{margin:0 0 18px;font-family:Fredoka,sans-serif;font-size:66px;color:#3E7D1F}}
.les .n{{font-family:Fredoka,sans-serif;font-size:120px;color:#1E1712}}
.calc{{left:110px;width:860px;top:730px;background:#111;border:10px solid #1E1712;border-radius:60px;padding:40px 38px;color:#fff}}
.calc .ln{{display:flex;justify-content:space-between;font-size:44px;padding:14px 4px;border-bottom:2px solid #333;color:#ddd}}
.calc .ln b{{color:#fff}}
.calc .tot{{display:flex;justify-content:space-between;font-size:62px;font-weight:900;padding-top:22px;color:#FF8A7A}}
.calc .vs{{display:flex;justify-content:space-between;font-size:52px;font-weight:900;padding-top:16px;color:#7FD86B}}
.q{{left:60px;right:60px;background:#fff;border:6px solid #1E1712;border-radius:28px;padding:26px 30px;font-size:47px;line-height:1.2;box-shadow:0 8px 0 #1E1712}}
.q b{{color:#C8473B}}
.endc{{left:50px;right:50px;top:1260px;text-align:center;font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;font-size:86px;line-height:1.1;color:#1E1712}}
.nx{{left:60px;right:60px;top:1560px;text-align:center;font-size:48px;color:#5E4B37}}
.note{{left:0;right:0;bottom:60px;text-align:center;font-size:30px;color:#5E4B37}}
.note2{{left:20px;right:20px;bottom:60px;text-align:center;font-size:27px;color:#C9D1D6}}
"""

def P(items, bgs): return page(items, bgs).replace('</style>', X + '</style>', 1)
def hook(t1, txt, sub=''): return item(0, t1, txt + (f'<small>{sub}</small>' if sub else ''), '', 'hook', 'none')
def ep(t1, txt): return item(0, t1, txt, '', 'ep', 'none')
def note(t0, t1, dark=False, txt='Watak & cerita rekaan · Bahan pendidikan, bukan nasihat pelaburan'):
    return item(t0, t1, txt, '', 'note2' if dark else 'note', 'none')
def endc(t0, T, txt): return item(t0, T, txt, '', 'endc', 'pop', 'pulse')
def nx(t0, T, txt): return item(t0, T, txt, '', 'nx', 'up')
def phone(t0, t1, who, sub, av='👤'):
    return item(t0, t1, f'<div class="top"><div class="av">{av}</div><div>{who}<small>{sub}</small></div></div>', '', 'ph', 'none')
def msg(t0, t1, txt, y, side='in', tm='21:14'):
    return item(t0, t1, f'{txt}<i>{tm}</i>', f'top:{y}px', f'm {side}', 'up')
def typ(t0, t1, y): return item(t0, t1, '•••', f'top:{y}px', 'typ', 'fade', 'pulse')
def bank(t0, t1, who, txt, y): return item(t0, t1, f'<b>{who}</b>{txt}', f'top:{y}px', 'bank', 'drop')

DARK = 'linear-gradient(180deg,#2A2F36,#14181C)'
PAPER = 'linear-gradient(180deg,#FCEFC7,#FFF6E5)'
GREEN = 'linear-gradient(180deg,#E4F3D6,#FFF6E5)'
RED = 'linear-gradient(180deg,#FBE1DD,#FFF6E5)'
GOLD = 'linear-gradient(180deg,#FFE9A3,#FFF6E5)'

V = {}
T = 18

# ---------- Ep 2: Mak call RM500 (dana kecemasan) ----------
V['diari-duit-tunas-ep2'] = P([
    ep(T, 'Diari Duit Tunas · Ep 2'),
    hook(3.4, 'Mak mesej:<br>"Ada RM500 tak?"', 'Baki akaun saya: RM212 😶'),
    phone(0, 8.6, 'Mak ❤️', 'dalam talian', '👩'),
    item(0, 8.6, 'Along, ada RM500 tak? Kereta abah rosak 🙏<i>21:14</i>', 'top:960px', 'm in', 'none'),
    msg(1.6, 8.6, 'Mak nak hantar bengkel esok pagi', 1150, 'in', '21:14'),
    typ(3.0, 4.6, 1320),
    msg(4.6, 8.6, 'Nanti Along check dulu ya mak…', 1320, 'out', '21:19'),
    bank(5.8, 8.6, 'BANK REKAAN · 21:20', 'Baki semasa: <b style="display:inline;font-size:44px;color:#C8473B">RM212.40</b>', 1500),
    item(8.6, 13.4, 'Bukan tak sayang mak.<br>Saya cuma <b>tak ada<br>simpanan langsung.</b><br>Kecemasan = hutang. 😔', '', 'diari', 'up'),
    item(13.4, 16.2, '<h3>Dana kecemasan</h3>Mula kecil:<br><span class="n">RM50</span><br>setiap hari gaji.<br>Sasaran: 3 bulan belanja.', '', 'les', 'pop'),
    emo(8.9, 13.4, '📓', 760, 1180, 200),
    emo(13.6, 16.2, '🐷', 430, 1360, 220, 'pop', 'bob'),
    endc(16.2, T, 'Korang pernah<br>kena macam ni? 👇'),
    nx(16.6, T, 'Ep 3: kawan ajak "join" 👀'),
    note(0, 8.6, True), note(8.6, T),
], [[0, DARK], [8.6, PAPER], [13.4, GREEN], [16.2, GOLD]])

# ---------- Ep 3: Kawan ajak join 5% seminggu (anti-scam) ----------
V['diari-duit-tunas-ep3'] = P([
    ep(T, 'Diari Duit Tunas · Ep 3'),
    hook(3.4, 'Kawan ajak join.<br>"Untung 5% seminggu."', 'Modal RM1,000 je, katanya 👀'),
    phone(0, 8.8, 'Amir (kawan sekolah)', 'sedang menaip…', '🧢'),
    item(0, 8.8, 'Bro join la. Aku dah dapat RM200 minggu ni 🔥<i>22:03</i>', 'top:960px', 'm in', 'none'),
    msg(1.5, 8.8, 'Untung 5% seminggu. Confirm!', 1150, 'in', '22:03'),
    msg(3.0, 8.8, 'Slot tinggal 3 je. Malam ni tutup ⏳', 1310, 'in', '22:04'),
    typ(4.6, 6.0, 1480),
    msg(6.0, 8.8, 'Hmm… bagi aku fikir jap', 1480, 'out', '22:06'),
    item(8.8, 9.9, 'Sebelum jawab,<br>saya tanya <b>3 soalan:</b>', '', 'diari', 'up'),
    item(9.9, 15.6, '1. Dia <b>berdaftar</b> dengan SC / BNM?', 'top:680px', 'q', 'left'),
    item(11.4, 15.6, '2. Untung <b>tetap & tinggi</b>? 🚩', 'top:880px', 'q', 'left'),
    item(12.9, 15.6, '3. Kena <b>cepat</b> / ajak orang? 🚩', 'top:1080px', 'q', 'left'),
    item(14.2, 15.6, 'Semak senarai amaran SC dulu.', 'left:60px;right:60px;top:1320px;font-size:48px;color:#3E7D1F', 'big', 'up'),
    endc(15.6, T, 'Modul anti-scam<br>PERCUMA 🛡️<br>Link di bio'),
    nx(16.0, T, 'Ep 4: Tunas beli 1 lot saham 📉'),
    note(0, 8.8, True), note(8.8, T),
], [[0, DARK], [8.8, RED], [15.6, GREEN]])

# ---------- Ep 4: Perangkap kos 1 lot (A/B hook) ----------
CALC = ('<div class="ln"><span>1 lot = 100 unit × RM0.50</span><b>RM50.00</b></div>'
        '<div class="ln"><span>Komisen broker (minimum)*</span><b>RM8.00</b></div>'
        '<div class="ln"><span>Fi penjelasan 0.03%</span><b>RM0.02</b></div>'
        '<div class="ln"><span>Duti setem</span><b>RM1.00</b></div>'
        '<div class="tot"><span>Kos beli</span><span>≈ RM9</span></div>'
        '<div class="vs"><span>Dividen setahun (6%)</span><span>RM3</span></div>')

def ep4(hk, sub):
    return P([
        ep(T, 'Diari Duit Tunas · Ep 4'),
        hook(3.4, hk, sub),
        item(0, 9.6, CALC, '', 'calc', 'none'),
        item(6.2, 9.6, 'RM9 ÷ RM3 = <b>3 tahun</b><br>dividen habis bayar kos 😨', 'left:60px;right:60px;top:1560px;font-size:56px;line-height:1.2;color:#FCEFC7', 'big', 'up'),
        item(9.6, 14.0, 'Pelajaran saya:<br>kira kos sebagai<br><b>% modal</b> dulu.<br>RM50 → 18% 😵<br>RM5,000 → 0.3% 🙂', '', 'diari', 'up'),
        emo(9.8, 14.0, '🧮', 720, 1200, 220),
        item(14.0, 16.0, 'Kira sendiri dengan<br>kalkulator kos Hari 1 🌱', 'left:60px;right:60px;top:700px;font-family:Fredoka;font-size:84px;line-height:1.15', 'big', 'pop'),
        endc(15.0, T, 'Cuba 3 hari<br>PERCUMA 🌱<br>Link di bio'),
        nx(16.2, T, 'Ep 5: emas & DUA harga 👀'),
        note(0, 9.6, True, '*Angka contoh, caj sebenar ikut broker · Watak rekaan · Bukan nasihat pelaburan'),
        note(9.6, T),
    ], [[0, DARK], [9.6, PAPER], [14.0, GREEN]])

V['diari-duit-tunas-ep4-a'] = ep4('Saya beli 1 lot.<br>Kos dia makan<br>dividen 3 tahun.', 'Jom kira 👇')
V['diari-duit-tunas-ep4-b'] = ep4('Beli saham RM50.<br>RM9 hilang<br>sebelum mula. 😨', 'Ke mana duit tu pergi? 👇')

if __name__ == '__main__':
    os.makedirs(os.path.join(BASE, 'html'), exist_ok=True)
    os.makedirs(os.path.join(BASE, 'out'), exist_ok=True)
    for k, h in V.items():
        open(os.path.join(BASE, 'html', f'{k}.html'), 'w').write(h)
    print(list(V))
