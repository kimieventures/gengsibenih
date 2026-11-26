# EP04 · Bab 4/6 "Butang kecemasan" (urus risiko macam robot). python3 ep04.py [--still] [--render]
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from dcks import *
EP = dict(nama='ep04', slug='butang-kecemasan', bab='4/6', jeda={5: 0.4, 9: 0.3, 11: 0.4, 13: 0.3},
  seterusnya='*scam* yang janji 30% sebulan 🚩',
  baris=[
  ('N', 'Akaun aku turun sepuluh peratus! Robot, kau tak panik ke?',
   dict(b=('rumah', '😰', ''), prop='📉', j='Akaun turun *10%*!', jt=230, punch='panik', rx=[('panik', '😱', 820, 620, 150, 'boing')])),
  ('D', 'Tak. Sebab saya dah tulis apa nak buat, sebelum benda ni jadi.',
   dict(b=('rumah', '😰', '🤖'), tg='Rahsia robot? <b>Tengok sampai habis.</b>', tgw='tulis')),
  ('N', 'Aku ada idea! Kita gandakan modal. Bila naik balik, terus untung!',
   dict(b=('rumah', '😤', '🤖'), prop='💰✖️2', j='*Gandakan* modal!', jt=260, punch='gandakan')),
  ('D', 'Itu namanya martingale. Macam main guna duit dapur, sebab nak kejar kalah.',
   dict(punch='martingale', rx=[('martingale', '🚫', 380, 540, 160, 'boing')])),
  ('N', 'Duit dapur? Kalau mak aku tahu, aku kena basuh pinggan sebulan.',
   dict(b=('rumah', '😳', '🤖'), punch='pinggan', rx=[('pinggan', '🍽️🧽', 330, 540, 140, 'boing')])),
  ('D', 'Peraturan saya: setiap posisi saiz tetap. Tanpa pinjaman. Kalau akaun jatuh lima belas peratus, saya berhenti.',
   dict(kad=stat('Had rugi akaun', '15%', 'kemudian robot <em>BERHENTI</em>', 'BUTANG KECEMASAN'), rx=[('berhenti', '🚨', 820, 1080, 120, 'ding')])),
  ('N', 'Berhenti? Macam kalah awal la.',
   dict(b=('rumah', '🤨', '🤖'), j='Berhenti = *kalah*?', jt=260)),
  ('D', 'Macam fius rumah. Dia putus, supaya rumah tak terbakar.',
   dict(prop='⚡🏠', punch='putus', rx=[('putus', '⚡', 470, 420, 150, 'whoosh')])),
  ('N', 'Patutlah fius rumah aku selalu putus. Aircond tiga bilik.',
   dict(b=('rumah', '😅', '🤖'), punch='aircond', rx=[('aircond', '🥵❄️', 330, 540, 140, 'boing')], tg='Tapi tunggu… kenapa *tanpa pinjaman*?', tgw='akhir')),
  ('N', 'Kenapa tak boleh pinjam? Untung lagi besar kan?',
   dict(b=('rumah', '🤔', '🤖'))),
  ('D', 'Rugi pun lagi besar. Akaun kecil yang hidup, lebih baik dari akaun besar yang mati.',
   dict(kad=stat('Pinjam 2 kali ganda', '2×', 'untung <em>DAN</em> rugi', 'MARGIN'))),
  ('N', 'Soalan terakhir. Kenapa robot tak takut rugi?',
   dict(q='Kenapa robot *tak takut* rugi?')),
  ('D', 'Sebab saiz tetap kecil. Had rugi dah ditulis awal. Dan tiada hutang yang mengejar.',
   dict(a=[('Saiz tetap, kecil', 'saiz'), ('Had rugi ditulis awal', 'had'), ('Tiada hutang mengejar', 'tiada')])),
  ('N', 'Okay. Malam ni aku boleh tidur lena.',
   dict(b=('rumah', '😌', '🤖'), prop='🛏️')),
  ('D', 'Saya pun. Robot pun perlu tidur.',
   dict(punch='tidur', rx=[('tidur', '💤', 860, 600, 130, 'pop')])),
  ])
buat(EP)
