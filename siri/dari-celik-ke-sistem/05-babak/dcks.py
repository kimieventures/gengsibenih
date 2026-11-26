# Pustaka siri "Dari Celik ke Sistem" (gaya watak emoji). Satu episod = satu spesifikasi data (lihat ep02/ep02.py).
# Jalankan episod: python3 epXX.py  -> suara (jika belum ada), HTML babak, audio + SFX, render MP4 ke 06-render/.
import os, sys, json, re, shutil, subprocess
LIB = os.path.dirname(os.path.abspath(__file__))
SIRI = os.path.abspath(os.path.join(LIB, '..'))
ALAT = os.path.abspath(os.path.join(SIRI, '../../alat'))
sys.path.insert(0, ALAT)
from tbblib import *  # noqa

LATAR = {'mamak': ('#3a2412', '🍵 🫓 🍳', 'Mamak, malam'), 'rumah': ('#2a2018', '🍽️ 🏠', 'Rumah, malam'),
         'pejabat': ('#16263a', '💻 ☕ 🗂️', 'Pejabat'), 'kereta': ('#1d2430', '🚗 🚦', 'Dalam kereta, jem'),
         'pasar': ('#2f2410', '🛒 🥭 🐟', 'Pasar malam'), 'data': ('#10233a', '📊 💡', ''), 'kosong': ('#1a1f1d', '', '')}
SFXSRC = {'pop': "aevalsrc='0.6*sin(2*PI*(500+900*t)*t)*exp(-18*t)':d=0.25",
          'boing': "aevalsrc='0.6*sin(2*PI*(180+260*sin(2*PI*7*t))*t)*exp(-4*t)':d=0.7",
          'whoosh': "anoisesrc=d=0.5:c=pink:a=0.5,bandpass=f=1200:w=900,afade=t=in:d=0.2,afade=t=out:st=0.25:d=0.25",
          'krik': "aevalsrc='0.25*sin(2*PI*4200*t)*(gt(sin(2*PI*14*t),0.6))*lt(mod(t,0.6),0.25)':d=1.3",
          'ding': "aevalsrc='0.5*sin(2*PI*1320*t)*exp(-5*t)+0.3*sin(2*PI*1980*t)*exp(-6*t)':d=0.8"}

def em(s):  # *kata* -> sorotan kuning
    return re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)

def chart_keluar(tag):
    svg = ('<svg width="900" height="600" viewBox="0 0 900 600"><path data-draw="1.2" d="M20 330 C250 300 450 270 880 240" fill="none" stroke="#4da3ff" stroke-width="10"/>'
           '<path data-draw="2.4" data-dl="0.3" d="M20 160 L120 130 L220 150 L300 110 L380 170 L440 230 L470 300 L540 360 L620 420 L700 400 L780 480 L860 520" fill="none" stroke="#ff5a4e" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
           '<text x="560" y="225" fill="#4da3ff" font-size="34" font-family="Nunito">purata 200 hari</text>'
           '<circle cx="470" cy="300" r="22" fill="#f5c542"/><text x="380" y="380" fill="#f5c542" font-size="36" font-family="Nunito">🚪 KELUAR</text></svg>')
    return f'<div class="tag">{tag}</div>{svg}'

def chart_kos(tag):
    bars = ''.join(f'<div style="display:flex;align-items:center;gap:20px;font-size:44px;margin:14px 0"><span style="width:300px;text-align:left">{a}</span>'
                   f'<span style="height:60px;width:{wd}px;background:{c};border-radius:10px"></span><b>{v}</b></div>'
                   for a, wd, c, v in [('Untung kasar', 420, '#3fbf74', '+RM420'), ('Kos & yuran', 470, '#ff5a4e', '−RM470'), ('Bersih', 50, '#f5c542', '−RM50')])
    return f'<div class="tag">{tag}</div>{bars}'

def pie(a, la, lb, tag):
    return (f'<div class="tag">{tag}</div><div style="display:flex;gap:50px;align-items:center"><div style="width:360px;height:360px;border-radius:50%;'
            f'background:conic-gradient(#f5c542 0 {a*3.6}deg,#2f7fd6 {a*3.6}deg 360deg);flex:none"></div>'
            f'<div style="font-size:50px;line-height:1.4;text-align:left"><b style="color:#f5c542">{a}%</b> {la}<br><b style="color:#4da3ff">{100-a}%</b> {lb}</div></div>')

