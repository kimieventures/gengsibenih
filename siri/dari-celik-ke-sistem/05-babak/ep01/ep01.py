# EP01 Naluri vs Data: "Terlepas Bas". Jalankan: python3 ep01.py  (hasil: ep01.html + ep01_audio.m4a dalam folder ini)
# Gambar dibaca dari 03-gambar/ep01/img-a..d.* ; jika tiada, kotak placeholder dipaparkan (animatic).
import os, sys, glob, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
SIRI = os.path.abspath(os.path.join(HERE, '../..'))
sys.path.insert(0, os.path.abspath(os.path.join(SIRI, '../../alat')))
from tbblib import *

GAMBAR = os.path.join(SIRI, '03-gambar/ep01')
AUDIO = os.path.join(SIRI, '04-audio/ep01')
os.chdir(AUDIO)
e = Ep('ep01', {3: 0.2, 5: 0.3, 7: 0.4, 11: 0.2, 14: 0.5, 16: 0.4}); S, E, w, T = e.S, e.E, e.w, e.T

NAMA_IMG = {'A': ('img-a', 'Naluri di mamak, teruja'), 'B': ('img-b', 'Robot Data + tablet'),
            'C': ('img-c', 'Naluri + Data, meja dapur'), 'D': ('img-d', 'Naluri tersengih malu')}

