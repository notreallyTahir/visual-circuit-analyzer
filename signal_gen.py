import numpy as np
def generate_input_signal(signal_freq=1000, noise_freq=25000, fs= 100000, duration=0.01):
    num_samples = int(fs*duration) # uniform samples, samples/time * time = samples
    Tarray = np.linspace(0, duration, num_samples)

    # Voltage formula = V = A sin(wt), where w = 2pi * f
    V_signal = 2 * np.sin(2*np.pi*signal_freq*Tarray) 
    V_Noise = 0.5 * np.sin(2*np.pi*noise_freq*Tarray)

    Vin = V_signal + V_Noise
    return Vin, Tarray