def stat(l1, n, l2, tag=''):
    return f'<div class="tag">{tag}</div><div class="stat"><div class="sl">{l1}</div><div class="n">{n}</div><div class="sl">{l2}</div></div>'

CSS2 = """
body{background:#0f1412!important}
.jd{text-align:center;font-family:Fredoka,sans-serif;font-size:84px;line-height:1.12;color:#fff;text-shadow:0 6px 24px rgba(0,0,0,.8),0 3px 0 #000}
.jd em,.tg em,.kadg em{font-style:normal;color:#f5c542} .jd small{font-size:52px}
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
.ew{position:absolute;text-align:center;width:380px}
.em{line-height:1;filter:drop-shadow(0 20px 30px rgba(0,0,0,.6))}
.rx{text-align:center;filter:drop-shadow(0 10px 20px rgba(0,0,0,.6))}
.emj{transform-origin:50% 55%}
.nm{display:inline-block;margin-top:14px;color:#fff;font-size:30px;letter-spacing:.12em;border-radius:999px;padding:6px 22px}
"""
JSM = r"""
const EW=[...document.querySelectorAll('.ew')],SC=[...document.querySelectorAll('.emj')];
const R2=window.render;window.render=t=>{R2(t);const c=SUB.find(c=>t>=c.t0&&t<c.t1);
 for(const el of EW){const talk=c&&c.who===el.dataset.who;el.style.transform=talk?`translateY(${-Math.abs(Math.sin(t*13))*22}px) rotate(${Math.sin(t*6)*4}deg) scale(1.05)`:`translateY(${Math.sin(t*2)*6}px) scale(.93)`;el.style.opacity=talk||!c?1:.82}
 let k=0;for(const p of PUNCH){if(t>=p&&t<p+0.9)k=Math.max(k,Math.exp(-(t-p)*5))}
 for(const s of SC){s.style.transform=k?`scale(${1+0.08*k}) translateX(${Math.sin(t*60)*12*k}px)`:''}};
"""

def babak(t0, t1, tempat, n, d, prop=''):
    bg, deco, nama = LATAR[tempat]
    h = f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 45%,{bg},#0b0f0d 75%)"></div>'
    if deco: h += f'<div style="position:absolute;left:0;right:0;top:1150px;text-align:center;font-size:70px;opacity:.35;letter-spacing:40px">{deco}</div>'
    if nama: h += f'<div style="position:absolute;left:0;right:0;top:1245px;text-align:center;font-size:28px;letter-spacing:.2em;color:#ffffff88">{nama.upper()}</div>'
    if n: h += f'<div class="ew" data-who="T" style="left:{120 if d else 350}px;top:640px"><div class="em" style="font-size:{400 if d else 500}px">{n}</div><div class="nm" style="background:#c8642a">NALURI</div></div>'
    if d: h += f'<div class="ew" data-who="K" style="left:{580 if n else 350}px;top:660px"><div class="em" style="font-size:{360 if n else 460}px">{d}</div><div class="nm" style="background:#2f7fd6">DATA</div></div>'
    if prop: h += f'<div style="position:absolute;left:0;right:0;top:540px;text-align:center;font-size:150px">{prop}</div>'
    return item(t0, t1, h, 'inset:0', 'emj', 'none')

