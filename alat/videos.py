from engine import *

C = 307  # x tengah untuk watak 620px
WARM = 'linear-gradient(180deg,#FCEFC7,#FFF6E5)'
BLUE = 'linear-gradient(180deg,#BFE6F7,#FFF6E5)'
RED = 'linear-gradient(180deg,#FBE1DD,#FFF6E5)'
GREEN = 'linear-gradient(180deg,#E4F3D6,#FFF6E5)'
GOLD = 'linear-gradient(180deg,#FFE9A3,#FFF6E5)'
NIGHT = 'linear-gradient(180deg,#2B3A55,#5A6B8C)'

V = {}

# ---------- V1: Group WhatsApp Tunas ----------
V['v1-group-whatsapp-tunas'] = page([
    cap(0, 4, 'Ini Tunas. 🌱'),
    ch(0.2, 4, 'T_thumb', C, 820),
    bub(1.4, 4, 'Tahun ni saya<br>nak kaya cepat! 💸', 160, 470),
    cap(4, 11, 'Group WhatsApp Tunas:'),
    ch(4, 11, 'T_shock', C, 1260, 560, 'pop', 'shake'),
    ntf(4.3, 11, 'GROUP FAMILY 🔥', 'BELI SEKARANG!! Confirm naik 🚀🚀', 380),
    ntf(5.4, 11, 'ABANG IPAR', 'Emas pasti naik, percayalah 😎', 560),
    ntf(6.5, 11, 'KAWAN SEKOLAH', 'Ada "signal VIP" RM99 je 🤫', 740),
    ntf(7.6, 11, 'GROUP KEDAI KOPI', 'Coin baru! Esok 10x!! 🌕', 920),
    ntf(8.6, 11, 'MAK SAUDARA', 'Skim untung 3% sebulan, dijamin ✨', 1100),
    emo(9.4, 11, '📱💥', 620, 1230, 170, 'pop', 'shake'),
    cap(11, 17, 'Tunas pun ikut...<br>SEMUA. 😵‍💫'),
    ch(11, 17, 'T_cemas', C, 1180, 600, 'pop', 'shake'),
    item(11.3, 17, '<svg width="900" height="520" viewBox="0 0 900 520"><path data-draw="2.4" d="M20 70 L140 110 L240 90 L340 190 L460 230 L560 340 L700 380 L880 480" fill="none" stroke="#D0533F" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/></svg>',
         'left:90px;top:440px', '', 'fade'),
    big(13.6, 17, 'Aduhhh 😭', 1000, 110, '#D0533F', 'pop', 'shake'),
    cap(17, 23, 'Lalu datang geng dia...'),
    ch(17, 23, 'P_ajar', -30, 1180, 560, 'left'),
    bub(17.6, 23, 'Bro... tip tu<br>bukan ilmu. 😅', 60, 500, 560),
    ch(18.8, 23, 'K_tunggu', 610, 1180, 560, 'right'),
    bub(19.6, 23, 'Faham dulu,<br>baru buat keputusan.', 400, 800, 620),
    emo(21.0, 23, '💡', 470, 1050, 160, 'pop', 'pulse'),
] + ending(23), [[0, WARM], [4, BLUE], [11, RED], [17, GREEN], [23, WARM]])

# ---------- V2: Tunas & 10 rantai emas ----------
NECK = '<svg width="420" height="260" viewBox="0 0 420 260">' + ''.join(f'<path d="M{40+i*12} {30+i*8} Q 210 {200+i*28} {380-i*12} {30+i*8}" fill="none" stroke="{c}" stroke-width="14" stroke-dasharray="2 16" stroke-linecap="round"/>' for i, c in enumerate(['#F5C04A','#E0A21B','#FFD95A'])) + '</svg>'
V['v2-tunas-rantai-emas'] = page([
    cap(0, 5.5, 'Tunas dengar:<br>"Emas PASTI naik!" ✨'),
    ch(0.2, 5.5, 'T_thumb', C, 860),
    item(1.6, 5.5, NECK, 'left:330px;top:1150px', '', 'drop', 'pulse'),
    bub(2.8, 5.5, 'Saya beli<br>10 rantai! 🤩', 560, 560, 460),
    cap(5.5, 12, 'Seminggu kemudian,<br>nak jual balik...'),
    item(5.8, 12, '<h3>KEDAI EMAS CAHAYA<br><span style="font-size:34px">(rekaan)</span></h3><div class="r"><span>Kedai jual</span><span>RM400/g</span></div><div class="r" style="color:#F5C04A"><span>Kedai beli balik</span><span>RM380/g</span></div>',
         'left:90px;right:90px;top:500px', 'board', 'drop'),
    ch(6.8, 12, 'T_shock', C, 1220, 580, 'pop', 'shake'),
    bub(7.6, 12, 'HAH?! Kenapa<br>harga lain? 🤯', 120, 1080, 520),
    cap(12, 18.5, 'Tambah upah lagi... 😭'),
    item(12.3, 18.5, '<div style="font-size:54px">Bayar</div><div class="n" style="font-size:150px"></div>', 'left:0;right:0;top:480px', 'big', 'pop', '', '0|4000|1|RM'),
    item(14.0, 18.5, '<div style="font-size:54px;color:#D0533F">Dapat balik</div><div class="n" style="font-size:150px;color:#D0533F"></div>', 'left:0;right:0;top:820px', 'big', 'pop', '', '4000|3300|1.6|RM'),
    emo(14.2, 18.5, '🪙', 200, 1180, 120, 'fade', 'fall'), emo(14.6, 18.5, '🪙', 480, 1180, 120, 'fade', 'fall'), emo(15.0, 18.5, '🪙', 760, 1180, 120, 'fade', 'fall'),
    ch(15.6, 18.5, 'T_cemas', C, 1240, 560, 'pop', 'shake'),
    cap(18.5, 24.5, 'Kuntum & Pucuk datang 🦸'),
    ch(18.5, 24.5, 'K_kalk', -20, 1180, 580, 'left'),
    bub(19.1, 24.5, 'Tanya DUA harga:<br>jual & beli balik.', 60, 500, 600),
    ch(20.3, 24.5, 'P_ajar', 610, 1180, 580, 'right'),
    bub(21.1, 24.5, 'Emas untuk simpan,<br>bukan cepat kaya. 🪙', 360, 820, 660),
] + ending(24.5), [[0, GOLD], [5.5, NIGHT], [12, RED], [18.5, GREEN], [24.5, WARM]])

