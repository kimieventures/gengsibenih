# EP06 · Bab 1/6 "Tambah modal bila rugi" (emosi, bukan ilmu). python3 ep06.py [--still] [--render]
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from dcks import *
JADUAL = ('<div class="tag">MATEMATIK RUGI</div><div style="font-size:54px;line-height:1.8">Turun <em>20%</em> → perlu naik <b style="color:#ff8a4c">25%</b><br>'
          'Turun <em>50%</em> → perlu naik <b style="color:#ff5a4e">100%</b></div>')
SOALAN = '<div class="tag">TANYA DIRI SENDIRI</div><div style="font-size:60px;line-height:1.3">"Kalau hari ni aku <em>tak pegang</em> saham ni,<br>aku nak beli tak?"</div><div style="font-size:46px;margin-top:20px;color:#9fb2ab">Tak? Jangan tambah.</div>'
EP = dict(nama='ep06', slug='tambah-modal-bila-rugi', bab='1/6', jeda={5: 0.4, 8: 0.3, 10: 0.4, 12: 0.3},
  seterusnya='ulang tonton *EP01: Terlepas Bas* 🚌',
  baris=[
  ('N', 'Saham aku turun dua puluh peratus. Aku nak tambah modal, purata kos jadi murah!',
   dict(b=('rumah', '😩', ''), prop='📉', j='Turun *20%*…<br>*tambah* lagi?', jt=230, punch='tambah', rx=[('murah', '🛒', 820, 620, 140, 'pop')])),
  ('D', 'Itu namanya kejar rugi. Ramai hilang lebih banyak sebab langkah ni.',
   dict(b=('rumah', '😩', '🤖'), tg='Kenapa? <b>Tengok sampai habis.</b>', tgw='ramai')),
  ('N', 'Tapi semua orang cakap, beli masa murah!',
   dict(b=('rumah', '😤', '🤖'), j='"Beli masa *murah*!"', jt=260)),
  ('D', 'Murah tak sama dengan bagus. Kedai nak tutup pun jual murah.',
   dict(punch='tutup', rx=[('tutup', '🏚️🏷️', 360, 540, 140, 'boing')])),
  ('N', 'Hahaha. Macam kedai kasut depan rumah aku. Sale tiga tahun.',
   dict(b=('pasar', '😂', '🤖'), punch='tahun', rx=[('kasut', '👟', 360, 540, 140, 'pop'), ('tahun', '🦗 krik… krik…', 330, 1210, 44, 'krik', 0.6)])),
  ('D', 'Bayangkan. Turun dua puluh peratus, perlu naik dua puluh lima untuk pulang modal. Turun lima puluh, perlu naik seratus.',
   dict(kad=JADUAL)),
  ('N', 'Seratus peratus?! Itu macam nak kurus lima kilo lepas raya.',
   dict(b=('rumah', '😱', '🤖'), punch='raya', rx=[('raya', '🍗🍰', 330, 540, 140, 'boing')])),
  ('D', 'Tepat. Senang naik, susah turun. Eh, terbalik.',
   dict(punch='terbalik', rx=[('terbalik', '🔄', 860, 600, 130, 'whoosh')], tg='Tapi tunggu… ada *satu soalan* penting', tgw='akhir')),
  ('N', 'Habis tu apa aku patut buat?',
   dict(b=('rumah', '🤔', '🤖'))),
  ('D', 'Tanya satu soalan. Kalau hari ni saya tak pegang saham ni, adakah saya akan beli? Kalau tak, jangan tambah.',
   dict(kad=SOALAN)),
  ('N', 'Soalan terakhir. Kenapa susah sangat nak lepaskan?',
   dict(q='Kenapa susah sangat<br>nak *lepaskan*?')),
  ('D', 'Sebab otak benci rasa rugi. Tambah modal rasa macam melawan. Tapi keputusan baik ikut peraturan, bukan ego.',
   dict(a=[('Otak benci rasa rugi', 'otak'), ('Tambah modal = lawan ego', 'tambah'), ('Ikut peraturan, bukan ego', 'keputusan')])),
  ('N', 'Okay. Ego aku pun dah turun dua puluh peratus.',
   dict(b=('rumah', '😌', '🤖'), punch='ego')),
  ('D', 'Yang tu, tak payah tambah.',
   dict(punch='tambah', rx=[('tambah', '🕶️', 672, 755, 175, 'whoosh')])),
  ])
buat(EP)