def buat(EP):
    """EP: dict(nama, bab, rate, jeda{}, baris=[(who 'N'|'D', teks, babak{})], soalan_komen, seterusnya)."""
    nama = EP['nama']; here = os.path.join(LIB, nama); aud = os.path.join(SIRI, '04-audio', nama)
    os.makedirs(here, exist_ok=True); os.makedirs(aud, exist_ok=True); os.chdir(aud)
    js = {'rate': EP.get('rate', '+28%'), 'lines': [[{'N': 'T', 'D': 'K'}[w], t] for w, t, _ in EP['baris']]}
    old = json.load(open(nama + '.json')) if os.path.exists(nama + '.json') else None
    if old != js or not os.path.exists(nama + '.tts.json'):
        json.dump(js, open(nama + '.json', 'w'), ensure_ascii=False)
        shutil.rmtree('a', ignore_errors=True)
        subprocess.run(['python3', os.path.join(ALAT, 'tts.py'), nama + '.json'], check=True, env={**os.environ, 'SSL_CERT_FILE': '/root/.ccr/ca-bundle.crt'}, stdout=subprocess.DEVNULL)
    e = Ep(nama); GAP, JEDA = 0.12, EP.get('jeda', {})
    t, e.S = 0.35, []
    for i, r in enumerate(e.D):
        t += JEDA.get(i, 0) if i else 0; e.S.append(t); t += r['words'][-1][1] + GAP
    e.END = e.S[-1] + e.D[-1]['dur']; e.T = round(e.END + 3.8, 2); e.E = e.S[1:] + [e.END + 0.2]
    S, E, w, T = e.S, e.E, e.w, e.T
    W = lambda i, k: w(i, k) if k else S[i]
    it, SFX, PUNCH = [item(0, T, '', 'inset:0;background:#0f1412', '', 'none')], [], []
    n = len(EP['baris'])
    # segmen latar: baris dengan 'b' mula babak baharu sehingga baris seterusnya yang ada 'b'/'kad'/'q'/'a'
    mula = [i for i, (_, _, b) in enumerate(EP['baris']) if any(k in b for k in ('b', 'kad', 'q', 'a'))]
    for j, i in enumerate(mula):
        b = EP['baris'][i][2]; akhir = E[(mula[j + 1] - 1) if j + 1 < len(mula) else n - 1]
        if 'b' in b:
            tm, nn, dd = b['b']; it.append(babak(S[i], akhir, tm, nn, dd, b.get('prop', '')))
    for i, (who, teks, b) in enumerate(EP['baris']):
        if 'j' in b:
            it.append(item(W(i, b.get('jw')), E[i] + b.get('jl', 0), em(b['j']), f'left:70px;right:70px;top:{b.get("jt", 240)}px', 'jd', 'pop', b.get('jlp', '')))
        if 'tg' in b:
            t0 = W(i, b.get('tgw')) if b.get('tgw') != 'akhir' else E[i] - 1.4
            it.append(item(t0, E[i] + b.get('tgl', 0.3), em(b['tg']), 'left:90px;right:90px;top:1170px', 'tg', 'pop', 'pulse'))
        if 'kad' in b:
            it.append(item(S[i], E[i] + b.get('kl', 0), b['kad'], 'left:80px;right:80px;top:360px', 'kadg', 'pop', bx=b.get('bx', '')))
        if 'q' in b:
            it.append(item(S[i], E[i], f'<div class="tag">SOALAN</div><div style="font-size:72px;line-height:1.2">❓ {em(b["q"])}</div>', 'left:70px;right:70px;top:420px', 'kadg', 'drop'))
        if 'a' in b:
            it.append(item(S[i], E[i], '<div class="tag">JAWAPAN · SIMPAN KAD NI 📌</div>', 'left:70px;right:70px;top:330px', 'kadg', 'pop'))
            for k, (pt, kw) in enumerate(b['a']):
                it.append(item(W(i, kw), E[i], f'<b style="color:#f5c542">{k+1}</b> {pt}', f'left:90px;right:90px;top:{480 + k*190}px', 'pt', 'left'))
            SFX.append((round(S[i], 2), 'ding'))
        for r in b.get('rx', []):  # (kata, emoji, x, y, saiz, bunyi[, anjakan])
            kw, emo, x, y, sz, bunyi = r[:6]; t0 = W(i, kw) + (r[6] if len(r) > 6 else 0)
            it.append(item(t0, t0 + 1.5, emo, f'left:{x}px;top:{y}px;font-size:{sz}px', 'rx', 'pop', 'wig')); SFX.append((round(t0, 2), bunyi))
        if 'punch' in b: PUNCH.append(W(i, b['punch']))
    END = e.END + 0.2
    it += [item(END, T, '', 'inset:0;background:#0f1412', '', 'fade'),
           item(END + 0.1, T, em('Naluri + Data<br>= *Sistem*'), 'left:70px;right:70px;top:330px', 'jd', 'pop'),
           item(END + 0.7, T, em(EP.get('soalan_komen', 'Korang <b>team Naluri</b> ke <b>team Data</b>? Komen 👇')), 'left:90px;right:90px;top:640px', 'tg', 'pop', 'pulse'),
           item(END + 1.3, T, em('Episod depan: ' + EP['seterusnya']), 'left:90px;right:90px;top:900px;font-size:46px', 'tg', 'up'),
           item(END + 1.8, T, 'Modul percuma · link di bio 🌱', 'left:200px;right:200px;top:1120px', 'chip', 'pop'),
           item(0, END, f'DARI CELIK KE SISTEM · BAB {EP["bab"]}', 'left:0;right:0;top:80px;text-align:center', 'badge', 'none'),
           item(0, T, 'Ilustrasi · suara AI · bahan pendidikan, bukan nasihat pelaburan', 'left:0;right:0;bottom:46px;text-align:center', 'lbl2', 'none')]
    SFX.append((round(END + 0.1, 2), 'ding'))
    e.write(it, CSS2, 'const PUNCH=' + json.dumps([round(x, 2) for x in PUNCH]) + ';' + JSM)
    html = open(nama + '.html').read().replace("NAMA={T:['TUNAS','#5FA82E'],K:['KUNTUM','#D4574B']}", "NAMA={T:['NALURI','#c8642a'],K:['DATA 🤖','#2f7fd6']}")
    open(os.path.join(here, nama + '.html'), 'w').write(html); os.remove(nama + '.html')
    inp, flt = ['-i', nama + '_audio.m4a'], []
    for k, (t0, bn) in enumerate(SFX):
        f = os.path.join(LIB, 'sfx_' + bn + '.wav')
        if not os.path.exists(f):
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', SFXSRC[bn], '-ar', '44100', '-ac', '2', f], check=True)
        inp += ['-i', f]; flt.append(f'[{k+1}:a]adelay={int(t0*1000)}|{int(t0*1000)},volume=0.7[s{k}]')
    flt.append('[0:a]' + ''.join(f'[s{k}]' for k in range(len(SFX))) + f'amix=inputs={len(SFX)+1}:normalize=0,alimiter=limit=0.95[o]')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inp, '-filter_complex', ';'.join(flt), '-map', '[o]', '-c:a', 'aac', '-b:a', '160k', os.path.join(here, nama + '_audio.m4a')], check=True)
    os.remove(nama + '_audio.m4a')
    if '--still' in sys.argv:
        ts = [str(round(x, 1)) for x in sys.argv[sys.argv.index('--still') + 1:]] or [str(round(S[i] + 1, 1)) for i in range(0, n, max(1, n // 8))]
        os.makedirs(os.path.join(here, 'out'), exist_ok=True); os.chdir(here)
        subprocess.run(['node', os.path.join(ALAT, 'still.js'), os.path.join(here, nama + '.html'), *ts], check=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', *sum([['-i', f'out/st_{nama}_{x}.jpg'] for x in ts], []), '-filter_complex', f'hstack={len(ts)},scale={300*len(ts)}:-1', 'out/sheet.jpg'], check=True)
        print('sheet', os.path.join(here, 'out/sheet.jpg'))
    if '--render' in sys.argv:
        os.makedirs(os.path.join(here, 'out'), exist_ok=True)
        v = os.path.join(here, 'out', nama + '_v.mp4')
        subprocess.run(['node', os.path.join(ALAT, 'render.js'), os.path.join(here, nama + '.html'), v, str(T)], check=True, stdout=subprocess.DEVNULL)
        dst = os.path.join(SIRI, '06-render', f'dcks-{nama}-{EP["slug"]}.mp4')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', v, '-i', os.path.join(here, nama + '_audio.m4a'), '-map', '0:v', '-map', '1:a', '-c', 'copy', '-shortest', dst], check=True)
        print('video', dst)
    print('T =', T)
