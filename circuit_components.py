import numpy as np
from scipy import signal

def Non_Invert_OPamp ( V, R1=1000, R2=3300, Vsat= 10):
    gain = 1 + (R2/R1) #for non inverting amp
    Vamped = np.array(V*gain) 
    Vamped = np.clip(a=Vamped, a_min=-Vsat, a_max=Vsat) # cannot exceed rail V
    return Vamped

def Low_PassFilter (V, R_Filter = 1000, C_Filter = 100e-9 ):
    Cutoff = 1/(2*np.pi*R_Filter*C_Filter) # for low pass cutoff is 1 / 2piRC
    sos = signal.butter(N=2, Wn=Cutoff, btype='lowpass', fs=100000, output='sos') # 2nd order low pass filtering blueprint
    V_filtered = signal.sosfiltfilt (sos, V) # forward backward filtering to eleminate Capacitor lag
    return V_filtered