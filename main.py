import matplotlib.pyplot as plt
import signal_gen
import circuit_components

def main():
    Vin, Time = signal_gen.generate_input_signal()
    Vamp = circuit_components.Non_Invert_OPamp(Vin)
    Vfilt = circuit_components.Low_PassFilter(Vamp)

    
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