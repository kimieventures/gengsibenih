# Penjana video intro Geng Si Benih (1080x1920, 30fps). Setiap video = senarai babak + item bertempoh.
import json, os, sys
import os
BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, 'img')
FONT = os.environ.get('GSB_FONT', os.path.join(BASE, 'node_modules/@fontsource'))

CSS = f"""
@font-face{{font-family:Fredoka;font-weight:700;src:url(file://{FONT}/fredoka/files/fredoka-latin-700-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:800;src:url(file://{FONT}/nunito/files/nunito-latin-800-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:900;src:url(file://{FONT}/nunito/files/nunito-latin-900-normal.woff2)}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1920px;overflow:hidden;font-family:Nunito,'Noto Color Emoji',sans-serif;font-weight:800;color:#3B2A1A}}
#bg{{position:absolute;inset:0}}
.it{{position:absolute;transform-origin:50% 50%;will-change:transform,opacity}}
.cap{{left:60px;right:60px;top:150px;text-align:center;font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;font-size:78px;line-height:1.1;color:#3B2A1A;
  text-shadow:0 4px 0 #fff,4px 0 0 #fff,-4px 0 0 #fff,0 -4px 0 #fff}}
.bub{{background:#fff;border:6px solid #3B2A1A;border-radius:44px;padding:26px 36px;font-size:54px;line-height:1.2;box-shadow:0 10px 0 #3B2A1A;text-align:center}}
.ch{{height:620px}}
.ntf{{left:90px;right:90px;background:#fff;border:5px solid #3B2A1A;border-radius:30px;padding:22px 30px;font-size:46px;line-height:1.2;box-shadow:0 8px 0 #D4574B}}
.ntf b{{display:block;font-size:30px;color:#D4574B;letter-spacing:.04em}}
.big{{font-family:Fredoka,'Noto Color Emoji',sans-serif;font-weight:700;text-align:center}}
.chip{{background:#5FA82E;color:#fff;border:6px solid #3B2A1A;border-radius:999px;padding:24px 40px;font-size:50px;box-shadow:0 10px 0 #3B2A1A;text-align:center}}
.disc{{left:0;right:0;bottom:70px;text-align:center;font-size:30px;color:#5E4B37}}
.board{{background:#2A2116;color:#FCEFC7;border:8px solid #3B2A1A;border-radius:36px;padding:34px 40px;font-size:52px;line-height:1.5;box-shadow:0 12px 0 #3B2A1A}}
.board h3{{color:#F5C04A;font-family:Fredoka,sans-serif;font-size:56px;text-align:center;margin-bottom:10px}}
.board .r{{display:flex;justify-content:space-between;gap:30px}}
"""

