# Video panjang YouTube (16:9): "Kos Sebenar Beli 1 Lot Saham di Bursa" — slaid + teks + muzik asli.
# Watak & cerita rekaan. Semua angka ialah CONTOH. Bahan pendidikan, bukan nasihat pelaburan.
import os, subprocess
from playwright.sync_api import sync_playwright
BASE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(BASE, 'node_modules/@fontsource')
OUT = os.path.join(BASE, 'out', 'yt'); os.makedirs(OUT, exist_ok=True)

CSS = f"""
@font-face{{font-family:Fredoka;font-weight:700;src:url(file://{F}/fredoka/files/fredoka-latin-700-normal.woff2)}}
@font-face{{font-family:Nunito;font-weight:800;src:url(file://{F}/nunito/files/nunito-latin-800-normal.woff2)}}
@font-face{{font-family:Caveat;font-weight:700;src:url(file://{F}/caveat/files/caveat-latin-700-normal.woff2)}}
*{{box-sizing:border-box;margin:0}}
body{{width:1920px;height:1080px;overflow:hidden;font-family:Nunito,'Noto Color Emoji',sans-serif;font-weight:800;color:#2B1F14;
 background:linear-gradient(180deg,#FCEFC7,#FFF6E5);padding:80px 120px;position:relative}}
body.dark{{background:linear-gradient(180deg,#2A2F36,#14181C);color:#F4EEE2}}
.tag{{position:absolute;left:120px;top:44px;font-size:30px;color:#5FA82E;letter-spacing:.06em;text-transform:uppercase}}
.foot{{position:absolute;left:0;right:0;bottom:26px;text-align:center;font-size:24px;color:#7A6650}}
.dark .foot{{color:#9AA4AD}}
h1{{font-family:Fredoka,'Noto Color Emoji',sans-serif;font-size:96px;line-height:1.08;margin-top:40px}}
h2{{font-family:Fredoka,'Noto Color Emoji',sans-serif;font-size:72px;line-height:1.1;margin:30px 0 36px}}
p,li{{font-size:52px;line-height:1.35}}
ul{{padding-left:50px;display:grid;gap:22px}}
.hl{{background:#F5C04A;color:#2B1F14;padding:0 14px;border-radius:10px}}
.red{{color:#C8473B}} .grn{{color:#3E7D1F}} .dark .grn{{color:#86C65A}} .dark .red{{color:#FF8A7A}}
.big{{font-family:Fredoka,'Noto Color Emoji',sans-serif;font-size:150px;line-height:1}}
table{{border-collapse:collapse;font-size:50px;width:100%}}
td,th{{padding:18px 26px;border-bottom:3px dashed #D9C7A6;text-align:left}}
th{{font-family:Fredoka,sans-serif;color:#5E4B37}}
td.r,th.r{{text-align:right}}
tr.tot td{{border-top:5px solid #2B1F14;border-bottom:none;font-size:58px}}
.note{{font-size:34px;color:#6E5B45;margin-top:28px}}
.diari{{background:#FFFDF3;border:6px solid #2B1F14;border-radius:24px;padding:40px 60px 40px 120px;
 background-image:repeating-linear-gradient(180deg,transparent 0 78px,#BFD8EE 78px 81px),linear-gradient(90deg,transparent 90px,#F2A7A0 90px 94px,transparent 94px);
 font-family:Caveat,'Noto Color Emoji',cursive;font-size:78px;line-height:81px;color:#22304A;margin-top:30px}}
.card{{background:#fff;border:6px solid #2B1F14;border-radius:36px;padding:44px 56px;box-shadow:0 12px 0 #5FA82E}}
.row{{display:flex;gap:40px;align-items:stretch}} .row>div{{flex:1}}
.cta{{display:inline-block;background:#5FA82E;color:#fff;border:6px solid #2B1F14;border-radius:999px;padding:26px 60px;font-size:64px;box-shadow:0 10px 0 #2B1F14;margin-top:40px}}
"""
FOOT = 'Watak & cerita rekaan · Angka contoh · Bahan pendidikan, bukan nasihat pelaburan'

def html(body, tag='', dark=False):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body class="{"dark" if dark else ""}"><div class="tag">{tag}</div>{body}<div class="foot">{FOOT}</div></body></html>')

# Setiap slaid: (tag, dark, [(html_terkumpul, saat), ...]) — langkah dipaparkan berturut-turut
S = []
def slide(tag, steps, dark=False):
    S.append((tag, dark, steps))

def build(parts, durs):
    """parts dipaparkan secara kumulatif."""
    return [(''.join(parts[:i + 1]), d) for i, d in enumerate(durs)]

