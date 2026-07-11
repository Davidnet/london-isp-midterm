# Intelligent Signal Processing Midterm — Video Demonstration Script (v2)

**Target Duration:** ~6 minutes  
**Format:** Screencast with voice narration  
**Scoring target:** 5/5 — "Excellent video demonstration of all exercises with appropriate voice narration and core code walkthrough."

> [!TIP]
> **Recording tips:** Use OBS or QuickTime screen recording. Keep the browser, editor, and terminal visible side-by-side where possible. Rehearse once before recording so transitions are smooth.

---

## [0:00 – 0:15] Introduction

**Visual:** Terminal in the repo root. Briefly show `ls` output with `ex1/`, `ex2complete/`, `ex3/`, `ex4/`.

**Voice-over:**  
"Hello, this is my video demonstration for the Intelligent Signal Processing midterm. The project is organized as four Git submodules — one per exercise. I'll demonstrate each application running, walk through the core logic, and show the results."

---

## [0:15 – 1:30] Exercise 1 — Ferric FX: Web Audio Effects Processor

**Visual:**  
1. In `ex1/`, start the local server (e.g. `npx serve .` or the static server in `.claude/`). Open the app in Chrome — it shows "CLICK TO POWER ON".
2. Click to power on. Select a sound from the **library dock** at the bottom — show the six pre-loaded cards.
3. Adjust effects: drag the **Low-Pass cutoff** knob down to ~400 Hz — point out that the *Spectrum Out* display loses the high-frequency content. Toggle the **Waveshaper** on and increase drive — show harmonics reappearing above the cutoff in the output spectrum.
4. Toggle **Compressor** and **Reverb** on. Show the **DRY/WET** and **OUT LVL** faders. Show the **bypass toggle** on a stage.
5. Click the **REC** button (top-right). Let it bounce a few seconds, click **STOP**. In the capture dialog, preview the take, rename it, and click **Save to Library**. Show the new card appearing in the dock with its baked-in effects label (e.g. "LPF · WSH · RVB").
6. On that new card, demonstrate **EDIT** (loads config into the editor), **CLR** (resets to dry), and **DEL** (removes the card).
7. Briefly switch to the editor showing [audioEngine.js](file:///Users/davidgf/Documents/london-isp-midterm/ex1/src/audioEngine.js). Scroll to the `init()` function.

**Voice-over:**  
"For Exercise 1, I built Ferric FX, a web-based audio effects processor using `p5.js` and `p5.sound`. 
Here, we can load a pre-recorded sound and apply a fixed processing chain. As you can see, I can adjust the low-pass filter cutoff, add waveshaper distortion to create new spectral harmonics, and add reverb. The spectrum analysers update in real-time. 
I can also record the processed audio and save it as a WAV file, or save my current effects configuration as a preset in the sounds library.
Looking at the core logic in `audioEngine.js`, the effects are disconnected from the main output and wired in series from the low-pass filter down to the master gain. The bypass toggle simply sets the dry/wet mix to zero rather than rewiring the graph, ensuring smooth transitions."

---

## [1:30 – 3:00] Exercise 2 — Audio CAPTCHA, Meyda Visualisation & Voice Controller

**Visual:**  
1. Open the Exercise 2.1 audio CAPTCHA app (in `ex2complete/london-isp-midterm-ex2/app/`). Click play — the CAPTCHA speaks five word–digit pairs (e.g. "apple nine, blue three, …"). Three target words are displayed on screen. Type the corresponding digits and submit. Show the "PASS" result.
2. Switch to the Exercise 2.2/2.3 visualisation app (`ex2complete/london-isp-midterm-ex223/`). Start the local server.
3. Select **Ex2_sound1.wav** and press Play — show the "Ripple pond" visualization with concentric rings breathing with loudness and onset ripples.
4. Switch to **Ex2_sound2.wav** — show the "Particle burst field" with colour and size reacting dynamically.
5. Switch to **Kalte_Ohren_(Remix).mp3** — show the "Figure field" visualisation. Point out the real-time feature readout (top-left corner showing rms, spectralCentroid, spectralFlatness, zcr, spectralFlux values).
6. Click the **VOICE · OFF** chip to enable the microphone. Speak: **"red"** → background changes. **"triangle"** → figures change shape. **"bigger"** → figures scale up. **"trails"** → motion blur appears. **"reset"** → clears all overrides.
7. Briefly show [sketch.js](file:///Users/davidgf/Documents/london-isp-midterm/ex2complete/london-isp-midterm-ex223/sketch.js) — highlight the Meyda analyzer callback and the `handleVoiceCommand()` function.

**Voice-over:**  
"Exercise 2 has three tasks. First, the audio CAPTCHA: it speaks five word–digit pairs using `p5.speech` with randomized voice, pitch, and rate. A masking layer of band-passed pink noise and brown noise runs underneath, amplitude-modulated to resist automated scraping. The user must type the digit that follows each of the three displayed target words.

Next is the Meyda-driven audio visualisation. Feature selection was measured, not guessed — I ran an offline analysis with librosa to compute each feature's coefficient of variation and mapped the features with the largest swing per sound. For example, Sound 2 has an RMS CV of 1.15 and centroid CV of 1.26, so centroid drives particle colour from dark cyan to hot magenta, and RMS drives emission rate. The spectral flux is derived from consecutive amplitude spectra since Meyda's streaming analyzer can't compute it directly — a spike 1.8× above the running baseline triggers an onset event.

The voice controller uses `p5.SpeechRec` in continuous mode. It scans each utterance word-by-word for keywords — background colours, shape names, transport commands, volume, speed, scale, and trail effects — with homophones accepted. Saying 'red triangle' immediately overrides the background colour and figure shape."

---

## [3:00 – 4:20] Exercise 3 — Audio Steganography (Python)

**Visual:**  
1. Open `ex3/app/Ex3_walkthrough.ipynb` in Jupyter. Run the cells — show:
   - The energy table flagging `Ex3_sound4.wav` with 10.86% ultrasonic energy at a peak of 19,001 Hz.
   - The spectrogram showing the AM carrier and symmetric sidebands above 18 kHz.
   - The demodulated output — play the recovered audio that speaks **"1891"**.
2. Switch to `ex3/app/Ex3_2_walkthrough.ipynb`. Run the cells — show:
   - The embedding of the message *"It always seems impossible until it's done"* into `Ex3_sound5.wav`: 184 of 407,280 samples used, 132 changed, each by at most ±3.
   - The cover vs. stego spectra overlay — they coincide perfectly.
   - Extraction with the correct key recovering the exact message.
   - Extraction with a wrong key failing on invalid UTF-8.

**Voice-over:**  
"Exercise 3 investigates audio steganography in Python. In Task 3.1, four WAV files may hide a secret code that was amplitude-modulated onto an ultrasonic carrier and mixed into a normal recording. My detector measures the fraction of spectral energy above 18 kHz for each file. `Ex3_sound4.wav` has 10.86% of its energy there — far above the others — peaking at exactly 19,001 Hz. The spectrogram confirms the AM fingerprint: a carrier line flanked by symmetric sidebands.

To decode, I band-pass around the carrier, apply Hilbert envelope detection to strip the carrier oscillation, and low-pass back to baseband. The recovered signal is intelligible speech: the code is 1891.

In Task 3.2, I implemented a key-based LSB embedding scheme. A single integer key seeds a pseudo-random permutation of sample indices, scattering the secret bits across non-consecutive samples. Each selected sample carries two least-significant bits, and a 32-bit length header makes extraction self-contained. The embedding altered only 132 samples out of 407,280, each by at most ±3 out of 65,536 — well below the threshold of hearing. With the correct key, the message is recovered exactly; a wrong key selects wrong samples and decoding fails."

---

## [4:20 – 5:40] Exercise 4 — Offline Multilingual ASR

**Visual:**  
1. In the terminal, navigate to `ex4/`. Run `./launch.sh` to build and start the Docker container (Python 3.7 environment). Show it completing.
2. Execute the Jupyter notebook `ex4/asr-project/Exercise 4.ipynb` inside the container. Show:
   - The version-pinned installation of `sherpa-onnx` 1.9.30 and `onnxruntime` 1.14.1.
   - The three model bundles loading from local disk (Zipformer for English, Kroko for Spanish and Italian).
   - The preprocessing chain output: show the before/after waveform plot from the report (high-pass filter removing rumble below 80 Hz, RMS normalization).
   - The per-file WER results printing: English corpus WER 14.7%, Spanish 0.0%, Italian 0.0%.
   - The two personal recordings (`own_sentence1.wav`, `own_sentence2.wav`) both achieving 0% WER.
3. Briefly show the preprocessing code in the notebook — the `sosfiltfilt` high-pass and RMS normalization.

**Voice-over:**  
"Exercise 4 is an offline multilingual speech interface for an airport virtual assistant. It runs inside a Docker container with Python 3.7 to match the module's Coursera environment. I chose `sherpa-onnx` over the deprecated Mozilla DeepSpeech because it's actively maintained and runs entirely offline on CPU.

The system uses a streaming Zipformer transducer for English and Kroko transducers for Spanish and Italian, all with int8-quantized weights for efficiency on kiosk hardware. Each language gets its own `OnlineRecognizer` with greedy-search decoding.

To handle the noisy airport environment, every utterance passes through a three-stage preprocessing chain: first, an order-4 zero-phase Butterworth high-pass at 80 Hz removes low-frequency rumble below the fundamental of adult speech; second, RMS normalization to −20 dBFS standardizes speaker volume; third, a 0.8-second low-amplitude lead-in pad lets the streaming decoder's state settle before the first phoneme.

Spanish and Italian are recognized perfectly at 0% WER. English has a corpus WER of 14.7% — the remaining errors are vocabulary-level confusions like 'check-in desk' decoding as 'chicken desk', which are limitations of the compact streaming model, not noise. Both personal recordings also achieve 0% WER after preprocessing."

---

## [5:40 – 6:00] Conclusion

**Visual:** Show the WER summary table from the notebook output, or the Ferric FX interface.

**Voice-over:**  
"To summarize: Exercise 1 implements a full audio effects processor with recording and a persistent sounds library. Exercise 2 combines a robust audio CAPTCHA with data-driven Meyda visualizations and a voice controller. Exercise 3 detects an ultrasonic AM-hidden code and implements a key-secured LSB embedding scheme. And Exercise 4 deploys an offline multilingual ASR system with noise-robust preprocessing. Thank you for watching."
