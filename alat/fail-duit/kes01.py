from scrapbook import *
e = Ep('fd1', {1: 0.2, 6: 0.2, 9: 0.5}); S, E, w, T = e.S, e.E, e.w, e.T
it = rangka(e, 1, 'Kosmo! Online · 5 Nov 2026', S[9])
it += [item(0, E[0], '<div class="sc"><div class="bar">📢 Ditaja · Pelaburan</div><div style="padding:30px;font-size:44px;line-height:1.3"><b>Untung saham harian!</b> 📈💰<br><br>Modal kecil, pulangan besar. Klik sekarang!</div></div>', 'left:300px;top:250px;transform:rotate(-4deg)', 'fon', 'none'),
       item(0, E[0], 'ILUSTRASI', 'left:620px;top:220px;transform:rotate(6deg)', 'lbl', 'none'),
       kad(0, E[0], f'<div style="text-align:center;font-family:Fredoka,sans-serif;font-size:120px;line-height:1">{hl("RM143,599", .1, .6)}</div><div style="text-align:center;font-size:64px;margin-top:10px">lesap. 💸</div>', 'left:120px;right:120px;top:780px;transform:rotate(2deg)', 'none')]
it += [kad(S[1], E[1], f'<b style="font-family:Nunito;font-size:30px;color:#C8473B">KOSMO! ONLINE · 5 NOV 2026</b><br>Penyelia syarikat {hl("rugi RM143,599.90", w(1, "seorang"))} ditipu pelaburan saham palsu', 'left:90px;right:90px;top:330px;transform:rotate(-2deg)', 'drop'),
       selo(S[1], E[1], 470, 300, -3),
       item(w(1, 'teluk'), E[1], '<div style="height:330px;width:470px;background:linear-gradient(160deg,#9BC6A2,#5C8F6B);display:flex;align-items:center;justify-content:center;font-size:150px">📍</div><p>Teluk Intan, Perak</p>', 'left:300px;top:760px;transform:rotate(3deg)', 'polar', 'pop'),
       item(w(1, 'laporan'), E[1], 'LAPORAN POLIS', 'left:110px;top:1180px;transform:rotate(-5deg)', 'lblk', 'pop')]
it += [item(S[2], E[2], '<div class="sc"><div class="bar">📢 Ditaja</div><div style="padding:30px;font-size:46px;line-height:1.3"><b>Pelaburan saham</b><br>untung setiap hari 📈</div></div>', 'left:90px;top:330px;transform:rotate(-5deg);height:620px', 'fon', 'left'),
       kad(w(2, 'tertarik'), E[2], f'"…{hl("tertarik dengan iklan pelaburan saham", w(2, "iklan"))} yang dipaparkan di media sosial."<small>Petikan laporan polis (Kosmo!)</small>', 'left:440px;width:580px;top:600px;font-size:44px;transform:rotate(3deg)', 'right')]
it += [item(S[3], E[3], '<div style="background:#fff;border:5px solid #2B2116;border-radius:36px 36px 36px 8px;padding:26px 34px;font-size:48px;box-shadow:6px 8px 0 #2B2116">Hai! Saya ejen pelaburan 😊<br>Boleh bantu awak untung.</div>', 'left:110px;top:430px;width:760px', '', 'pop'),
       emo(S[3], E[3], '🕴️', 720, 720, 260, 'pop', 'bob'), item(w(3, 'mengaku'), E[3], 'MENGAKU ✋', 'left:180px;top:880px;transform:rotate(-6deg)', 'lblk', 'pop', 'pulse')]
chart = '<svg width="400" height="300" viewBox="0 0 400 300"><path data-draw="1.6" d="M10 270 L70 240 L120 250 L180 180 L230 190 L290 110 L340 90 L390 20" fill="none" stroke="#2E9E55" stroke-width="12" stroke-linecap="round"/></svg>'
it += [item(S[4], E[4], f'<div class="sc"><div class="bar" style="background:#1F7A4D">📲 AppPelaburan</div><div style="padding:24px;text-align:center"><div style="font-size:30px;color:#666">Keuntungan anda</div><div style="font-size:70px;font-weight:900;color:#1F7A4D" class="n">+RM0</div>{chart}</div></div>', 'left:300px;top:260px', 'fon', 'pop', bx='0|28400|3.5|+RM'),
       item(S[4], E[4], 'ILUSTRASI', 'left:110px;top:300px;transform:rotate(-6deg)', 'lbl', 'pop'),
       item(w(4, 'sangat'), E[4], 'TERLALU CANTIK? 🤨', 'left:90px;top:1150px;transform:rotate(-4deg);font-size:48px', 'lblk', 'pop', 'pulse')]
