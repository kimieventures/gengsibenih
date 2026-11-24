# Video panjang YouTube (16:9): "Emas untuk Pemula: 2 Harga yang Patut Ditanya Sebelum Beli".
# Diambil dari modul Celik Emas (Hari 12-14: spread, upah, 2 kedai). Slaid + teks + muzik asli.
# Kedai, harga & watak REKAAN. Semua angka CONTOH. Bahan pendidikan, bukan nasihat pelaburan.
import os
from playwright.sync_api import sync_playwright
import yt_kos1lot as K   # guna CSS & html() yang sama

OUT = os.path.join(K.BASE, 'out', 'yt_emas'); os.makedirs(OUT, exist_ok=True)
K.FOOT = 'Kedai, harga & watak rekaan · Angka contoh · Bahan pendidikan, bukan nasihat pelaburan'
S = []
def slide(tag, steps, dark=False): S.append((tag, dark, steps))
def build(parts, durs): return [(''.join(parts[:i + 1]), d) for i, d in enumerate(durs)]

# 1. Hook (frame 0: konflik + nombor)
slide('Diari Duit Tunas · Video penuh', build([
    '<h1>Tunas beli emas <span class="hl">RM4,600</span>.<br>Esoknya nak jual balik: <span class="red">RM4,250</span>.</h1>',
    '<p style="margin-top:50px">Harga emas tak berubah pun. Tapi <b class="red">RM350</b> dah hilang.</p>',
    '<h2 style="margin-top:60px">Ke mana duit tu pergi? 🤔<br>Jawapannya: DUA harga yang ramai tak tanya.</h2>',
], [4, 6, 8]), dark=True)

slide('Geng Si Benih', [(
    '<h1 style="margin-top:160px;text-align:center">Emas untuk Pemula:<br>2 Harga yang Patut Ditanya Sebelum Beli</h1>'
    '<p style="text-align:center;margin-top:40px">Spread, upah & cara banding kedai, dengan kiraan mudah</p>', 7)])

slide('Bahagian 1 · Dua harga di papan kedai', build([
    '<h2>Setiap kedai emas ada dua harga:</h2>',
    '<div class="row"><div class="card"><p class="red" style="font-size:60px">Harga JUAL</p><p>Harga kedai jual <b>kepada anda</b> (anda beli)</p></div>'
    '<div class="card" style="box-shadow:0 12px 0 #F5C04A"><p class="grn" style="font-size:60px">Harga BELI BALIK</p><p>Harga kedai beli <b>daripada anda</b> (anda jual semula)</p></div></div>',
    '<p class="note">Harga jual sentiasa lebih tinggi. Beza antara dua harga ini dipanggil <b>spread</b>: itulah kos pertama anda.</p>',
], [5, 14, 12]))

slide('Bahagian 1 · Papan harga Kedai Emas Cahaya (rekaan)', build([
    '<table><tr><th>Emas 999 · per gram</th><th class="r">Harga</th></tr>'
    '<tr><td>Harga jual (anda beli)</td><td class="r red">RM460</td></tr>'
    '<tr><td>Harga beli balik (anda jual)</td><td class="r grn">RM425</td></tr>'
    '<tr class="tot"><td>Beza (spread)</td><td class="r">RM35</td></tr></table>',
    '<p style="margin-top:34px">RM35 ÷ RM460 = <span class="hl">7.6%</span> hilang sebaik keluar kedai</p>',
    '<p class="note">Beli 10 g = RM4,600. Jual balik serta-merta = RM4,250. Itulah RM350 Tunas.</p>',
], [14, 10, 12]))

slide('Bahagian 1 · Garisan pulang modal', build([
    '<h2>Berapa harga perlu naik untuk pulang modal?</h2>',
    '<p>Harga <b>beli balik</b> mesti naik dari RM425 ke RM460.</p>',
    '<p class="big" style="font-size:110px;margin:30px 0">RM460 ÷ RM425 − 1 ≈ <span class="red">8.2%</span></p>',
    '<p class="note">Ini bukan ramalan harga. Ia cuma garisan permulaan: sebelum harga naik sebanyak itu, anda masih "rugi kertas" jika menjual.</p>',
], [5, 9, 10, 14]))

slide('Bahagian 2 · Barang kemas: ada kos kedua', build([
    '<h2>Rantai, gelang, cincin = ada <span class="hl">upah</span>.</h2>',
    '<ul><li>Upah = kos tukang & reka bentuk, dikira per gram atau per barang</li>',
    '<li>Bila jual balik, kedai biasanya bayar ikut <b>berat & ketulenan</b> sahaja</li>',
    '<li>Upah hampir tidak pernah "kembali"</li></ul>',
], [5, 9, 9, 8]))

slide('Bahagian 2 · Kira rantai 916 (contoh)', build([
    '<table><tr><th>Rantai 916 · 10 g (rekaan)</th><th class="r">RM</th></tr>'
    '<tr><td>Harga emas 916: RM430/g × 10 g</td><td class="r">4,300</td></tr>'
    '<tr><td>Upah: RM40/g × 10 g</td><td class="r">400</td></tr>'
    '<tr class="tot"><td>Anda bayar</td><td class="r red">4,700</td></tr></table>',
    '<p style="margin-top:30px">Jual balik ikut berat: RM395/g × 10 g = <b class="grn">RM3,950</b></p>',
    '<p>Beza: <b class="red">RM750</b> = <span class="hl">± 16%</span> modal</p>',
    '<p class="note">Barang kemas untuk dipakai: OK. Tapi kalau niat "simpanan", tahu dulu kosnya.</p>',
], [16, 10, 8, 12]))

