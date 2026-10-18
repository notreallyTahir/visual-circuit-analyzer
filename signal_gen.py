import numpy as np
import json
from scipy import signal


# json file to save data
with open('config.json', 'r') as file:
    data = json.load(file)

values = data['signal_gen']

def generate_input_signal(cfg=values):
    signal_freq = cfg['Signal Frequency']
    noise_freq = cfg['Noise Frequency']
    Cycles = cfg['Number of Cycles']
    fs = data['samples']
    wave = cfg['Signal Type']
    amp = cfg['Signal Amplitude']


    Period = 1 / signal_freq
    duration = Cycles*Period
    samples = int(fs * duration)
    Tarray = np.linspace(0, duration, samples)
    phase = 2*np.pi*signal_freq*Tarray


    # Voltage formula = V = A sin(wt), where w = 2pi * f

    if wave == 'sin':
        # Voltage formula = V = A sin(wt), where w = 2pi * f
        V_signal = amp * np.sin(phase) 
    elif wave == 'square':
        V_signal = amp*signal.square(phase)

    elif wave == 'triangle':
        V_signal = amp*signal.sawtooth(phase, width=0.5)

    else:
        raise ValueError(f'Unknown signal type {wave}')

    def Noise_adder (Noise_level= np.linspace(0, 2, samples), totalS= samples):
        return np.random.normal(0, Noise_level, totalS)

    Vin = V_signal + Noise_adder()



        
    return Vin, V_signal, Tarray
git pull origin main --rebase
