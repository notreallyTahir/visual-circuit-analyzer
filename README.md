# Visual Circuit Analyzer

A simple Python project that simulates an analog circuit pipeline: it generates wave, amplifies it using an Op-Amp, clips the signal at supply limits, and cleans it up with a low-pass filter.

---

## Features

Multiple Waveforms: Generates sine, square, or triangle waves with customizable frequency, amplitude, and high-frequency noise.

Op-Amp Simulation: Models non-inverting op-amp gain ($A_v = 1 + \frac{R_2}{R_1}$) with rail voltage saturation ($\pm V_{\text{sat}}$).

Low-Pass Filtering: Uses a 2nd-order Butterworth low-pass filter with zero-phase filtering (sosfiltfilt) to avoid time delays.

Visualization: Displays input, amplified, and filtered signals on a single Matplotlib plot.

---

## Code Breakdown

* `signal_gen.py`: Generates waves and gets values from config.json
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
    pip install -r requirements.txt
2. Run the program:
   ```bash
    python main.py
   
---

## Recent Improvements

* Configuration File: Moved settings (frequencies, amplitude, wave type) to config.json instead of hardcoding them in Python scripts.

* More Waveforms: Added support for square and triangle waves alongside sine waves.

* Cleaner Structure: Separated signal generation, circuit math, and main execution into distinct modules.

---

## Planned Improvements

* Add FFT / frequency spectrum plots alongside the time domain graphs.

* Model realistic op-amp limitations like slew rate and gain-bandwidth limits.
