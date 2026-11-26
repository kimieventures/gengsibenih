# EP02 · Bab 2/6 "Bila nak KELUAR?" (dari indikator ke keputusan). python3 ep02.py [--still t..] [--render]
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from dcks import *

EP = dict(nama='ep02', slug='bila-nak-keluar', bab='2/6', jeda={4: 0.9, 8: 0.3, 11: 0.4, 13: 0.3},
  seterusnya='strategi yang robot ni *BUANG* dalam tong sampah 🗑️',
  baris=[
  ('N', 'Saham aku dah turun sepuluh peratus! Kenapa robot ni dah jual awal-awal?',
   dict(b=('rumah', '😭', ''), prop='📉', j='Turun *10%*…<br>robot dah *JUAL* awal?!', jt=230, punch='jual', rx=[('jual', '💢', 820, 620, 150, 'boing')])),
  ('D', 'Sebab harga tutup bawah purata dua ratus hari. Itu isyarat keluar saya.',
   dict(b=('rumah', '😭', '🤖'), tg='Siapa betul? <b>Tengok sampai habis.</b>', tgw='isyarat')),
  ('N', 'Aku ni diamond hand! Hold sampai kiamat!',
   dict(b=('rumah', '😤', '🤖'), prop='💎🙌', j='"Hold sampai *kiamat*!"', jt=260, punch='kiamat')),
  ('D', 'Diamond hand awak dah cair. Jadi ais batu.',
   dict(punch='ais', rx=[('ais', '🧊', 380, 560, 160, 'boing'), ('batu', '🥶', 160, 560, 140, 'pop')])),
  ('D', 'Tengok ni. Harga turun, kena garis biru, saya keluar. Lepas tu jatuh lagi sepuluh peratus.',
   dict(kad=chart_keluar('CONTOH SEJARAH · ILUSTRASI'), rx=[('keluar', '✂️', 820, 1060, 110, 'whoosh')])),
  ('N', 'Tapi kalau esok naik balik, kau tak menyesal ke?',
   dict(b=('kereta', '🤨', '🤖'), j='Kalau esok *naik balik*?', jt=260)),
  ('D', 'Macam GPS. Salah simpang, dia tak menangis. Dia cuma cakap: recalculating.',
   dict(prop='🗺️', punch='recalculating', rx=[('recalculating', '🔄', 470, 420, 150, 'whoosh')], tg='"Recalculating…" 🛰️', tgw='recalculating')),
  ('N', 'Hahaha. GPS aku haritu suruh masuk sawah.',
   dict(b=('kereta', '😂', '🤖'), punch='sawah', rx=[('sawah', '🌾🚗', 360, 430, 150, 'boing'), ('sawah', '🦗 krik… krik…', 330, 1210, 44, 'krik', 0.9)])),
  ('D', 'Sebab tu peraturan kena diuji dulu. Bukan ikut GPS rosak.',
   dict(b=('kereta', '😅', '🤖'), j='Peraturan kena *diuji* dulu', jt=260, tg='Tapi tunggu… bila nak *MASUK* balik?', tgw='akhir')),
  ('N', 'Okay. Jadi bila nak masuk balik?',
   dict(b=('rumah', '🤔', '🤖'))),
  ('D', 'Bila harga tutup semula atas garis tu. Mungkin terlepas sikit naik awal, tapi elak jatuh besar.',
   dict(kad=pie(10, 'terlepas naik awal', 'elak jatuh besar', 'PERTUKARAN · CONTOH SAHAJA'))),
  ('N', 'Soalan terakhir. Kalau keluar terlalu awal, bukan rugi ke?',
   dict(q='Kalau keluar *terlalu awal*,<br>bukan rugi ke?')),
  ('D', 'Keluar bukan kalah. Rugi kecil boleh dikejar. Rugi besar susah nak bangun. Peraturan buat keputusan masa hati panas.',
   dict(a=[('Keluar ≠ kalah', 'keluar'), ('Rugi kecil boleh dikejar', 'rugi'), ('Peraturan sejuk masa hati panas', 'peraturan')])),
  ('N', 'Fuh. Aku nak pasang GPS dalam portfolio aku.',
   dict(b=('rumah', '🤩', '🤖'), prop='🛰️', j='GPS untuk *portfolio*', jt=260)),
  ('D', 'Pasang. Tapi jangan masuk sawah.',
   dict(punch='sawah', rx=[('sawah', '🌾', 860, 600, 130, 'pop'), ('jangan', '🕶️', 672, 755, 175, 'whoosh')])),
  ])
buat(EP)
