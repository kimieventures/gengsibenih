# Perpustakaan siri bersuara (Tunas Baca Buku, Fail Duit Tunas): audio + subtitle perkataan demi perkataan + penutup.
# Guna dari folder episod: sys.path.insert(0, '<repo>/alat'); from tbblib import *
import json, subprocess, sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import *
FONTC = os.path.join(FONT, 'caveat/files/caveat-latin-700-normal.woff2')
MUZIK = os.environ.get('GSB_MUZIK', os.path.join(BASE, 'out/muzik-ceria.wav'))
X = f"""
@font-face{{font-family:Caveat;font-weight:700;src:url(file://{FONTC})}}
body{{background:#FFF8E8}}
.paper{{position:absolute;inset:0;background:#FFF8E8;background-image:repeating-linear-gradient(180deg,transparent 0 86px,#D9E6F2 86px 89px),linear-gradient(90deg,transparent 96px,#F2B8B0 96px 100px,transparent 100px)}}
.epc{{left:120px;top:70px;font-size:34px;background:#3B2A1A;color:#FFF6E5;border-radius:999px;padding:10px 26px;transform:rotate(-1.5deg)}}
.tape{{left:110px;right:90px;top:150px;text-align:center;background:#F5C04A;font-family:Fredoka,sans-serif;font-size:82px;padding:18px 20px 22px;transform:rotate(-2.2deg);
  clip-path:polygon(0 6%,3% 0,97% 4%,100% 0,99% 94%,96% 100%,2% 96%,0 100%);box-shadow:0 6px 0 rgba(59,42,26,.15)}}
.diari{{left:130px;top:300px;font-family:Caveat,cursive;font-size:64px;color:#22304A;transform:rotate(-3deg)}}
.sub{{position:absolute;left:70px;right:70px;top:1395px;text-align:center;font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;font-size:76px;line-height:1.18;color:#3B2A1A;
  text-shadow:0 4px 0 #fff,4px 0 0 #fff,-4px 0 0 #fff,0 -4px 0 #fff}}
.sub span{{padding:0 6px;border-radius:12px}} .sub span.on{{background:#F5C04A;text-shadow:none}}
.who{{position:absolute;left:0;right:0;top:1318px;text-align:center}} .who b{{display:inline-block;font-size:34px;border-radius:999px;padding:6px 22px;color:#fff;border:4px solid #3B2A1A}}
.card{{background:#fff;border:7px solid #3B2A1A;border-radius:34px;box-shadow:0 12px 0 #3B2A1A;padding:30px 36px;text-align:center}}
.cop{{left:120px;right:120px;top:560px;border:12px double #C8473B;color:#C8473B;border-radius:30px;padding:30px;text-align:center;transform:rotate(-4deg);background:rgba(255,255,255,.75)}}
.cop h2{{font-family:Fredoka;font-size:86px;letter-spacing:.04em}} .cop p{{color:#3B2A1A;font-size:52px;line-height:1.25;margin-top:14px}}
.bk{{left:250px;width:580px;top:470px;height:420px;background:#6B4A2B;color:#FCEFC7;border:8px solid #3B2A1A;border-radius:16px 30px 30px 16px;box-shadow:16px 16px 0 #3B2A1A;padding:50px 40px;text-align:center}}
.bk h3{{font-family:Fredoka;font-size:66px;line-height:1.05}} .bk p{{font-size:40px;margin-top:24px;color:#F5C04A}}
"""
class Ep:
    def __init__(s, name, gaps=None):
        s.name = name; s.D = json.load(open(name + '.tts.json')); gaps = gaps or {}
        s.S, t = [], 0.35
        for i, r in enumerate(s.D):
            t += gaps.get(i, 0.0) if i else 0
            s.S.append(t); t += r['words'][-1][1] + 0.38
        s.END = s.S[-1] + s.D[-1]['dur']; s.T = round(s.END + 3.6, 2); s.E = s.S[1:] + [s.END + 0.2]
    def w(s, i, word, nth=0):
        for k, w in enumerate(s.D[i]['words']):
            if w[2].lower().startswith(word.lower()):
                if nth == 0: return round(s.S[i] + w[0], 2)
                nth -= 1
        return s.S[i]
    def audio(s):
        D, S, T = s.D, s.S, s.T; inp, flt = [], []
        for i, r in enumerate(D):
            inp += ['-i', r['f']]; flt.append(f'[{i}:a]adelay={int(S[i]*1000)}|{int(S[i]*1000)},aresample=44100,pan=stereo|c0=c0|c1=c0[v{i}]')
        n = len(D); inp += ['-stream_loop', '-1', '-i', MUZIK]
        flt.append(''.join(f'[v{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0,volume=1.6[vo]')
        flt.append(f'[{n}:a]atrim=0:{T},volume=0.10,afade=t=out:st={T-2}:d=2[mu]')
        flt.append('[vo][mu]amix=inputs=2:normalize=0,alimiter=limit=0.95[out]')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inp, '-filter_complex', ';'.join(flt), '-map', '[out]', '-t', str(T), '-c:a', 'aac', '-b:a', '160k', s.name + '_audio.m4a'], check=True)
    def frame(s, epn, banner, hari):
        return [item(0, s.T, '', '', 'paper', 'none'),
                item(0, s.END + .2, f'📖 TUNAS BACA BUKU · EP {epn:02d}', '', 'epc', 'none'),
                item(0, s.END + .2, banner, '', 'tape', 'none'),
                item(0, s.S[1], f'Diari Tunas, hari ke-{hari} ✍️', '', 'diari', 'none'),
                item(0, s.END + .2, 'Watak & cerita rekaan · bahan pendidikan, bukan nasihat pelaburan', 'bottom:60px', 'disc', 'fade')]
    def closing(s, cop, nxt):
        i = len(s.D) - 1
        it = [item(s.S[i] - 0.3, s.END + .2, f'<h2>1 BENIH HARI NI 🌱</h2><p>{cop}</p>', '', 'cop', 'pop'),
              ch(s.S[i], s.END + .2, 'T_thumb', 400, 1030, 300, 'pop', 'bob')]
        end = ending(s.END + 0.2, s.T)
        end[3] = item(s.END + 1.0, s.T, f'Follow untuk {nxt} 🌱', 'left:140px;right:140px;top:1520px', 'chip', 'pop', 'pulse')
        end[4] = item(s.END + .2, s.T, 'Watak & cerita rekaan · suara AI · bahan pendidikan, bukan nasihat pelaburan', '', 'disc', 'fade')
        return it + end
    def write(s, it, extra_css='', extra_js=''):
        D, S = s.D, s.S; SUB = []
        for i, r in enumerate(D):
            ws = [[round(S[i] + a, 2), round(S[i] + b, 2), w] for a, b, w in r['words']]
            toks = r['text'].split(); j = 0
            for w in ws:
                while j < len(toks) and not re.sub(r'[^\w-]', '', toks[j]).lower().startswith(re.sub(r'[^\w-]', '', w[2]).lower()[:3]): j += 1
                if j < len(toks): w[2] = toks[j]; j += 1
            chunk = []
            for w in ws:
                chunk.append(w)
                if len(chunk) >= 5 or re.search(r'[.,?!:…]$', w[2]): SUB.append({'who': r['who'], 'w': chunk}); chunk = []
            if chunk: SUB.append({'who': r['who'], 'w': chunk})
        for k, c in enumerate(SUB):
            c['t0'] = c['w'][0][0] - 0.05
            c['t1'] = (SUB[k + 1]['w'][0][0] - 0.05) if k + 1 < len(SUB) and SUB[k + 1]['w'][0][0] - c['w'][-1][1] < 0.9 else c['w'][-1][1] + 0.5
        SUBJS = 'const SUB=' + json.dumps(SUB, ensure_ascii=False) + r""";
        const sb=document.createElement('div');sb.className='sub';document.body.appendChild(sb);
        const wh=document.createElement('div');wh.className='who';document.body.appendChild(wh);
        const NAMA={T:['TUNAS','#5FA82E'],K:['KUNTUM','#D4574B']};
        const R0=window.render;window.render=t=>{R0(t);const c=SUB.find(c=>t>=c.t0&&t<c.t1);
         if(!c){sb.innerHTML='';wh.innerHTML='';return}
         sb.innerHTML=c.w.map(w=>`<span class="${t>=w[0]-0.03&&t<w[1]?'on':''}">${w[2]}</span>`).join(' ');
         const n=NAMA[c.who];wh.innerHTML=`<b style="background:${n[1]}">${n[0]}</b>`;};
        """
        html = page(it, [[0, '#FFF8E8']]).replace('</style>', X + extra_css + '</style>', 1).replace('</body>', '<script>' + SUBJS + extra_js + '</script></body>')
        open(s.name + '.html', 'w').write(html); s.audio()
        print('T', s.T, 'S', [round(x, 2) for x in S])
