import matplotlib.pyplot as plt
import math

def get_variables():
    """
    Asks a user for the values of gamma, omega0 and the number of points to 
    plot on the graph.
    """
    gamma = float(input("Please enter a value for gamma: "))
    omega_zero = float(input("Please enter a value for omega: "))
    points = int(input("Please enter the number of points to plot on the " + 
        "graph: "))
    
    return gamma, omega_zero, points

def calculate_time(omega_zero, points, i):
    """Calculates the current time variable of the displacement."""
    return (5.0*math.pi*i/points)/omega_zero

def shm(omega_zero, gamma, t):
    """Calculates the displacement for a damped simple harmonic oscillator."""
    # Checks if the oscillator is critically damped, hence gamma == 2*omega_zero
    if gamma == 2*omega_zero:
            # Calculates the coefficient of damping b for a critically damped 
            # oscillator
            b = gamma/2
            return math.exp(-(gamma*t)/2)*(1+b*t)
    # Checks if the oscillator is over damped, hence gamma > 2*omega_zero
    elif gamma > 2*omega_zero:
            p = math.sqrt(((gamma**2)/4)-omega_zero**2)
            # Calculates the coefficient of damping b for an over damped
            # oscillator
            b = gamma/(2*p)
            return math.exp(-(gamma*t)/2)*(math.cosh(p*t)+b*math.sinh(p*t))
    # Checks if the oscillator is under damped, hence gamma < 2*omega_zero
    elif gamma < 2*omega_zero:
            omega = math.sqrt((omega_zero**2)-((gamma**2)/4))
            # Calculates the coefficient of damping b for an under damped
            # oscillator
            b = gamma/(2*omega)
            return math.exp(-(gamma*t)/2)*(math.cos(omega*t)+b*math.sin(omega*t))


def plot_amplitude_against_time(amplitudes, times, damping_type):
    """Plots the amplitude of a damped oscillator against time."""
    plt.plot(times, amplitudes, "k")
    plt.title("Amplitude vs Time for a%s Simple Harmonic Oscillator" % 
        (damping_type))
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude x(t) (m)")
    plt.show()

def main():
    """The main method executes the main functionality of the program."""
    gamma, omega_zero, points = get_variables()
    times = []
    amplitudes = []
    for i in range(0, points):
        # Calculates the time for each displacement.
        t = calculate_time(omega_zero, points, i)
        # Appends the current time to the list of times
        times.append(t)
        # Calculates the displacement at the current time and appends it to the 
        # list of amplitudes
        amplitudes.append(shm(omega_zero, gamma, t))

    # Checks if the oscillator is critically damped in order to change the title
    # of the plot accordingly
    if gamma == 2*omega_zero:
        plot_amplitude_against_time(amplitudes, times, " Critically Damped")
    # Checks if the oscillator is over damped in order to change the title
    # of the plot accordingly
    elif gamma > 2*omega_zero:
        plot_amplitude_against_time(amplitudes, times, "n Over Damped")
    # Checks if the oscillator is under damped in order to change the title
    # of the plot accordingly
    elif gamma < 2*omega_zero:
        plot_amplitude_against_time(amplitudes, times, "n Under Damped")        

main()