for k in range(3):
    it.append(item(S[5] + 0.5 + k * 1.1, E[5], f'PINDAHAN #{k+1}<br>Ke: akaun bank <b>individu ****{[3,7,1][k]}{[8,2,9][k]}</b>', f'left:{200 + k*20}px;top:{380 + k*210}px;transform:rotate({[-3,2,-1][k]}deg)', 'slip', 'right'))
it.append(item(w(5, 'suspek'), E[5], 'AKAUN YANG SUSPEK BAGI 🚩', 'left:150px;top:1080px;transform:rotate(-3deg)', 'lblk', 'pop', 'pulse'))
it += [kad(S[6], E[6], f'<div style="text-align:center"><div style="font-family:Nunito;font-size:40px;color:#5E4B37">JUMLAH DIPINDAHKAN</div><div style="font-family:Fredoka,sans-serif;font-size:118px">{hl("RM143,599.90", w(6, "lima"), 1.2)}</div></div>', 'left:90px;right:90px;top:500px;transform:rotate(-1.5deg)', 'pop')]
it += [item(S[7], E[7], '<div class="sc"><div class="bar" style="background:#1F7A4D">📲 AppPelaburan</div><div style="padding:40px 24px;text-align:center;font-size:40px">Baki: <b>RM171,999</b><br><br><div style="background:#1F7A4D;color:#fff;border-radius:18px;padding:22px">KELUARKAN WANG</div></div></div>', 'left:300px;top:260px', 'fon', 'pop'),
       item(w(7, 'modal'), E[7], 'GAGAL ❌', 'left:330px;top:760px;font-size:96px;background:#C8473B;color:#fff;transform:rotate(-8deg)', 'lblk', 'pop', 'shake'),
       item(S[7], E[7], 'ILUSTRASI', 'left:110px;top:300px;transform:rotate(-6deg)', 'lbl', 'none')]
it += [kad(S[8], E[8], '<b style="font-family:Nunito;font-size:32px;color:#5E4B37">KETUA POLIS PERAK</b><br>Siasatan di bawah Seksyen 420 Kanun Keseksaan.', 'left:110px;right:110px;top:350px;transform:rotate(2deg)', 'drop'),
       item(w(8, 'menipu'), E[8], '<div style="font-size:92px">SEKSYEN 420</div><div style="font-size:60px;color:#2B2116">MENIPU</div>', 'left:200px;right:200px;top:820px;transform:rotate(-7deg)', 'cop2', 'pop')]
it += [item(S[9] - .3, E[10], '📌 PENGAJARAN TUNAS', 'left:300px;top:250px;transform:rotate(-2deg)', 'lblk', 'pop'),
       ch(S[9], E[9], 'T_idea', 40, 760, 420, 'left', 'bob'),
       item(w(9, 'beli'), E[9], '<div class="alir" style="zoom:.82"><div>🙋 Kamu</div><i>⬇️</i><div>🏢 Broker <b style="color:#2E9E55">berlesen</b></div><i>⬇️</i><div>📒 Akaun CDS<br><b>atas nama KAMU</b></div></div>', 'left:400px;top:360px', '', 'pop')]
it += [ch(S[10], E[10], 'T_shock', 640, 800, 400, 'right', 'shake'),
       kad(S[10], E[10], f'Transfer ke akaun<br>{hl("bank peribadi", w(10, "transfer"))} = 🚩🚩🚩', 'left:90px;width:640px;top:380px;text-align:center;font-family:Fredoka,sans-serif;font-size:62px', 'pop'),
       item(w(10, 'bendera'), E[10], 'BENDERA MERAH', 'left:120px;top:770px;font-size:60px;background:#C8473B;color:#fff;transform:rotate(-5deg)', 'lblk', 'pop', 'pulse')]
it += [kad(S[11], E[11], f'✅ Semak <b>Senarai Amaran Pelabur</b><br><span style="font-size:38px">Suruhanjaya Sekuriti (SC)</span><br><br>📞 Dah tertipu? {hl("NSRC 997", w(11, "sembilan"))}', 'left:110px;right:110px;top:380px;text-align:center;font-family:Nunito,sans-serif;font-weight:800;font-size:56px', 'pop'),
       ch(S[11], E[11], 'K_perisai', 360, 900, 380, 'pop', 'bob')]
it += penutup(e, 'BELAJAR KENAL SCAM 🛡️', 'Modul percuma<br>Link di bio')
tulis(e, it)
