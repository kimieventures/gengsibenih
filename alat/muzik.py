# Muzik latar asli (dijana sendiri, bebas hak cipta) untuk video Geng Si Benih.
import numpy as np, sys
from scipy.io import wavfile
SR = 44100
def ks(freq, dur, bright=0.5, seed=0):
    """Petikan gaya ukulele (Karplus-Strong)."""
    rng = np.random.default_rng(seed); n = int(SR * dur); p = max(2, int(SR / freq))
    buf = rng.uniform(-1, 1, p) * 0.5; out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = 0.996 * (bright * buf[i % p] + (1 - bright) * buf[(i + 1) % p]) if True else 0
    return out
def note(m): return 440 * 2 ** ((m - 69) / 12)
def env(n, a=0.005, r=0.2):
    e = np.ones(n); ai = int(a * SR); ri = int(r * SR)
    e[:ai] = np.linspace(0, 1, ai); e[-ri:] = np.linspace(1, 0, ri); return e

def make(bpm, chords, mel, dur=30.0, seed=1):
    beat = 60 / bpm; N = int(dur * SR); mix = np.zeros(N + SR)
    def add(sig, t, g):
        i = int(t * SR)
        if i >= len(mix): return
        j = min(len(mix), i + len(sig)); mix[i:j] += sig[:j - i] * g
    t = 0.0; k = 0
    while t < dur:
        root, third, fifth = chords[k % len(chords)]
        # strum ukulele: 8th notes pola "down down-up up-down"
        for s, g in [(0, 1), (1, .6), (1.5, .7), (2.5, .6), (3, .8), (3.5, .5)]:
            ts = t + s * beat
            for d, m in enumerate([root + 12, third + 12, fifth + 12, root + 24]):
                add(ks(note(m), 0.9, 0.5, seed + k * 13 + d), ts + d * 0.012, 0.11 * g)
        # bass
        for s in [0, 2]:
            b = np.sin(2 * np.pi * note(root - 12) * np.arange(int(beat * 1.6 * SR)) / SR)
            add(b * env(len(b), 0.01, 0.3), t + s * beat, 0.22)
        # melodi bunyi "glockenspiel"
        for (s, m, l) in mel[k % len(mel)]:
            n_ = int(l * beat * SR); tt = np.arange(n_) / SR
            g_ = (np.sin(2 * np.pi * note(m) * tt) + 0.3 * np.sin(2 * np.pi * note(m) * 2.76 * tt)) * np.exp(-tt * 5)
            add(g_, t + s * beat, 0.16)
        # perkusi: tepukan & shaker
        rng = np.random.default_rng(k)
        for s in [1, 3]:
            c = rng.uniform(-1, 1, int(0.08 * SR)) * np.exp(-np.arange(int(0.08 * SR)) / (0.012 * SR)); add(c, t + s * beat, 0.18)
        for s in np.arange(0, 4, 0.5):
            sh = rng.uniform(-1, 1, int(0.04 * SR)) * np.exp(-np.arange(int(0.04 * SR)) / (0.006 * SR)); add(sh, t + s * beat, 0.05)
        t += 4 * beat; k += 1
    mix = mix[:N]
    f = int(1.5 * SR); mix[-f:] *= np.linspace(1, 0, f); mix[:int(.3 * SR)] *= np.linspace(0, 1, int(.3 * SR))
    mix = mix / np.max(np.abs(mix)) * 0.8
    st = np.stack([mix, np.roll(mix, 220) * 0.95], 1)
    return (st * 32767).astype(np.int16)

C, G, Am, F, D, Em = (60, 64, 67), (55, 59, 62), (57, 60, 64), (53, 57, 60), (62, 66, 69), (52, 55, 59)
MEL_A = [[(0, 76, 1), (1, 79, 1), (2, 76, 1), (3, 72, 1)], [(0, 74, 1), (1, 71, 1), (2, 74, 2)],
         [(0, 72, 1), (1, 76, 1), (2, 79, 1), (3, 81, 1)], [(0, 77, 2), (2, 76, 1), (3, 74, 1)]]
MEL_B = [[(0, 72, .5), (.5, 74, .5), (1, 76, 1), (2.5, 79, 1.5)], [(0, 74, 1), (1.5, 71, .5), (2, 74, 2)],
         [(0, 76, .5), (.5, 74, .5), (1, 72, 1), (2, 69, 2)], [(0, 72, 1), (1, 74, 1), (2, 76, 2)]]
TRACKS = {
    'ceria': make(112, [C, G, Am, F], MEL_A, seed=3),       # gembira, kelakar
    'nakal': make(124, [F, G, Em, Am], MEL_B, seed=7),      # lebih laju, nakal
}
if __name__ == '__main__':
    for k, v in TRACKS.items(): wavfile.write(f'out/muzik-{k}.wav', SR, v); print(k)
