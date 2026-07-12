# Exercise 1 — Ferric FX · Video Segment Script

**Slot in the master script:** [0:15 – 1:30] (75 s)
**Spoken words:** ~189 ≈ 73 s at a relaxed 155 wpm — the narration is meant to overlap the on-screen actions, so keep the demo moving while you talk.
**Screens:** the Coursera-hosted app for the demo beats; the local editor (`ex1/src/audioEngine.js`, `ex1/src/persistence.js`) for the code beats.
**Delivery:** read the *Say* lines exactly as printed — they are full sentences, not notes. If a rehearsal runs long, tighten the on-screen actions, not the sentences.

---

## Beat 1 — Power on and play (≈15 s)

**On screen:** The Coursera tab shows "CLICK TO POWER ON" — click it. Pick one of the six cards in the library dock. Tap play, toggle loop for a moment, skip back to the start, and nudge the MASTER VOLUME knob.

**Say:**
"Exercise 1 is Ferric FX, an audio effects processor built with p5.js and p5.sound. I'll load one of the six library sounds and play it through the effects chain, using the transport controls and the master volume."

---

## Beat 2 — Effects on the spectrum (≈12 s)

**On screen:** Drag the LOW-PASS CUTOFF knob down to about 400 Hz while watching *Spectrum Out* collapse. Toggle the WAVESHAPER on and raise DRIVE. Let the audio be heard for a second after you finish the line.

**Say:**
"When I lower the low-pass cutoff, the output spectrum loses its highs. And when I enable the waveshaper, new harmonics appear above the cutoff."

---

## Beat 3 — Record, export, library (≈15 s)

**On screen:** Click REC (top-right), let it bounce ~3 seconds, STOP. In the capture dialog: preview the take, rename it, click EXPORT WAV (the `.wav` download appears), then ADD TO LIBRARY. The new card shows "LPF · WSH · RVB" — click EDIT, then CLR, then DEL in quick succession.

**Say:**
"I can record the processed signal, export it as a WAV file, and add it to the library, where it keeps its effects and can be edited, cleared, or deleted."

---

## Beat 4 — Code: building the chain (≈13 s)

**On screen:** The local editor on `ex1/src/audioEngine.js`, inside `init()`. Hold the cursor on the `disconnect()` loop, then move down the five `connect()` lines.

**Say:**
"Now the core of the engine. Every p5.sound effect connects itself straight to the speakers, so init() first disconnects each node, then wires the chain in series, from the low-pass down to the master gain."

---

## Beat 5 — Code: the spectra and the recorder (≈10 s)

**On screen:** Still in `init()`: the `fftIn` line, then `fftOut.setInput(nodes.masterGain)`, then `recorder.setInput(nodes.masterGain)`.

**Say:**
"Two FFT analysers tap the start and the end of that chain — those are the two spectrum displays — and the recorder taps the end as well, capturing the processed audio."

---

## Beat 6 — Code: bypass and persistence (≈12 s)

**On screen:** Scroll to the bypass branch — `node.drywet(0); node.amp(1)` — and pause on it. Then flash `ex1/src/persistence.js`: the localStorage library index and the IndexedDB audio store.

**Say:**
"Bypass never rewires the graph — it simply sets a stage's dry-wet mix to zero. And the library survives a reload: its index lives in localStorage, its audio in IndexedDB."