def foto(k, t0, t1, zin=True, focus='50% 35%'):
    """Gambar penuh skrin dengan gerakan kamera perlahan (Ken Burns)."""
    f = sorted(glob.glob(os.path.join(GAMBAR, NAMA_IMG[k][0] + '*')))
    f = [x for x in f if x.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    if f:
        inner = f'<img src="file://{f[0]}" style="width:100%;height:100%;object-fit:cover;object-position:{focus}">'
    else:
        tone = {'A': '#6b3a1e,#24140b', 'B': '#1c4a78,#0b1626', 'C': '#6b3a1e 0 50%,#1c4a78 50%', 'D': '#6b3a1e,#24140b'}[k]
        grad = f'linear-gradient(90deg,{tone})' if k == 'C' else f'linear-gradient(160deg,{tone})'
        inner = (f'<div style="width:100%;height:100%;background:{grad};display:flex;align-items:center;justify-content:center;'
                 f'flex-direction:column;color:#fff;font-size:54px;text-align:center;gap:20px"><b style="font-size:120px">IMG-{k}</b>{NAMA_IMG[k][1]}</div>')
    return item(t0, t1, inner, f'inset:0;overflow:hidden', 'kb ' + ('zin' if zin else 'zout'), 'none')

def judul(t0, t1, html, top=210, en='pop', lp=''):
    return item(t0, t1, html, f'left:70px;right:70px;top:{top}px', 'jd', en, lp)

def hl(s): return f'<em>{s}</em>'

it = [item(0, T, '', 'inset:0;background:#0f1412', '', 'none')]
# 0 HOOK: Naluri ke kamera
it += [foto('A', 0, E[1]),
       judul(0.15, E[0], f'RM1,000 boleh jadi<br>{hl("RM1,330")}', 230, 'pop'),
       judul(w(0, 'terlepas'), E[1], f'Aku {hl("TERLEPAS")}…', 560, 'pop', 'shake')]
# 1 Data masuk
it += [item(S[1], E[1], f'<img src="" style="display:none">🤖', 'right:60px;top:880px;font-size:260px', '', 'right', 'bob'),
       item(S[1] + 0.6, E[1] + 2.0, 'Siapa betul?<br><b>Tengok sampai habis.</b>', 'left:90px;right:90px;top:760px', 'tg', 'pop')]
# 2 +33%
it += [foto('A', S[2], E[2], False, '50% 30%'),
       judul(S[2], E[2], f'{hl("+33%")}<br><small>dalam 10 hari</small>', 260, 'pop', 'pulse'),
       judul(w(2, 'dah'), E[2], '"Aku dah cakap kan!"', 640, 'up')]
# 3 Data perli: 47 vs 3
it += [foto('B', S[3], E[3]),
       item(S[3], E[3], '<div class="stat"><div class="sl">"Aku dah cakap kan"</div><div class="n">0</div><div class="sl">kali bulan ni</div></div>',
            'left:110px;right:110px;top:260px', 'kadg', 'pop', bx='0|47|1.4|'),
       item(w(3, 'betul'), E[3], '<div class="stat"><div class="sl">Yang betul</div><div class="n" style="color:#f5c542">3</div></div>',
            'left:300px;right:300px;top:760px', 'kadg', 'pop', 'pulse')]
# 4 kenapa suruh tunggu
it += [foto('C', S[4], E[4]), judul(S[4], E[4], f'Kenapa suruh {hl("TUNGGU")}?', 260)]
# 5 carta pisau jatuh
chart = ('<svg width="900" height="620" viewBox="0 0 900 620"><path data-draw="1.2" d="M20 300 C200 290 400 270 600 250 S800 230 880 225" fill="none" stroke="#4da3ff" stroke-width="10" stroke-dasharray="1"/>'
         '<path data-draw="2.2" data-dl="0.4" d="M20 180 L150 150 L260 170 L330 130 L420 160 L470 330 L540 420 L600 380 L660 470 L740 520" fill="none" stroke="#ff5a4e" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
         '<text x="610" y="215" fill="#4da3ff" font-size="34" font-family="Nunito">purata 200 hari</text><text x="300" y="110" fill="#ff5a4e" font-size="34" font-family="Nunito">harga</text></svg>')
it += [item(S[5], E[5], '<div class="tag">BERITA SKANDAL · ILUSTRASI</div>' + chart, 'left:90px;top:330px', 'kadg', 'pop'),
       item(w(5, 'pisau'), E[5], '🔪 Jangan tangkap pisau jatuh', 'left:90px;right:90px;top:1110px', 'tg', 'pop', 'shake')]
# 6 pisau dapur + durian, hook semula
it += [foto('A', S[6], E[6], False, '50% 40%'),
       judul(S[6], w(6, 'macam'), f'Pisau? Aku nak beli saham,<br>bukan {hl("pisau dapur")}!', 260, 'pop'),
       judul(w(6, 'macam'), E[6], f'Macam tak jadi beli {hl("durian")} masa murah…', 260, 'pop', 'wig'),
       item(E[6] - 1.2, E[6] + 0.4, 'Tapi tunggu. Robot ni ada rahsia…', 'left:90px;right:90px;top:900px', 'tg', 'pop', 'pulse')]
# 7 jatuh terus jatuh
it += [foto('B', S[7], E[7]), judul(S[7], E[7], f'Beli masa jatuh…<br>{hl("terus jatuh")} ↓↓↓', 260, 'pop')]
# 8 malu
it += [foto('D', S[8], E[8]), judul(w(8, 'tak'), E[8], '"Tak payah ungkit." 😅', 300, 'pop', 'wig')]
# 9-10 tiket
it += [foto('C', S[9], E[10]),
       item(w(9, 'tiket'), E[10], '🎟️', 'left:400px;top:700px;font-size:260px', '', 'pop', 'wig'),
       judul(S[10], E[10], f'{hl("Tiket konsert?")} 🎤', 280, 'pop', 'shake')]
# 11 pai 95/5
pie = ('<div style="display:flex;gap:50px;align-items:center"><div style="width:380px;height:380px;border-radius:50%;'
       'background:conic-gradient(#f5c542 0 18deg,#2f7fd6 18deg 360deg);flex:none"></div>'
       '<div style="font-size:52px;line-height:1.4;text-align:left"><b style="color:#f5c542">5%</b> tiket keyakinan<br><b style="color:#4da3ff">95%</b> ikut peraturan</div></div>')
it += [item(S[11], E[11], '<div class="tag">TIKET KEYAKINAN · CONTOH SAHAJA</div>' + pie, 'left:80px;right:80px;top:420px', 'kadg', 'pop'),
       item(w(11, 'salah'), E[11], 'Betul → untung · Salah → rugi sikit', 'left:90px;right:90px;top:1000px', 'tg', 'up')]
# 12-13 idea vs had
it += [foto('C', S[12], E[13], False),
       judul(S[13], E[13], f'Naluri bagi {hl("idea")}.<br>Data bagi {hl("had")}.', 250, 'pop'),
       item(w(13, 'tipu'), E[13], '🤖 Data tak tipu.', 'left:250px;right:250px;top:640px', 'tg', 'pop', 'pulse')]
# 14 SOALAN
it += [item(S[14], E[14], '<div class="tag">SOALAN</div><div style="font-size:72px;line-height:1.2">❓ Kalau naluri dah betul,<br>kenapa masih perlu peraturan?</div>',
            'left:70px;right:70px;top:420px', 'kadg', 'drop')]
# 15 JAWAPAN 3 poin
pts = ['Betul sekali ≠ betul selalu', 'Peraturan jaga modal', 'Tiket bagi ruang pada naluri']
it += [item(S[15], E[15], '<div class="tag">JAWAPAN · SIMPAN KAD NI 📌</div>', 'left:70px;right:70px;top:330px', 'kadg', 'pop')]
for k, p in enumerate(pts):
    t0 = [S[15], w(15, 'peraturan'), w(15, 'tiket')][k]
    it.append(item(t0, E[15], f'<b style="color:#f5c542">{k+1}</b> {p}', f'left:90px;right:90px;top:{480 + k*190}px', 'pt', 'left'))
# 16-17 gelung + penutup
it += [foto('D', S[16], E[17] + 0.2, False),
       judul(S[16], E[16], f'Tapi kalau {hl("durian")} turun harga lagi?', 280, 'pop'),
       judul(S[17], E[17] + 0.2, '"Saya tak buat ramalan durian." 🤖', 280, 'pop')]
END = e.END + 0.2
it += [item(END, T, '', 'inset:0;background:#0f1412', '', 'fade'),
       judul(END + 0.1, T, f'Naluri + Data<br>= {hl("Sistem")}', 330, 'pop'),
       item(END + 0.7, T, 'Korang <b>team Naluri</b> ke <b>team Data</b>? Komen 👇', 'left:90px;right:90px;top:760px', 'tg', 'pop', 'pulse'),
       item(END + 1.3, T, 'Episod depan: robot ni tahu bila nak <em>KELUAR</em>?', 'left:90px;right:90px;top:1000px;font-size:46px', 'tg', 'up'),
       item(END + 1.8, T, 'Modul percuma · link di bio 🌱', 'left:200px;right:200px;top:1180px', 'chip', 'pop')]
# lencana siri + label tetap
it += [item(0, END, 'DARI CELIK KE SISTEM · BAB 5/6', 'left:0;right:0;top:80px;text-align:center', 'badge', 'none'),
       item(0, T, 'Ilustrasi · suara AI · bahan pendidikan, bukan nasihat pelaburan', 'left:0;right:0;bottom:46px;text-align:center', 'lbl2', 'none')]

CSS2 = """
body{background:#0f1412!important}
.jd{text-align:center;font-family:Fredoka,sans-serif;font-size:84px;line-height:1.12;color:#fff;text-shadow:0 6px 24px rgba(0,0,0,.8),0 3px 0 #000}
.jd em,.tg em{font-style:normal;color:#f5c542} .jd small{font-size:52px}
.tg{text-align:center;background:rgba(10,14,12,.82);color:#fff;border:3px solid #f5c542;border-radius:28px;padding:22px 30px;font-size:54px;line-height:1.25}
.tg b{color:#f5c542}
.kadg{background:rgba(16,22,20,.94);color:#fff;border:3px solid #2f7fd6;border-radius:32px;padding:34px 40px;text-align:center}
.tag{font-size:30px;letter-spacing:.12em;color:#9fb2ab;margin-bottom:18px}
.stat .n{font-family:Fredoka,sans-serif;font-size:220px;line-height:1;color:#ff8a4c} .stat .sl{font-size:46px}
.pt{background:rgba(16,22,20,.94);color:#fff;border-left:12px solid #f5c542;border-radius:20px;padding:30px 34px;font-size:60px}
.badge{font-family:Nunito;font-size:30px;letter-spacing:.14em;color:#fff;text-shadow:0 2px 8px #000}
.lbl2{font-size:26px;color:#cfd8d4;text-shadow:0 2px 6px #000}
.chip{background:#2f7fd6!important}
.sub{top:1430px!important;color:#fff!important;text-shadow:0 4px 14px #000,0 2px 0 #000!important}
.sub span.on{background:#f5c542!important;color:#111!important}
.who{top:1350px!important}
.kb{overflow:hidden}
"""
JS2 = r"""
const KB=[...document.querySelectorAll('.kb')];const R1=window.render;window.render=t=>{R1(t);for(const k of KB){const t0=+k.dataset.t0,t1=+k.dataset.t1;
 const p=Math.min(1,Math.max(0,(t-t0)/Math.max(1,t1-t0)));const s=k.classList.contains('zin')?1+0.10*p:1.10-0.10*p;const im=k.firstElementChild;if(im)im.style.transform=`scale(${s})`;}};
"""
e.write(it, CSS2, JS2)
html = open('ep01.html').read().replace("NAMA={T:['TUNAS','#5FA82E'],K:['KUNTUM','#D4574B']}", "NAMA={T:['NALURI','#c8642a'],K:['DATA 🤖','#2f7fd6']}")
open(os.path.join(HERE, 'ep01.html'), 'w').write(html); os.remove('ep01.html')
shutil.move('ep01_audio.m4a', os.path.join(HERE, 'ep01_audio.m4a'))
print('siap', os.path.join(HERE, 'ep01.html'), 'T =', T)
