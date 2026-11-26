# EP05 · Bab 6/6 "Kebal scam". python3 ep05.py [--still] [--render]
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from dcks import *
SEMAK = ('<div class="tag">KALAU DAH DAPAT MESEJ MACAM NI</div><div style="font-size:52px;line-height:1.7;text-align:left">❌ Jangan transfer apa-apa<br>'
         '🔎 Semak <em>Senarai Amaran Pelabur</em> SC<br>📞 Dah tertipu? <em>NSRC 997</em></div>')
EP = dict(nama='ep05', slug='kebal-scam', bab='6/6', jeda={4: 0.5, 9: 0.3, 10: 0.4, 12: 0.3},
  seterusnya='kenapa ramai *KALAH*: emosi, bukan ilmu 🎭',
  baris=[
  ('N', 'Ada orang mesej. Pelaburan untung tiga puluh peratus sebulan. Join cepat, slot terhad!',
   dict(b=('pejabat', '🤑', ''), prop='📲', j='*30%* sebulan?!', jt=230, punch='tiga', rx=[('terhad', '⏰', 820, 620, 140, 'pop')])),
  ('D', 'Saya robot. Saya pun tak berani janji untung.',
   dict(b=('pejabat', '🤑', '🤖'), tg='Siapa betul? <b>Tengok sampai habis.</b>', tgw='janji')),
  ('N', 'Dia siap ada screenshot untung. Testimoni pun banyak!',
   dict(b=('pejabat', '😍', '🤖'), prop='🖼️💯', j='Ada *screenshot* untung!', jt=260)),
  ('D', 'Screenshot boleh edit. Testimoni boleh beli. Saya pun boleh buat dalam lima saat.',
   dict(punch='lima', rx=[('edit', '✏️', 380, 540, 140, 'whoosh'), ('lima', '⏱️', 860, 600, 120, 'pop')])),
  ('N', 'Seriuslah?',
   dict(b=('pejabat', '😨', '🤖'), punch='seriuslah', rx=[('seriuslah', '😱', 360, 540, 150, 'boing')])),
  ('D', 'Tiga puluh peratus sebulan. Seribu ringgit dalam setahun jadi dua puluh tiga ribu. Pelabur terbaik dunia pun tak buat macam tu.',
   dict(kad=stat('RM1,000 · 30% sebulan · 12 bulan', 'RM0', 'tak masuk akal 🤯', 'KIRA SENDIRI'), bx='0|23298|1.8|RM')),
  ('N', 'Habis tu macam mana aku nak tahu dia scam?',
   dict(b=('rumah', '🤔', '🤖'))),
  ('D', 'Tiga bendera merah. Janji untung tetap. Desak cepat. Dan minta pindah ke akaun peribadi.',
   dict(prop='🚩', j='*3* bendera merah', jt=260, rx=[('desak', '🚩', 380, 420, 130, 'pop'), ('pindah', '🚩', 560, 420, 130, 'pop')])),
  ('N', 'Alamak. Semalam aku dah balas: berminat bos.',
   dict(b=('rumah', '😅', '🤖'), punch='bos', rx=[('bos', '🦗 krik… krik…', 330, 1210, 44, 'krik', 0.6)], tg='Tapi tunggu… *apa nak buat* sekarang?', tgw='akhir')),
  ('D', 'Jangan transfer apa-apa. Semak senarai amaran pelabur Suruhanjaya Sekuriti. Kalau dah tertipu, telefon NSRC sembilan sembilan tujuh.',
   dict(kad=SEMAK)),
  ('N', 'Soalan terakhir. Kenapa orang bijak pun boleh kena?',
   dict(q='Kenapa orang *bijak* pun<br>boleh kena scam?')),
  ('D', 'Sebab scam jual perasaan, bukan nombor. Desakan matikan otak. Dan untung tetap memang tak wujud.',
   dict(a=[('Scam jual perasaan', 'scam'), ('Desakan matikan otak', 'desakan'), ('Untung tetap tak wujud', 'untung')])),
  ('N', 'Okay. Aku nak balas dia sekarang.',
   dict(b=('rumah', '😤', '🤖'), prop='📲')),
  ('D', 'Balas apa?', dict()),
  ('N', 'Maaf bos. Robot aku cakap tak.',
   dict(b=('rumah', '😎', '🤖'), punch='robot', rx=[('tak', '🤖👍', 820, 560, 120, 'ding')])),
  ])
buat(EP)