JS = r"""
const IT=[...document.querySelectorAll('.it')].map(e=>({e,t0:+e.dataset.t0,t1:+e.dataset.t1,en:e.dataset.en||'pop',lp:e.dataset.lp||'',bx:e.dataset.bx||''}));
const BG=JSON.parse(document.getElementById('bgd').textContent);
const ease=p=>1-Math.pow(1-p,3), back=p=>{const c=1.7;return 1+(c+1)*Math.pow(p-1,3)+c*Math.pow(p-1,2)};
window.render=t=>{
  let b=BG[0][1]; for(const [s,c] of BG) if(t>=s) b=c; document.getElementById('bg').style.background=b;
  for(const o of IT){
    if(t<o.t0||t>=o.t1){o.e.style.opacity=0;continue}
    const p=Math.min(1,(t-o.t0)/0.45), q=Math.min(1,(o.t1-t)/0.3), r=t-o.t0;
    let tf='',op=Math.min(1,q*1.2);
    if(o.en==='pop'){const s=back(p);tf+=`scale(${Math.max(0,s)})`;op*=Math.min(1,p*3)}
    if(o.en==='fade'){op*=ease(p)}
    if(o.en==='up'){tf+=`translateY(${(1-ease(p))*160}px)`;op*=ease(p)}
    if(o.en==='left'){tf+=`translateX(${(1-ease(p))*-900}px)`}
    if(o.en==='right'){tf+=`translateX(${(1-ease(p))*900}px)`}
    if(o.en==='drop'){tf+=`translateY(${(1-back(p))*-700}px)`;op*=Math.min(1,p*4)}
    if(o.lp==='bob') tf+=` translateY(${Math.sin(r*4)*14}px)`;
    if(o.lp==='shake') tf+=` rotate(${Math.sin(r*40)*4}deg) translateX(${Math.sin(r*55)*10}px)`;
    if(o.lp==='wig') tf+=` rotate(${Math.sin(r*6)*5}deg)`;
    if(o.lp==='pulse') tf+=` scale(${1+Math.sin(r*7)*0.05})`;
    if(o.lp==='fall') tf+=` translateY(${r*r*420}px) rotate(${r*90}deg)`;
    o.e.style.transform=tf; o.e.style.opacity=op;
    if(o.bx){ // nombor menghitung
      const [a,z,d,pre]=o.bx.split('|'); const k=Math.min(1,Math.max(0,(r-0.3)/(+d))); o.e.querySelector('.n').textContent=pre+Math.round(+a+(+z-+a)*ease(k)).toLocaleString('en-US');}
    o.e.querySelectorAll('[data-draw]').forEach(pth=>{const L=pth.getTotalLength(),d=+pth.dataset.draw,dl=+(pth.dataset.dl||0);pth.style.strokeDasharray=L;pth.style.strokeDashoffset=L*(1-Math.min(1,Math.max(0,(r-dl)/d)))});
  }
};
"""

def img(k): return f'file://{IMG}/{k}.png'

def item(t0, t1, html, style, cls='', en='pop', lp='', bx=''):
    return f'<div class="it {cls}" data-t0="{t0}" data-t1="{t1}" data-en="{en}" data-lp="{lp}" data-bx="{bx}" style="{style}">{html}</div>'

def page(items, bgs):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body><div id="bg"></div>' +
            ''.join(items) + '<script type="application/json" id="bgd">' + json.dumps(bgs) + '</script><script>' + JS + '</script></body></html>')

# ---------- komponen ----------
def cap(t0, t1, txt): return item(t0, t1, txt, '', 'cap', 'up')
def ch(t0, t1, k, x, y, h=620, en='pop', lp='bob'):
    return item(t0, t1, f'<img src="{img(k)}" style="height:{h}px">', f'left:{x}px;top:{y}px', '', en, lp)
def bub(t0, t1, txt, x, y, w=760, en='pop', bg='#fff'):
    return item(t0, t1, txt, f'left:{x}px;top:{y}px;width:{w}px;background:{bg}', 'bub', en)
def ntf(t0, t1, who, txt, y, en='drop', lp=''):
    return item(t0, t1, f'<b>{who}</b>{txt}', f'top:{y}px', 'ntf', en, lp)
def big(t0, t1, txt, y, size=120, color='#3B2A1A', en='pop', lp=''):
    return item(t0, t1, txt, f'left:40px;right:40px;top:{y}px;font-size:{size}px;color:{color}', 'big', en, lp)
def emo(t0, t1, e, x, y, size=140, en='pop', lp='wig'):
    return item(t0, t1, e, f'left:{x}px;top:{y}px;font-size:{size}px', '', en, lp)

def ending(t0, T=30):
    return [
        item(t0, T, f'<img src="{img("GROUP")}" style="width:860px">', 'left:110px;top:430px', '', 'pop', 'bob'),
        big(t0 + 0.4, T, 'Geng Si Benih', 1130, 130, '#3B2A1A', 'up'),
        big(t0 + 0.9, T, 'Belajar duit dari sifar.<br>Tanpa tip. Tanpa pening.', 1300, 62, '#5E4B37', 'up'),
        item(t0 + 1.6, T, 'Follow untuk 30 saat ilmu<br>setiap hari 🌱', 'left:140px;right:140px;top:1520px', 'chip', 'pop', 'pulse'),
        item(t0, T, 'Watak & cerita rekaan · Bahan pendidikan, bukan nasihat pelaburan', '', 'disc', 'fade'),
    ]
