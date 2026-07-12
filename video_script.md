# Intelligent Signal Processing Midterm — Video Demonstration Script (v4)

**Target Duration:** ~5:40 (hard cap 6:00 — assume the marker stops watching there)
**Format:** Screencast with voice narration
**Scoring target:** 5/5 — "Excellent video demonstration of all exercises with appropriate voice narration and core code walkthrough."
**Balance:** each exercise = a rapid, jump-cut **Run** beat (proof the app works) + a longer **Code** walkthrough (~half the section). The narration explains implementation decisions, not just what's on screen.

> [!TIP]
> **Recording setup:**
> - The running apps are demoed on Coursera: the two web apps via their static-page links (the same links included in the report), exercises 3 & 4 via their Coursera Jupyter links. Open and sign in to every tab **before** recording.
> - Code walkthroughs come from the **local clone** in your editor (ex1/ex2 source files); for exercises 3 & 4 the code is walked through directly in the Coursera notebook cells.
> - Pre-run all three notebooks on Coursera beforehand so outputs, the recovered-audio files and the model cache already exist; during recording only re-run the key cells.
> - Record with OBS capturing **system audio + microphone** (QuickTime alone does not capture app audio — on macOS route it through BlackHole/Loopback). The marker must *hear* the CAPTCHA, the effects and the decoded code.
> - Pause narration whenever the audio itself is the evidence (the CAPTCHA words, the decoded "1891").
> - Keep the Run beats moving — jump-cut between actions; the saved seconds belong to the code.

---

## [0:00 – 0:15] (15 s) Introduction

**Visual:** Browser with the four Coursera exercise tabs; the local repo open in the editor behind it.

**Voice-over:**
"Hello — this is my video demonstration for the Intelligent Signal Processing midterm. For each exercise I'll show the application running on Coursera, then spend most of the time in the code that makes it work."

---

## [0:15 – 1:30] (75 s) Exercise 1 — Ferric FX: Web Audio Effects Processor

**Run — Coursera tab (~25 s, jump-cut):**
1. "CLICK TO POWER ON" → power on, pick a library card (six pre-loaded). Tap play/pause, loop, skip-to-start; nudge MASTER VOLUME.
2. Low-Pass CUTOFF down to ~400 Hz → *Spectrum Out* loses the highs; Waveshaper on, DRIVE up → harmonics reappear.
3. REC → bounce a few seconds → STOP → in the dialog: **EXPORT WAV** (show the `.wav` download) + **ADD TO LIBRARY** → new card ("LPF · WSH · RVB") → EDIT / CLR / DEL in quick succession.

**Code — local editor, `ex1/src/audioEngine.js` (~45 s):**
1. `init()`: the `disconnect()` loop over the four effects, then the series wiring `lowpass → waveshaper → compressor → reverb → masterGain → output`.
2. The two analysers: `fftIn` on the source, `fftOut.setInput(nodes.masterGain)` — the in/out spectra.
3. `recorder.setInput(nodes.masterGain)` — REC captures the *processed* bus.
4. The bypass branch: `node.drywet(0); node.amp(1)` — contrast with the active branch above it.
5. Flash `src/persistence.js`: the localStorage library index and the WAV-encoded blobs in IndexedDB.

**Voice-over:**
"Exercise 1 is Ferric FX, built with p5.js and p5.sound. Quickly, the app: transport, the low-pass stripping the highs from the output spectrum, the waveshaper adding new harmonics back, and a take recorded, exported as WAV, and saved to the library for editing, clearing or deleting.
Now the core code. Every p5.sound effect auto-connects to the speakers, so `init()` first disconnects each node, then wires the fixed series chain: low-pass, waveshaper, compressor, reverb, master gain. Two FFTs tap the chain — the source and the master gain — giving the in and out spectra, and the recorder taps the master gain too, so it captures the processed signal. Bypass never rewires the graph: it sets a stage's dry/wet to zero at unity gain. Persistence is two layers — the library index in localStorage, the audio WAV-encoded into IndexedDB — so everything survives a reload."

---

## [1:30 – 2:55] (85 s) Exercise 2 — Audio CAPTCHA, Meyda Visualisation & Voice Controller

**Run — Coursera tab (~30 s, jump-cut):**
1. CAPTCHA: play — **let the first two word–digit pairs be heard** (pause narration), point at the pulsing scope — jump-cut to the three answers filled → **"Verified · Human"**.
2. Visualiser: flick through **Ex2_sound1** "Ripple pond" → **Ex2_sound2** "Particle burst field" → **Ex2_sound3** "Spark shower" (a beat each, feature readout visible top-left).
3. **Kalte_Ohren_(Remix).mp3** "Figure field": VOICE chip on → say **"red"** → background changes; **"triangle"** → figures re-render.

**Code — local editor (~50 s):**
1. `ex2complete/london-isp-midterm-ex2/app/js/challenge.js`: three targets + two fillers → the five spoken pairs.
2. `app/js/audio.js`: the per-word randomised `pitch` / `rate` / `voiceIndex`; the noise bed — pink noise → band-pass at 1.4 kHz, brown noise → low-pass rumble; `updateNoiseAmp()` amplitude-modulating the mask in sync with the words.
3. `ex2complete/london-isp-midterm-ex223/sketch.js`: the Meyda analyzer callback — the flux loop summing positive deltas between `spec` and `prevSpectrum`; the onset line `fluxN > fluxBaseline * 1.8`.
4. `handleVoiceCommand()`: the word-by-word scan over `VOICE_COLORS` / `VOICE_SHAPES`, latest keyword per category wins.