slide('Bahagian 3 · Banding dua kedai (rekaan)', build([
    '<table><tr><th>Emas 999 / g</th><th class="r">Kedai Cahaya</th><th class="r">Kedai Bintang</th></tr>'
    '<tr><td>Harga jual</td><td class="r">RM460</td><td class="r">RM455</td></tr>'
    '<tr><td>Harga beli balik</td><td class="r">RM425</td><td class="r">RM440</td></tr>'
    '<tr class="tot"><td>Spread</td><td class="r red">7.6%</td><td class="r grn">3.3%</td></tr></table>',
    '<p style="margin-top:30px">Kedai Bintang bukan cuma "lebih murah RM5". Beza dua hargaannya jauh lebih kecil.</p>',
    '<p class="note">Pelajaran: jangan banding harga jual sahaja. Banding <b>spread</b>.</p>',
], [16, 12, 10]))

slide('Bahagian 3 · Formula 10 saat', build([
    '<h2>Di kaunter, tanya dua soalan:</h2>',
    '<ul><li>"Harga jual per gram berapa?"</li><li>"Kalau saya jual balik hari ni, kedai beli berapa?"</li></ul>',
    '<p class="big" style="font-size:96px;margin:36px 0">(jual − beli balik) ÷ jual</p>',
    '<p class="note">Untuk barang kemas, tanya juga: upah berapa, dan adakah upah dikira semasa jual balik?</p>',
], [5, 12, 10, 12]))

slide('Bahagian 4 · Cara memiliki emas, kos berbeza', build([
    '<h2>Tiga cara biasa & kos utamanya:</h2>',
    '<table><tr><th>Bentuk</th><th>Kos yang perlu ditanya</th></tr>'
    '<tr><td>Jongkong / syiling</td><td>Spread, kos simpan & insurans</td></tr>'
    '<tr><td>Barang kemas</td><td>Spread + upah</td></tr>'
    '<tr><td>Akaun emas / bukan fizikal</td><td>Spread, fi, siapa penjaga, terma tebus</td></tr></table>',
    '<p class="note">Semak terma sendiri: akaun pelaburan emas biasanya <b>tidak</b> dilindungi PIDM. Isu syariah (cth. belian ansuran): rujuk mufti / pusat zakat negeri anda.</p>',
], [5, 18, 16]))

slide('Bahagian 5 · Tanda merah', build([
    '<h2>Berhenti jika "skim emas" ada tanda ini 🚩</h2><ul>',
    '<li>Janji <b>untung tetap</b> setiap bulan</li>',
    '<li>Ganjaran kalau <b>ajak orang</b> masuk</li>',
    '<li>Desak: "slot terhad, malam ni tutup"</li>',
    '<li>Tak boleh tebus / tak jelas emas disimpan di mana</li></ul>',
    '<p class="note">Emas sebenar tidak menjanjikan pulangan tetap. Semak senarai amaran SC dan BNM. Tertipu? Hubungi NSRC 997 segera.</p>',
], [5, 7, 7, 7, 8, 12]))

slide('Kesilapan pemula', build([
    '<h2>4 kesilapan emas yang biasa:</h2><ul>',
    '<li>Tanya harga jual sahaja, lupa harga beli balik</li>',
    '<li>Anggap barang kemas = simpanan, tanpa kira upah</li>',
    '<li>Beli sebab berita / FOMO, selepas harga dah bergerak</li>',
    '<li>Jual balik terlalu cepat: spread jadi rugi sebenar</li></ul>',
], [5, 8, 8, 8, 9]))

slide('Diari Tunas', [(
    '<div class="diari">Pelajaran saya:<br>emas tak "untung" bila dibeli.<br><b style="color:#C8473B">Ia mula dengan kos.</b><br>Sekarang saya tanya dua harga dulu. ✍️</div>', 14)])

slide('Latihan untuk anda', build([
    '<h2>Cuba sendiri (5 minit):</h2><ul>',
    '<li>Tanya <b>dua kedai</b>: harga jual & harga beli balik per gram</li>',
    '<li>Kira spread setiap kedai: (jual − beli balik) ÷ jual</li>',
    '<li>Untuk barang kemas: catat upah, dan tolak dalam kiraan</li></ul>',
    '<p class="note">Ada kalkulator spread & upah dalam modul Celik Emas app Geng Si Benih: isi nombor anda sendiri.</p>',
], [5, 10, 9, 9, 10]))

slide('Geng Si Benih', build([
    '<h1 style="text-align:center;margin-top:120px">Belajar duit dari kosong.<br>Tanpa tip. Tanpa janji untung.</h1>',
    '<div style="text-align:center"><span class="cta">Cuba 3 hari percuma 🌱 Link di deskripsi</span></div>',
    '<p class="note" style="text-align:center;margin-top:50px">Komen: korang pernah tanya harga beli balik sebelum beli? 👇</p>',
], [5, 8, 10]))

if __name__ == '__main__':
    lst = []; n = 0; total = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for tag, dark, steps in S:
            for body, d in steps:
                f = os.path.join(OUT, f's{n:03d}.png')
                hf = os.path.join(OUT, 'tmp.html'); open(hf, 'w').write(K.html(body, tag, dark)); pg.goto('file://' + hf); pg.wait_for_timeout(300); pg.screenshot(path=f)
                lst.append((f, d)); n += 1; total += d
        b.close()
    with open(os.path.join(OUT, 'list.txt'), 'w') as fh:
        for f, d in lst: fh.write(f"file '{f}'\nduration {d}\n")
        fh.write(f"file '{lst[-1][0]}'\n")
    print(n, 'langkah,', total, 's')