# 1. Hook (frame 0 sudah ada konflik + nombor)
slide('Diari Duit Tunas · Video penuh', build([
    '<h1>Tunas beli <span class="hl">1 lot</span> saham.<br>Harga: <span class="red">RM50</span>.</h1>',
    '<p style="margin-top:50px">Dividen setahun (contoh 6%): <b class="grn">RM3</b></p>',
    '<p>Kos beli + jual (contoh): <b class="red">± RM18</b></p>',
    '<h2 style="margin-top:60px">Berapa tahun dividen hanya untuk<br>tutup kos? 🤔 Kita kira sama-sama.</h2>',
], [3, 3.5, 4, 6]), dark=True)

slide('Geng Si Benih', [(
    '<h1 style="margin-top:160px;text-align:center">Kos Sebenar Beli 1 Lot<br>Saham di Bursa</h1>'
    '<p style="text-align:center;margin-top:40px">Kenapa beli RM50 boleh jadi rugi sebelum mula</p>', 7)])

slide('Bahagian 1 · Apa itu 1 lot?', build([
    '<h2>Di Bursa Malaysia, saham dibeli ikut <span class="hl">lot</span>.</h2>',
    '<p class="big" style="margin:30px 0">1 lot = 100 unit</p>',
    '<ul><li>Harga RM0.50 × 100 unit = <b>RM50</b> satu lot</li>',
    '<li>Harga RM5.00 × 100 unit = <b>RM500</b> satu lot</li></ul>',
    '<p class="note">Jadi "beli 1 lot" tak semestinya mahal. Tapi ada kos tetap yang ramai pemula terlepas pandang.</p>',
], [5, 6, 6, 6, 9]))

slide('Bahagian 2 · Tiga kos setiap kali beli ATAU jual', build([
    '<h2>Setiap transaksi ada 3 kos utama:</h2><ul>',
    '<li><b>Komisen broker</b>: contoh 0.1%, tetapi ada <span class="hl">caj minimum</span> (contoh RM8)</li>',
    '<li><b>Fi penjelasan</b>: 0.03% daripada nilai dagangan</li>',
    '<li><b>Duti setem</b>: RM1 bagi setiap RM1,000 (atau sebahagian daripadanya)</li></ul>',
    '<p class="note">Cukai perkhidmatan atas komisen mungkin dikenakan. Kadar & caj minimum berbeza ikut broker dan jenis akaun: semak jadual caj broker anda sendiri.</p>',
], [5, 12, 9, 11, 14]))

slide('Bahagian 2 · Perangkap utama', build([
    '<h2>Yang paling "makan" modal kecil:<br><span class="red">caj minimum</span> komisen.</h2>',
    '<p>0.1% daripada RM50 = 5 sen sahaja…</p>',
    '<p>tetapi kalau caj minimum RM8, anda bayar <b class="red">RM8</b>.</p>',
    '<p class="note">Itu sebabnya kos sebagai % modal jadi sangat tinggi bila nilai belian kecil.</p>',
], [6, 6, 7, 10]))

def calc(tag, modal, kom, fi, duti, sehala, pb, pct, extra=''):
    rows = (f'<table><tr><th>Perkara (contoh)</th><th class="r">Sehala</th></tr>'
            f'<tr><td>Nilai belian</td><td class="r">{modal}</td></tr>'
            f'<tr><td>Komisen (minimum RM8)</td><td class="r">{kom}</td></tr>'
            f'<tr><td>Fi penjelasan 0.03%</td><td class="r">{fi}</td></tr>'
            f'<tr><td>Duti setem</td><td class="r">{duti}</td></tr>'
            f'<tr class="tot"><td>Kos sehala</td><td class="r red">{sehala}</td></tr></table>')
    slide(tag, build([
        rows,
        f'<p style="margin-top:34px">Beli + jual (pergi-balik): <b class="red">{pb}</b> = <span class="hl">{pct} modal</span></p>',
        extra,
    ], [16, 9, 12 if extra else 0.1]))

calc('Kira 1 · Belian RM50', 'RM50.00', 'RM8.00', 'RM0.02', 'RM1.00', '≈ RM9.02', '≈ RM18', '36%',
     '<p class="note">Dividen contoh 6% = RM3 setahun. RM18 ÷ RM3 = <b>6 tahun</b> dividen hanya untuk tutup kos. 😵</p>')
