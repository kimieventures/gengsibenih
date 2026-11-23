# Gaya "scrapbook berita" untuk siri Fail Duit Tunas: kertas, kad koyak, highlighter, polaroid, selotip, slip, cop.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tbblib import *
SB = """
body{background:#EDE3CF}
.kertas{position:absolute;inset:0;background:#EFE5D0;background-image:radial-gradient(circle at 20% 15%,rgba(255,255,255,.55),transparent 40%),radial-gradient(circle at 85% 80%,rgba(160,120,70,.18),transparent 45%),repeating-linear-gradient(0deg,rgba(120,90,50,.035) 0 2px,transparent 2px 5px)}
.koyak{background:#FFFDF6;padding:40px 46px;font-family:Georgia,serif;font-weight:400;font-size:52px;line-height:1.35;color:#2B2116;box-shadow:6px 10px 18px rgba(60,40,20,.25);clip-path:polygon(0 3%,4% 0,9% 2%,15% 0,22% 3%,30% 1%,38% 3%,46% 0,55% 2%,63% 0,71% 3%,80% 1%,88% 3%,95% 0,100% 2%,99% 97%,94% 100%,86% 98%,77% 100%,69% 97%,60% 100%,51% 98%,42% 100%,33% 97%,24% 100%,15% 98%,7% 100%,0 97%)}
.koyak small{display:block;margin-top:22px;padding-top:18px;border-top:3px dashed #B9A88C;font-family:Nunito,sans-serif;font-size:32px;color:#5E4B37;text-align:center}
.hl{background:linear-gradient(transparent 55%,#FFE45C 55%,#FFE45C 92%,transparent 92%);background-repeat:no-repeat;background-size:0% 100%}
.selo{width:170px;height:54px;background:rgba(245,230,180,.85);box-shadow:0 2px 4px rgba(0,0,0,.12)}
.lbl{background:#FFFDF6;border:4px solid #2B2116;padding:8px 22px;font-family:'Courier New',monospace;font-weight:700;font-size:34px;color:#2B2116;box-shadow:4px 4px 0 #2B2116}
.lblk{background:#F5C04A;border:4px solid #2B2116;padding:8px 22px;font-size:36px;color:#2B2116;box-shadow:4px 4px 0 #2B2116}
.polar{background:#fff;padding:26px 26px 80px;box-shadow:6px 12px 20px rgba(60,40,20,.3);text-align:center}
.polar p{font-family:Caveat,cursive;font-size:46px;color:#22304A;margin-top:14px}
.fon{width:470px;height:820px;background:#1E1E24;border-radius:60px;padding:26px;box-shadow:10px 16px 26px rgba(0,0,0,.35)}
.fon .sc{width:100%;height:100%;background:#fff;border-radius:40px;overflow:hidden;font-family:Nunito,sans-serif;font-size:34px;color:#222}
.fon .bar{background:#3B5998;color:#fff;padding:18px 24px;font-weight:900;font-size:30px}
.slip{width:640px;background:#FFFDF6;border:4px solid #2B2116;border-radius:14px;padding:20px 28px;font-family:'Courier New',monospace;font-weight:700;font-size:34px;color:#2B2116;box-shadow:6px 8px 0 rgba(43,33,22,.6)}
.slip b{color:#C8473B}
.cop2{border:12px double #C8473B;color:#C8473B;border-radius:24px;padding:26px 40px;text-align:center;background:rgba(255,255,255,.6);font-family:Fredoka,sans-serif}
.alir{display:flex;flex-direction:column;align-items:center;gap:14px}
.alir div{background:#fff;border:6px solid #2B2116;border-radius:26px;padding:18px 30px;font-size:46px;box-shadow:0 8px 0 #2B2116;text-align:center;width:640px}
.alir i{font-style:normal;font-size:54px}
.sumber{position:absolute;left:0;right:0;bottom:40px;text-align:center;font-family:'Courier New',monospace;font-weight:700;font-size:28px;color:#5E4B37}
.sub{top:1450px} .who{top:1372px}
"""
HLJS = r"""const HL=[...document.querySelectorAll('.hl')].map(e=>({e,t:+e.dataset.t,d:+(e.dataset.d||0.8)}));
const R1=window.render;window.render=t=>{R1(t);for(const h of HL){const k=Math.min(1,Math.max(0,(t-h.t)/h.d));h.e.style.backgroundSize=(k*100)+'% 100%'}};"""
hl = lambda txt, t, d=0.8: f'<span class="hl" data-t="{t}" data-d="{d}">{txt}</span>'
selo = lambda t0, t1, x, y, r: item(t0, t1, '', f'left:{x}px;top:{y}px;transform:rotate({r}deg)', 'selo', 'pop')
kad = lambda t0, t1, html, st, en='pop', lp='': item(t0, t1, html, st, 'koyak', en, lp)
def rangka(e, kes, sumber, end_lesson):
    return [item(0, e.T, '', '', 'kertas', 'none'),
            item(0, e.END + .2, f'📁 FAIL DUIT TUNAS · KES {kes:02d}', 'left:70px;top:70px;background:#2B2116;color:#FFF6E5', 'lbl', 'none'),
            item(0, e.END + .2, 'KES SEBENAR', 'left:770px;top:66px;transform:rotate(4deg);background:#C8473B;color:#fff', 'lblk', 'none'),
            item(0, end_lesson, f'Sumber: {sumber} · rumusan Geng Si Benih', '', 'sumber', 'none')]
def penutup(e, cta_h2, cta_p):
    i = len(e.D) - 1
    it = [item(e.S[i], e.E[i], f'<h2>{cta_h2}</h2><p>{cta_p}</p>', '', 'cop', 'pop'), ch(e.S[i], e.E[i], 'T_thumb', 400, 1030, 300, 'pop', 'bob')]
    end = ending(e.END + 0.2, e.T)
    end[3] = item(e.END + 1.0, e.T, 'Follow untuk Fail Duit seterusnya 📁', 'left:120px;right:120px;top:1520px', 'chip', 'pop', 'pulse')
    end[4] = item(e.END + .2, e.T, 'Rumusan berita · watak Tunas rekaan · ilustrasi · suara AI · bahan pendidikan, bukan nasihat pelaburan', 'left:40px;right:40px', 'disc', 'fade')
    return it + end
def tulis(e, it): e.write(it, SB, HLJS)
