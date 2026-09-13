import matplotlib.pyplot as plt
import json
import signal_gen
import circuit_components

def main():
    with open("config.json", "r") as file:
        data= json.load(file)
    Vin, originalV, noiseV, Time = signal_gen.generate_input_signal()
    Vamp = circuit_components.Non_Invert_OPamp(Vin)
    try:
        if data['signal_gen']["Filter"] == "lowpass":
            Vfilt = circuit_components.Low_PassFilter(Vamp)
        elif data['signal_gen']["Filter"] == "highpass":
            Vfilt = circuit_components.High_PassFilter(Vamp)
        elif data['signal_gen']["Filter"] == "highpass":
            Vfilt = circuit_components.Band_PassFilter(Vamp)
    except:
        TypeError("Unknown Filter selection")
    
    plt.figure(figsize=(10, 7))

    #plot 1: Original Input signal
    plt.subplot(3, 1, 1)
    plt.plot(Time * 1000, Vin, color='orange')
    plt.title('Vin')
    plt.xlabel('Time in ms')
    plt.ylabel('Volts in V')
    plt.tight_layout()
    plt.grid(True)

    #plot 2: Amplified Input signal
    plt.subplot(3, 1, 2)
    plt.plot(Time * 1000, Vamp, color='red')
    plt.title('Vin Amplified')
    plt.xlabel('Time in ms')
    plt.ylabel('Volts in V')
    plt.grid(True)

    #Plot 3: Amplified and filtered signal
    plt.subplot(3, 1, 3)
    plt.plot(Time * 1000, Vfilt, color='green')
    plt.title('Vin Amplified and Filtered')
    plt.xlabel('Time in ms')
    plt.ylabel('Volts in V')
    plt.grid(True)

    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()