calc('Kira 2 · Belian RM500', 'RM500.00', 'RM8.00', 'RM0.15', 'RM1.00', '≈ RM9.15', '≈ RM18.30', '± 3.7%',
     '<p class="note">Lebih baik, tapi masih makan lebih setengah tahun dividen contoh 6% (RM30 setahun).</p>')
calc('Kira 3 · Belian RM5,000', 'RM5,000.00', 'RM8.00', 'RM1.50', 'RM5.00', '≈ RM14.50', '≈ RM29', '± 0.6%',
     '<p class="note">Kos tetap sama-sama ada, tetapi bahagiannya dalam modal jadi kecil.</p>')

slide('Ringkasan', build([
    '<h2>Kos pergi-balik sebagai % modal (contoh)</h2>'
    '<table><tr><th>Modal</th><th class="r">Kos pergi-balik</th><th class="r">% modal</th></tr>'
    '<tr><td>RM50</td><td class="r">≈ RM18</td><td class="r red">36%</td></tr>'
    '<tr><td>RM500</td><td class="r">≈ RM18.30</td><td class="r">3.7%</td></tr>'
    '<tr><td>RM5,000</td><td class="r">≈ RM29</td><td class="r grn">0.6%</td></tr></table>',
    '<p class="note">Kos tidak naik selaju modal kerana caj minimum. Itulah "perangkap kos 1 lot".</p>',
], [18, 12]))

slide('Pelajaran · Nilai minimum belian yang masuk akal', build([
    '<h2>Sebelum tekan "Beli", kira dulu:</h2>',
    '<p class="big" style="font-size:96px;margin:20px 0 30px">kos pergi-balik ÷ modal</p>',
    '<p>Contoh had peribadi: <span class="hl">kos ≤ 1% modal</span>.</p>',
    '<p>Dengan caj contoh di atas, itu bermaksud belian sekitar <b>RM2,500 ke atas</b> setiap kali.</p>',
    '<p class="note">Had ini contoh rangka kerja untuk anda tetapkan sendiri, bukan cadangan berapa atau saham apa untuk dibeli.</p>',
], [5, 7, 8, 12, 12]))

slide('Kesilapan pemula', build([
    '<h2>4 kesilapan kos yang biasa:</h2><ul>',
    '<li>Beli sikit-sikit, kerap (setiap kali kena caj minimum)</li>',
    '<li>Jual cepat (kos dua kali dalam masa singkat)</li>',
    '<li>Lupa caj minimum bila kira "untung"</li>',
    '<li>Kejar dividen tanpa tolak kos dagangan</li></ul>',
], [5, 8, 8, 8, 10]))

slide('Diari Tunas', [(
    '<div class="diari">Pelajaran saya minggu ni:<br>bukan saham tu mahal.<br><b style="color:#C8473B">Kos kecil yang berulang</b><br>yang makan modal. ✍️</div>', 14)])

slide('Latihan untuk anda', build([
    '<h2>Cuba sendiri (5 minit):</h2><ul>',
    '<li>Buka jadual caj broker anda: catat <b>% komisen</b> dan <b>caj minimum</b></li>',
    '<li>Pilih satu nilai belian yang anda rancang (contoh RM300)</li>',
    '<li>Kira kos pergi-balik dan % modal</li></ul>',
    '<p class="note">Kalkulator kos ada dalam pelajaran Hari 1 app Geng Si Benih: isi nombor anda sendiri.</p>',
], [5, 10, 8, 8, 10]))

slide('Geng Si Benih', build([
    '<h1 style="text-align:center;margin-top:120px">Belajar duit dari kosong.<br>Tanpa tip. Tanpa janji untung.</h1>',
    '<div style="text-align:center"><span class="cta">Cuba 3 hari percuma 🌱 Link di deskripsi</span></div>',
    '<p class="note" style="text-align:center;margin-top:50px">Komen: berapa nilai belian minimum yang korang rasa masuk akal? 👇</p>',
], [5, 8, 10]))

if __name__ == '__main__':
    lst = []; n = 0; total = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for tag, dark, steps in S:
            for body, d in steps:
                if d < 0.5: continue
                f = os.path.join(OUT, f's{n:03d}.png')
                hf = os.path.join(OUT, 'tmp.html'); open(hf, 'w').write(html(body, tag, dark)); pg.goto('file://' + hf); pg.wait_for_timeout(300); pg.screenshot(path=f)
                lst.append((f, d)); n += 1; total += d
        b.close()
    with open(os.path.join(OUT, 'list.txt'), 'w') as fh:
        for f, d in lst: fh.write(f"file '{f}'\nduration {d}\n")
        fh.write(f"file '{lst[-1][0]}'\n")
    print(n, 'langkah,', total, 's')