# ---------- V3: Pakar 5 minit ----------
SPAG = ''.join(f'<path data-draw="1.2" data-dl="{0.25*i}" d="M20 {300+((i*53)%180)-90} C 200 {80+i*37 % 400}, 420 {460-(i*61)%380}, 600 {120+(i*29)%360} S 820 {420-(i*47)%300}, 880 {200+(i*71)%260}" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round"/>'
               for i, c in enumerate(['#D9940F','#2E78C2','#7A4FB5','#C2477A','#3E9A57','#D0533F','#2E9A93','#8E6CC0']))
CANDLES = ''.join(f'<rect x="{40+i*70}" y="{y}" width="40" height="{h}" fill="{"#3E9A57" if u else "#D0533F"}"/><line x1="{60+i*70}" x2="{60+i*70}" y1="{y-30}" y2="{y+h+30}" stroke="#3B2A1A" stroke-width="5"/>'
                  for i, (y, h, u) in enumerate([(280,90,1),(240,70,1),(260,110,0),(200,80,1),(170,60,1),(210,120,0),(190,70,1),(150,90,1),(120,60,1),(160,110,0),(130,70,1),(100,80,1)]))
V['v3-pakar-5-minit'] = page([
    cap(0, 5, 'Tunas tengok video<br>trading 5 minit... 📱'),
    ch(0.2, 5, 'T_phone', C, 1000),
    item(0.6, 5, '<div style="background:#3B2A1A;border-radius:20px;height:40px;width:820px;overflow:hidden"><div class="bar" style="height:100%;width:100%;background:#D4574B;transform-origin:left;"></div></div>', 'left:130px;top:620px', '', 'fade'),
    big(1.0, 5, '⏱ 5:00', 700, 90, '#3B2A1A', 'pop', 'pulse'),
    cap(5, 11, '...terus rasa<br>jadi PAKAR 😎'),
    ch(5, 11, 'T_thumb', C, 900, 640, 'pop', 'wig'),
    emo(5.4, 11, '🕶️', 420, 960, 200, 'drop', ''),
    bub(6.6, 11, 'Saya dah faham<br>SEMUA indikator! 💪', 160, 560, 760),
    cap(11, 17.5, 'Carta Tunas: 🍝'),
    item(11, 17.5, f'<svg width="900" height="520" viewBox="0 0 900 520" style="background:#fff;border:6px solid #3B2A1A;border-radius:30px">{CANDLES}{SPAG}</svg>', 'left:90px;top:440px', '', 'pop'),
    ch(13.4, 17.5, 'K_fikir', C, 1100, 600, 'up', 'wig'),
    bub(14.4, 17.5, 'Ni carta...<br>atau mi goreng? 🤔', 300, 1000, 640),
    cap(17.5, 24, 'Pucuk: "Satu lilin dulu, bro." 🕯️'),
    item(17.8, 24, '<svg width="520" height="620" viewBox="0 0 520 620"><line x1="200" x2="200" y1="20" y2="600" stroke="#3B2A1A" stroke-width="10"/><rect x="130" y="140" width="140" height="300" fill="#3E9A57" stroke="#3B2A1A" stroke-width="8"/></svg>',
         'left:120px;top:520px', '', 'pop'),
    item(18.6, 24, '← TINGGI', 'left:440px;top:505px;font-size:58px', 'big', 'right'),
    item(19.0, 24, '← TUTUP', 'left:440px;top:625px;font-size:58px;color:#3E9A57', 'big', 'right'),
    item(19.4, 24, '← BUKA', 'left:440px;top:925px;font-size:58px;color:#3E9A57', 'big', 'right'),
    item(19.8, 24, '← RENDAH', 'left:440px;top:1085px;font-size:58px', 'big', 'right'),
    ch(20.0, 24, 'P_ajar', 600, 1250, 560, 'right'),
    bub(20.8, 24, 'Kenal 4 harga ni,<br>carta jadi kawan. 😉', 60, 1240, 580),
] + ending(24), [[0, NIGHT], [5, GOLD], [11, BLUE], [17.5, GREEN], [24, WARM]])

if __name__ == '__main__':
    os.makedirs('html', exist_ok=True); os.makedirs('out', exist_ok=True)
    for k, h in V.items():
        # bar 5 minit: animasi khas melalui render
        h = h.replace('window.render=t=>{', "window.render=t=>{const bb=document.querySelector('.bar');if(bb)bb.style.transform=`scaleX(${Math.min(1,t/4.2)})`;", 1)
        open(f'html/{k}.html', 'w').write(h)
    print(list(V))
