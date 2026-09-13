import numpy as np
import json
from scipy import signal

with open("config.json", "r") as file:
    data = json.load(file)

components = data['components']

def Non_Invert_OPamp ( V, R1=1000, R2=3300, Vsat= 10):
    gain = 1 + (R2/R1) #for non inverting amp
    Vamped = np.array(V*gain) 
    Vamped = np.clip(a=Vamped, a_min=-Vsat, a_max=Vsat) # cannot exceed rail V
    return Vamped

def Low_PassFilter (V, R_Filter = components['lowpass filter']['R'], C_Filter = components['lowpass filter']['C'] ):
    
    Cutoff = 1/(2*np.pi*R_Filter*C_Filter) # for low pass cutoff is 1 / 2piRC
    sos = signal.butter(N=2, Wn=Cutoff, btype='lowpass', fs= data['samples'], output='sos') # 2nd order low pass filtering blueprint
    V_filtered = signal.sosfiltfilt (sos, V) # forward backward filtering to eleminate Capacitor lag
    return V_filtered


def High_PassFilter (V, R_Filter = components['highpass filter']['R'], C_Filter = components['highpass filter']['C'] ):
    Cutoff = 1/(2*np.pi*R_Filter*C_Filter) # for high pass cutoff is 1 / 2piRC
    sos = signal.butter(N=2, Wn=Cutoff, btype='highpass', fs= data['samples'], output='sos')
    V_filtered = signal.sosfiltfilt (sos, V) # forward backward filtering to eleminate Capacitor lag
    return V_filtered

def Band_PassFilter (V, R_Filter_lower = components['bandpass filter']['R_low_stage'], C_Filter_lower = components['bandpass filter']['C_low_stage'], R_Filter_higher = components['bandpass filter']['R_high_stage'], C_Filter_higher = components['bandpass filter']['C_high_stage']):
    Cutoff_Low = 1/(2*np.pi*R_Filter_lower*C_Filter_lower)
    Cutoff_High = 1/(2*np.pi*R_Filter_higher* C_Filter_higher)
    sos= signal.butter(N=2, Wn=[Cutoff_Low, Cutoff_High], btype='bandpass', fs= data['samples'], output='sos')
    V_filtered = signal.sosfiltfilt (sos, V) # forward backward filtering to eleminate Capacitor lag
    return V_filtered