**Voice-over:**
"Exercise 2. The CAPTCHA speaks five word–digit pairs — listen — [pause] (≈8 s) — and you type the digit that followed each of the three displayed words. In the code, every pair — three targets, two decoys — gets a randomly chosen voice, pitch and speaking rate, while a masking bed of band-passed pink noise and brown-noise rumble runs underneath, amplitude-modulated in sync with the words, so a bot can't subtract a static background.
The visualiser's features come from an offline librosa analysis — the highest-variance features per sound drive each mapping. In the Meyda callback, streaming Meyda can't compute spectral flux, so I sum the positive differences between consecutive amplitude spectra; a spike one-point-eight times above its running baseline is an onset and spawns ripples, sparks or bursts. The voice controller scans each utterance word by word — five colours, four shapes, plus transport, volume, scale and trails — and the latest keyword per category wins."

---

## [2:55 – 4:10] (75 s) Exercise 3 — Audio Steganography (Python)

**Run + code — Coursera Jupyter, Exercise 3.1 notebook (pre-run) (~40 s):**
1. The detection cell + **energy table**: `Ex3_sound4.wav` flagged — **10.86%** above 18 kHz, peak **19,001 Hz**. Glance at the spectrum zoom (carrier + symmetric sidebands) and the spectrogram (burst above the cyan 18 kHz line).
2. Walk the **`demodulate()` cell** line by line — band-pass → `hilbert()` envelope → low-pass — re-run it and the playback cell, and **play the recovered audio: pause narration so "1891" is clearly audible**.

**Run + code — Exercise 3.2 notebook (~35 s):**
3. Walk the embed cells: `KEY`, `N_LSB = 2`, `HEADER_BITS = 32`; `_key_order()` — `random.Random(key).shuffle(order)`. Re-run: **184 of 407,280 samples used, 132 changed, max ±3**; the waveform plot with modified samples in red.
4. The extraction cell: correct key → exact message; wrong key → *"decoding failed (invalid UTF-8)"* in the `try/except`.

**Voice-over:**
"Exercise 3, in the Coursera notebooks. Detection is one function: the fraction of spectral energy at or above 18 kilohertz. Sound 4 holds 10.86 percent — peaking at 19,001 hertz — and the spectrum zoom shows a carrier with symmetric sidebands, the AM fingerprint, with the burst visible in the spectrogram. `demodulate()` reverses it in three steps you can read right here: a band-pass isolates the carrier, the Hilbert envelope strips the oscillation, and a low-pass returns the message to baseband. Listen — [pause] (≈4 s) — 1891.
Task 3.2: a single integer key seeds a pseudo-random shuffle of all sample indices, and the message rides two least-significant bits per selected sample behind a 32-bit length header, so extraction is self-contained. Running it: 184 of 407,280 samples used, only 132 actually change, none by more than plus-or-minus 3 out of 65,536. The correct key recovers the message exactly; a wrong key lands on the wrong samples and fails on invalid UTF-8."

---

## [4:10 – 5:25] (75 s) Exercise 4 — Offline Multilingual ASR

**Run + code — Coursera Jupyter, Exercise 4.ipynb (pre-run) (~75 s):**
1. Glance: the version-pinned install cell (`sherpa-onnx==1.9.30`, `onnxruntime==1.14.1`) and the model bundles resolving from local disk.
2. Walk `build_recognizer()` — `OnlineRecognizer.from_transducer(..., decoding_method="greedy_search", provider="cpu")` — and the `recognizers = {lang: …}` dictionary: language selection is a lookup.
3. Walk **`preprocess()`**: `butter(4, 80, "highpass", output="sos")` + `sosfiltfilt` (zero-phase), `rms_normalize` to −20 dBFS, the 0.8 s lead-in pad.
4. Glance at `wer()` — the word-level Levenshtein counting S/D/I.
5. Re-run the evaluation summary cell if fast, else scroll its output: per-file table — **English corpus 14.7%, Spanish 0.0%, Italian 0.0%**, personal recordings **0%**. *(If you rename the recordings to `your_sentence1/2.wav` per the brief before recording, re-run first so the table shows the required names.)*

**Voice-over:**
"Exercise 4, the airport assistant, in the module's Python 3.7 Coursera environment. sherpa-onnx replaces the archived Mozilla DeepSpeech — actively maintained, and fully offline on CPU. In the code, language selection is a dictionary: each language maps to its own OnlineRecognizer built with from_transducer, greedy search on the CPU provider, over int8-quantised bundles — a streaming Zipformer for English, Kroko for Spanish and Italian. preprocess() handles the noisy concourse in three stages you can read here: an order-4 Butterworth high-pass at 80 hertz, run forwards and backwards with sosfiltfilt so it's zero-phase; RMS normalisation to minus 20 dBFS; and a lead-in pad that settles the streaming decoder before the first phoneme. wer() aligns hypothesis and reference with a word-level Levenshtein, counting substitutions, deletions and insertions. The results: Spanish and Italian at zero percent, English at 14.7 — vocabulary confusions like 'check-in desk' becoming 'chicken desk' — and both of my own recordings at zero."

---

## [5:25 – 5:40] (15 s) Conclusion

**Visual:** The WER summary output, or the Ferric FX interface.

**Voice-over:**
"That's the four exercises — an effects chain built once and never rewired, a synthesised and masked CAPTCHA, feature-driven visuals under voice control, key-scattered LSB steganography, and offline multilingual recognition. Thanks for watching."
