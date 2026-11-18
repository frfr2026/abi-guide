#!/usr/bin/env python3
"""ABI NEXUS — build_audio.py : generation des ambiances sonores (S17).

Produit deux pistes boucleables, synthetisees localement :

  audio/ambiance-menu.mp3      nappe d'ambiance industrielle sombre
                                (drone grave, souffle de ventilation,
                                cliquetis metalliques lointains)
  audio/ambiance-infection.mp3 ambiance d'alerte pour les pages zombies
                                (bourdon dissonant, pulsation, souffle
                                chaud, impacts lointains)

Aucun binaire externe n'est requis : le signal est genere avec numpy
et encode en MP3 (MPEG-1 Layer III) via lameenc.

Usage : python3 tools/build_audio.py
"""
import pathlib
import struct
import wave

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'audio'
OUT = OUT_DIR / 'ambiance-menu.mp3'
OUT_INF = OUT_DIR / 'ambiance-infection.mp3'

SR = 44100
DUR = 24.0          # secondes : boucle courte, le lecteur boucle deja
N = int(SR * DUR)


def synth():
    t = np.arange(N) / SR
    rng = np.random.default_rng(20261117)

    # ── nappe grave : deux sinus tres proches (battement lent) ──
    drone = (0.30 * np.sin(2 * np.pi * 55.0 * t)
             + 0.22 * np.sin(2 * np.pi * 55.35 * t)
             + 0.12 * np.sin(2 * np.pi * 110.0 * t + 0.4))
    # respiration lente de l'ambiance
    drone *= 0.75 + 0.25 * np.sin(2 * np.pi * 0.06 * t)

    # ── souffle de ventilation : bruit rose filtre passe-bas ──
    noise = rng.normal(0.0, 1.0, N)
    # filtre passe-bas simple (moyenne mobile glissante)
    k = 220
    kernel = np.ones(k) / k
    pink = np.convolve(noise, kernel, mode='same')
    pink *= 3.2 * (0.7 + 0.3 * np.sin(2 * np.pi * 0.11 * t + 1.1))

    # ── cliquetis metalliques lointains ──
    clicks = np.zeros(N)
    for _ in range(26):
        start = int(rng.uniform(0.2, DUR - 0.6) * SR)
        length = int(rng.uniform(0.03, 0.11) * SR)
        env = np.exp(-np.linspace(0, 7, length))
        tone = (np.sin(2 * np.pi * rng.uniform(900, 2600) * np.arange(length) / SR)
                + 0.5 * np.sin(2 * np.pi * rng.uniform(2600, 5200) * np.arange(length) / SR))
        clicks[start:start + length] += rng.uniform(0.03, 0.11) * env * tone

    # ──Metal distant : bruit bande etroit ──
    k2 = 40
    hiss = np.convolve(rng.normal(0, 1, N), np.ones(k2) / k2, mode='same')
    hiss = np.convolve(hiss, np.ones(k2) / k2, mode='same') * 9.0

    sig = drone + pink + clicks + hiss * 0.25

    # ── fondu de bouclage : les extremites se rejoignent ──
    fade = int(SR * 1.2)
    ramp = np.linspace(0, 1, fade)
    sig[:fade] *= ramp
    sig[-fade:] *= ramp[::-1]

    # normalisation
    peak = np.max(np.abs(sig))
    if peak > 0:
        sig = sig / peak * 0.82
    return sig


def synth_infection():
    """Ambiance des pages zombies : bourdon dissonant, pulsation
    cardiaque, souffle chaud, impacts lointans. Genere avec une graine
    differente pour ne pas reutiliser le signal du menu."""
    t = np.arange(N) / SR
    rng = np.random.default_rng(20261117)

    # ── bourdon dissonant : quinte mineure + seconde mineure ──
    drone = (0.26 * np.sin(2 * np.pi * 73.0 * t)
             + 0.20 * np.sin(2 * np.pi * 87.0 * t + 0.7)   # quinte
             + 0.13 * np.sin(2 * np.pi * 77.8 * t + 1.9))  # seconde mineure
    drone *= 0.70 + 0.30 * np.sin(2 * np.pi * 0.17 * t)

    # ── pulsation lente, comme un battement ──
    beat = 0.16 * np.sin(2 * np.pi * 1.15 * t) ** 8
    drone += beat * np.sin(2 * np.pi * 146.0 * t + 0.2)

    # ── souffle chaud : bruit passe-bas, plus grave que celui du menu ──
    noise = rng.normal(0.0, 1.0, N)
    k = 520
    warm = np.convolve(noise, np.ones(k) / k, mode='same')
    warm *= 3.0 * (0.65 + 0.35 * np.sin(2 * np.pi * 0.23 * t + 0.5))

    # ── impacts lointans, plus graves et plus espacés ──
    hits = np.zeros(N)
    for _ in range(14):
        start = int(rng.uniform(0.4, DUR - 1.2) * SR)
        length = int(rng.uniform(0.12, 0.28) * SR)
        env = np.exp(-np.linspace(0, 6, length))
        tone = (np.sin(2 * np.pi * rng.uniform(120, 300) * np.arange(length) / SR)
                + 0.4 * np.sin(2 * np.pi * rng.uniform(600, 1400) * np.arange(length) / SR))
        hits[start:start + length] += rng.uniform(0.05, 0.14) * env * tone

    # ── sifflement aigu tres discret, sugere l'infection ──
    k2 = 26
    air = np.convolve(rng.normal(0, 1, N), np.ones(k2) / k2, mode='same')
    air = np.convolve(air, np.ones(k2) / k2, mode='same') * 7.0

    sig = drone + warm + hits + air * 0.18

    # ── fondu de bouclage ──
    fade = int(SR * 1.4)
    ramp = np.linspace(0, 1, fade)
    sig[:fade] *= ramp
    sig[-fade:] *= ramp[::-1]

    peak = np.max(np.abs(sig))
    if peak > 0:
        sig = sig / peak * 0.80
    return sig


def write_wav(path, sig):
    pcm = np.clip(sig, -1.0, 1.0)
    pcm = (pcm * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def encode_mp3(wav_path, mp3_path, bitrate=64):
    import lameenc
    enc = lameenc.Encoder()
    enc.set_bit_rate(bitrate)
    enc.set_in_sample_rate(SR)
    enc.set_channels(1)
    enc.set_quality(2)

    with wave.open(str(wav_path), 'rb') as w:
        raw = w.readframes(w.getnframes())
    # lameenc attend des echantillons int16 : le WAV contient deja
    # de l'int16, aucune conversion de format n'est necessaire
    pcm = np.frombuffer(raw, dtype='<i2')
    mp3 = enc.encode(pcm.tobytes())
    mp3 += enc.flush()
    mp3_path.write_bytes(mp3)
    return len(mp3)


def build(synth_fn, out_path, tmp_name):
    sig = synth_fn()
    tmp = OUT_DIR / tmp_name
    write_wav(tmp, sig)
    size = encode_mp3(tmp, out_path)
    tmp.unlink()
    return size


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    size = build(synth, OUT, '_ambiance-menu.wav')
    print('audio/ambiance-menu.mp3 : %d Ko (%.1f s, mono 44,1 kHz)'
          % (size / 1024, DUR))
    size = build(synth_infection, OUT_INF, '_ambiance-infection.wav')
    print('audio/ambiance-infection.mp3 : %d Ko (%.1f s, mono 44,1 kHz)'
          % (size / 1024, DUR))


if __name__ == '__main__':
    main()
