# Jana suara setiap baris + masa perkataan (edge-tts, percuma). Guna: python3 tts.py <ep>.json
# Perlu: pip install edge-tts ; di sandbox Claude set SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
import asyncio, edge_tts, json, os, sys, subprocess
V = {'T': 'ms-MY-OsmanNeural', 'K': 'ms-MY-YasminNeural'}
async def one(i, who, text, rate):
    c = edge_tts.Communicate(text, V[who], rate=rate, boundary='WordBoundary', proxy=os.environ.get('HTTPS_PROXY'))
    mp3, words = bytearray(), []
    async for ch in c.stream():
        if ch['type'] == 'audio': mp3 += ch['data']
        elif ch['type'] == 'WordBoundary': words.append([ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7, ch['text']])
    f = f'a/{i:02d}.mp3'; open(f, 'wb').write(mp3)
    d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
    return {'f': f, 'dur': d, 'words': words}
async def main(p):
    ep = json.load(open(p)); os.makedirs('a', exist_ok=True); out = []
    for i, (who, text) in enumerate(ep['lines']):
        r = await one(i, who, text, ep.get('rate', '+0%')); r['who'] = who; r['text'] = text; out.append(r); print(i, who, round(r['dur'], 2), len(r['words']))
    json.dump(out, open(p.replace('.json', '.tts.json'), 'w'), ensure_ascii=False, indent=1)
asyncio.run(main(sys.argv[1]))
