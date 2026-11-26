# Video 9:16 daripada gambar CGI (Gemini) + suara Osman + sari kata berkumpulan + hook + label.
# Guna: python3 cgi_ep.py <ep.json>   (perlu: edge-tts, ffmpeg; SSL_CERT_FILE & HTTPS_PROXY di sandbox)
# ep.json: {"out": "...mp4", "hook": ["baris1","baris2"], "cta": ["baris1","baris2"], "label": "...",
#           "scenes": [{"img": "path.jpg", "say": "teks narator", "zoom": "in|out"}]}
import asyncio, edge_tts, json, os, subprocess, sys, tempfile

FONT = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))

async def tts(text, f):
    c = edge_tts.Communicate(text, 'ms-MY-OsmanNeural', rate='+6%', boundary='WordBoundary', proxy=os.environ.get('HTTPS_PROXY'))
    mp3, words = bytearray(), []
    async for ch in c.stream():
        if ch['type'] == 'audio': mp3 += ch['data']
        elif ch['type'] == 'WordBoundary': words.append([ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7, ch['text']])
    open(f, 'wb').write(mp3)
    d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
    return d, words

def chunks(words, n=3):
    out = []
    for i in range(0, len(words), n):
        g = words[i:i + n]; out.append([g[0][0], g[-1][1], ' '.join(w[2] for w in g)])
    for i in range(len(out) - 1): out[i][1] = out[i + 1][0]
    return out

def dt(tmp, text, size, y, t0=None, t1=None, box=None, border=6, color='white'):
    p = tempfile.mktemp(suffix='.txt', dir=tmp); open(p, 'w').write(text)
    s = f"drawtext=fontfile={FONT}:textfile={p}:fontsize={size}:fontcolor={color}:borderw={border}:bordercolor=black:x=(w-text_w)/2:y={y}"
    if box: s += f":box=1:boxcolor={box}:boxborderw=18"
    if t0 is not None: s += f":enable='between(t,{t0:.2f},{t1:.2f})'"
    return s

def main(p):
    ep = json.load(open(p)); tmp = tempfile.mkdtemp(); segs = []; t = 0.0; subs = []
    for i, sc in enumerate(ep['scenes']):
        a = f'{tmp}/a{i}.mp3'; d, words = asyncio.run(tts(sc['say'], a)); dur = d + 0.35
        n = int(dur * FPS); z = "1+0.10*on/%d" % n if sc.get('zoom', 'in') == 'in' else "1.10-0.10*on/%d" % n
        v = f'{tmp}/v{i}.mp4'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', sc['img'], '-i', a, '-filter_complex',
            f"[0]scale={W}:-2,crop={W}:{H},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},format=yuv420p[v];[1]apad=pad_dur=0.35[a]",
            '-map', '[v]', '-map', '[a]', '-t', f'{dur:.3f}', '-r', str(FPS), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-c:a', 'aac', '-ar', '44100', v], check=True)
        segs.append(v)
        for c0, c1, txt in chunks(words): subs.append((t + c0, t + c1, txt))
        t += dur
    lst = f'{tmp}/l.txt'; open(lst, 'w').write(''.join(f"file '{s}'\n" for s in segs))
    raw = f'{tmp}/raw.mp4'; subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', raw], check=True)
    f = []
    f.append(f"drawbox=x=0:y=0:w=iw:h=520:color=black@0.35:t=fill:enable='lt(t,2.8)'")
    f.append(dt(tmp, ep['hook'][0], 92, 170, 0, 2.8, box='0xFFD400@0.95', border=0, color='black'))
    f.append(dt(tmp, ep['hook'][1], 62, 330, 0, 2.8))
    te = t - 3.2
    for a0, a1, txt in subs:
        a0, a1 = max(a0, 2.85), min(a1, te)
        if a1 - a0 < 0.15: continue
        f.append(dt(tmp, txt.upper(), 70, 1360, a0, a1, border=7))
    f.append(f"drawbox=x=0:y=ih-760:w=iw:h=520:color=black@0.45:t=fill:enable='gt(t,{te:.2f})'")
    f.append(dt(tmp, ep['cta'][0], 62, 1180, te, t + 1, box='0xFFD400@0.95', border=0, color='black'))
    f.append(dt(tmp, ep['cta'][1], 52, 1330, te, t + 1))
    f.append(dt(tmp, ep['label'], 30, 1840, border=3))
    mus = os.path.join(HERE, 'out/muzik-ceria.wav')
    if not os.path.exists(mus):
        os.makedirs(os.path.join(HERE, 'out'), exist_ok=True); subprocess.run(['python3', 'muzik.py'], cwd=HERE, check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-stream_loop', '-1', '-i', mus, '-filter_complex',
        ','.join(f) + '[v];[1]volume=0.10[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-16:TP=-1.5[a]',
        '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', ep['out']], check=True)
    print(ep['out'], round(t, 1), 's')

if __name__ == '__main__': main(sys.argv[1])
