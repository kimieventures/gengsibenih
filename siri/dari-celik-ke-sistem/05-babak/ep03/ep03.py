# EP03 · Bab 3/6 "Strategi yang dibuang" (backtest gagal sebab kos). python3 ep03.py [--still] [--render]
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from dcks import *
LANGKAH = '<div class="tag">UJI DULU · 3 LANGKAH</div><div style="font-size:54px;line-height:1.7;text-align:left">1 📚 Uji dengan data lama<br>2 🧮 Kira <em>semua</em> kos<br>3 🪙 Cuba duit kecil</div>'
EP = dict(nama='ep03', slug='strategi-dibuang', bab='3/6', jeda={3: 0.7, 9: 0.3, 11: 0.4, 13: 0.3},
  seterusnya='robot ni ada *BUTANG KECEMASAN* 🚨',
  baris=[
  ('N', 'Aku jumpa strategi day trade. Untung setiap hari! Video tu cakap senang je.',
   dict(b=('pejabat', '🤑', ''), prop='📱', j='Untung *setiap hari*?!', jt=230, punch='untung', rx=[('senang', '💸', 820, 620, 150, 'pop')])),
  ('D', 'Saya dah uji strategi macam tu. Lima tahun data. Hasilnya...',
   dict(b=('pejabat', '🤑', '🤖'), tg='Hasilnya? <b>Tengok sampai habis.</b>', tgw='hasilnya')),
  ('N', 'Mesti kaya kan? Kan? Kan?',
   dict(b=('pejabat', '😍', '🤖'), punch='kaya', rx=[('kaya', '💰', 380, 540, 150, 'pop')])),
  ('D', 'Rugi.',
   dict(b=('pejabat', '😶', '🤖'), punch='rugi', rx=[('rugi', '🦗 krik… krik…', 330, 1210, 44, 'krik', 0.4)])),
  ('D', 'Untung kasar ada. Tapi bila tolak yuran broker, cukai, dan beza harga beli jual, terus jadi merah.',
   dict(kad=chart_kos('CONTOH SAHAJA · 100 DAGANGAN'))),
  ('N', 'Yuran tu kecil je kot. Seringgit dua.',
   dict(b=('mamak', '🤨', '🤖'), j='Kecil je kot…', jt=260)),
  ('D', 'Kecil, tapi seratus kali sebulan. Macam teh tarik setiap hari. Tahu tahu dah seribu setahun.',
   dict(prop='🧋', punch='seribu', rx=[('seribu', '💸💸', 400, 420, 140, 'boing')])),
  ('N', 'Aduh. Teh tarik aku pun kena audit.',
   dict(b=('mamak', '😅', '🤖'), punch='audit', rx=[('audit', '🧾', 360, 540, 150, 'boing')])),
  ('D', 'Sebab tu kami buang strategi tu dalam tong sampah. Sebelum ia buang duit kita.',
   dict(j='Buang strategi, *bukan duit*', jt=260, rx=[('sampah', '🗑️', 860, 600, 140, 'whoosh')], tg='Tapi tunggu… macam mana nak *uji*?', tgw='akhir')),
  ('N', 'Macam mana nak tahu strategi tu bagus sebelum guna duit betul?',
   dict(b=('rumah', '🤔', '🤖'))),
  ('D', 'Uji dulu dengan data lama. Kira semua kos. Lepas tu cuba dengan duit kecil.',
   dict(kad=LANGKAH)),
  ('N', 'Soalan terakhir. Kenapa video guru trading tu nampak untung je?',
   dict(q='Kenapa video "guru trading"<br>nampak *untung je*?')),
  ('D', 'Sebab yang rugi tak masuk video. Untung kasar bukan untung bersih. Dan uji dulu, baru percaya.',
   dict(a=[('Yang rugi tak masuk video', 'yang'), ('Kasar ≠ bersih', 'kasar'), ('Uji dulu, baru percaya', 'uji')])),
  ('N', 'Jadi guru tu tak tipu. Cuma... edit.',
   dict(b=('rumah', '😏', '🤖'), punch='edit', rx=[('edit', '✂️🎬', 360, 540, 140, 'whoosh')])),
  ('D', 'Data tak edit.',
   dict(punch='edit', rx=[('data', '🕶️', 672, 755, 175, 'whoosh')])),
  ])
buat(EP)
