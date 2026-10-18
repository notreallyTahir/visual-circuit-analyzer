def Invert_OPamp (V, R1= 1000, R2= 3300, Vsat= 10):
    gain = -(R2/R1) 
    Vamped = np.array(V*gain)
    Vamped = np.clip(a=Vamped,a_min=-Vsat, a_max=Vsat)
