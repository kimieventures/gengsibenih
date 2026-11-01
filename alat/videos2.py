from engine import *
from videos import C, WARM, BLUE, RED, GREEN, GOLD, NIGHT
V = {}

# ---------- V4: Gaji masuk, gaji hilang ----------
V['v4-gaji-hilang-3-hari'] = page([
    cap(0, 5, 'Hari gaji! 🎉'),
    ch(0.2, 5, 'T_thumb', C, 900, 640, 'pop', 'wig'),
    item(0.6, 5, '<div style="font-size:54px">Baki akaun</div><div class="n" style="font-size:150px;color:#3E9A57"></div>', 'left:0;right:0;top:420px', 'big', 'pop', '', '0|3000|1.2|RM'),
    cap(5, 13, 'Hari 1... Hari 2... Hari 3...'),
    ntf(5.3, 13, 'KEDAI KOPI ☕', 'Kopi sejuk + kek: −RM28', 380),
    ntf(6.4, 13, 'PESANAN DALAM TALIAN 🛒', 'Kasut "flash sale": −RM259', 560),
    ntf(7.5, 13, 'PENGHANTARAN MAKANAN 🍔', 'Makan malam 3 hari: −RM96', 740),
    ntf(8.6, 13, 'LANGGANAN 📺', '4 aplikasi tonton: −RM70', 920),
    item(9.8, 13, '<div style="font-size:54px">Baki akaun</div><div class="n" style="font-size:150px;color:#D0533F"></div>', 'left:0;right:0;top:1110px', 'big', 'pop', '', '3000|42|1.8|RM'),
    ch(10.6, 13, 'T_shock', C, 1400, 480, 'pop', 'shake'),
    cap(13, 19, 'Tunas: "Mana duit saya pergi?!" 😭'),
    ch(13, 19, 'T_cemas', C, 1150, 620, 'pop', 'shake'),
    emo(13.4, 19, '💸', 160, 500, 150, 'fade', 'fall'), emo(13.8, 19, '💸', 460, 450, 150, 'fade', 'fall'), emo(14.2, 19, '💸', 760, 520, 150, 'fade', 'fall'),
    cap(19, 25, 'Kuntum ada petua 🌸'),
    ch(19, 25, 'K_kalk', -20, 1180, 580, 'left'),
    bub(19.6, 25, 'Bila gaji masuk,<br>asingkan simpanan DULU.', 60, 480, 640),
    ch(20.8, 25, 'P_ajar', 610, 1180, 580, 'right'),
    bub(21.6, 25, 'Belanja guna<br>yang tinggal. 😉', 380, 820, 600),
] + ending(25), [[0, GOLD], [5, BLUE], [13, RED], [19, GREEN], [25, WARM]])

# ---------- V5: Panggilan "bank" ----------
CALL = ('<div style="background:#1C1C1E;border-radius:60px;border:8px solid #3B2A1A;padding:60px 40px;color:#fff;text-align:center;width:640px">'
        '<div style="font-size:40px;color:#aaa">Panggilan masuk...</div><div style="font-size:66px;margin:20px 0">📞 "Pegawai Bank"</div>'
        '<div style="font-size:36px;color:#aaa">Nombor tidak dikenali</div>'
        '<div style="display:flex;justify-content:space-around;margin-top:50px;font-size:90px"><span>🔴</span><span>🟢</span></div></div>')
V['v5-panggilan-pegawai-bank'] = page([
    cap(0, 5, 'Tunas tengah santai... 😌'),
    ch(0.2, 5, 'T_idea', C, 1000),
    item(2.2, 5, CALL, 'left:220px;top:420px', '', 'drop', 'shake'),
    cap(5, 12, '"Akaun encik dibekukan!<br>Bagi kod OTP sekarang!" 😱'),
    ch(5, 12, 'T_phone', C, 1150, 620, 'pop', 'shake'),
    bub(5.6, 12, 'Cepat! Dalam<br>5 minit je! ⏰', 80, 560, 520, bg='#FBE1DD'),
    bub(7.4, 12, 'Ok ok... kodnya...', 520, 820, 480),
    cap(12, 18, 'TUNGGU!! ✋'),
    ch(12, 18, 'K_perisai', C, 1050, 680, 'pop', 'pulse'),
    big(12.5, 18, '🚫 OTP', 560, 150, '#D0533F', 'pop', 'shake'),
    cap(18, 25, 'Kuntum: 3 peraturan emas 🛡️'),
    item(18.3, 25, '1️⃣ Bank TAK akan minta OTP', 'left:80px;right:80px;top:440px;font-size:56px', 'bub', 'left'),
    item(19.3, 25, '2️⃣ Letak telefon, telefon bank sendiri', 'left:80px;right:80px;top:640px;font-size:56px', 'bub', 'left'),
    item(20.3, 25, '3️⃣ Tertipu? NSRC 997 segera', 'left:80px;right:80px;top:880px;font-size:56px', 'bub', 'left'),
    ch(21.0, 25, 'T_idea', C, 1150, 600, 'up', 'bob'),
] + ending(25), [[0, BLUE], [5, NIGHT], [12, RED], [18, GREEN], [25, WARM]])

# ---------- V6: Jutawan dalam sebulan ----------
V['v6-jutawan-sebulan'] = page([
    cap(0, 6, 'Tunas ada "formula" baru 🧠'),
    ch(0.2, 6, 'T_idea', C, 1000),
    bub(1.4, 6, 'Modal RM1,000, untung<br>10% SEHARI... mesti kaya! 🤑', 120, 520, 840),
    cap(6, 13, 'Kira jom... 🧮'),
    item(6.3, 13, '<div style="font-size:54px;color:#FCEFC7">Selepas 30 hari (atas kertas)</div><div class="n" style="font-size:140px;color:#7CE08A"></div>', 'left:0;right:0;top:420px', 'big', 'pop', '', '1000|17449|4|RM'),
    ch(7.0, 13, 'T_thumb', C, 1150, 620, 'pop', 'wig'),
    emo(8.5, 13, '🚀', 760, 1000, 160, 'pop', 'shake'),
    cap(13, 19, 'Pucuk & Kuntum: "Hmm... 🤨"'),
    ch(13, 19, 'P_silang', -20, 1180, 580, 'left'),
    ch(13.4, 19, 'K_fikir', 610, 1180, 580, 'right'),
    bub(14.0, 19, 'Siapa janji 10%<br>SEHARI?', 100, 500, 560),
    bub(15.6, 19, 'Itu bukan pelaburan.<br>Itu tanda merah! 🚩', 380, 820, 620, bg='#FBE1DD'),
    cap(19, 25, 'Tunas sedar... 😅'),
    ch(19, 25, 'T_cemas', C, 1150, 600, 'pop', 'shake'),
    item(19.4, 25, '🚩 Untung tetap "dijamin"<br>🚩 Desak cepat masuk<br>🚩 Bayar ke akaun peribadi', 'left:80px;right:80px;top:470px;font-size:58px;text-align:left;line-height:1.6', 'bub', 'pop'),
] + ending(25), [[0, GOLD], [6, NIGHT], [13, BLUE], [19, RED], [25, WARM]])

if __name__ == '__main__':
    os.makedirs('html', exist_ok=True); os.makedirs('out', exist_ok=True)
    for k, h in V.items(): open(f'html/{k}.html', 'w').write(h)
    print(list(V))
