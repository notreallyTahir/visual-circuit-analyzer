# Visual Circuit Analyzer

A simple Python project that simulates an analog circuit pipeline: it generates a noisy sine wave, amplifies it using an Op-Amp, clips the signal at supply limits, and cleans it up with a low-pass filter.

---

## What It Does

1. **Creates a signal:** Generates a 1 kHz sine wave with unwanted 25 kHz high-frequency noise.
2. **Amplifies it:** Passes the wave through a non-inverting Op-Amp model ($A_v = 4.3$) with $\pm 10\text{ V}$ clipping.
3. **Filters it:** Uses a 2nd-order Butterworth low-pass filter ($f_c \approx 1591.5\text{ Hz}$) to strip out the high-frequency noise without delaying the wave.
4. **Plots the result:** Shows $V_{\text{in}}$, $V_{\text{amp}}$, and $V_{\text{filtered}}$ on a single graph in milliseconds.

---

## Code Breakdown

* `signal_gen.py`: Generates the time array, sine wave, and noise.
* `circuit_components.py`: Contains the math for the Op-Amp and RC filter.
* `main.py`: Connects the pipeline together and creates the plots.

---

## Formulas Used
* **AC Voltage Signal:**
  $$V(t) = A \sin(\omega t)$$

* **Angular Frequency:**
  $$\omega = 2\pi f$$
* **Op-Amp Gain:**
  $$A_v = 1 + \frac{R_2}{R_1}$$

* **Filter Cutoff Frequency:**
  $$f_c = \frac{1}{2\pi R C}$$

---

## How to Run

1. Install dependencies:
   ```bash
   pip install numpy scipy matplotlib
