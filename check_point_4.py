# Check Point 4 Task
# Gregor Rowley s1705159

import matplotlib.pyplot as plt
import math

def read_data(filename):
    """
    Reads the voltage and current data from the file provided by the user.
    """
    # List to store the voltages from the file. 
    voltages = []
    # List to store the currents from the file.
    currents = []
    # Opens the file, creating a file object named f_obj and closes the file,
    # once all work has been completed on the file.
    with open(filename) as f_obj:
        # Loops through each line read in from the sample.txt file.
        for line in f_obj.readlines():
            # Checks if each line read in from the file begins with a #, if it
            # does, the program is instructed to skip to the next loop and hence
            # the next line in the file.
            if line.startswith("#"):
                continue
            # If the line read in from the file is found not to begin with a #,
            # it is split on the delimeter of the comma between the voltage and
            # current reading and stored in a two item list of strings, token.
            tokens = line.split(",")
            # Appends the first item stored in the tokens list, hence the 
            # voltage in the list of voltages.
            voltages.append(float(tokens[0]))
            # Appends the second item stored in the tokens list, hence the
            # current in the list of currents.
            currents.append(float(tokens[1]))
    return voltages, currents


def logpower(voltage, current):
    """Calculates the log power of the product of voltage and current."""
    return math.log(voltage*current) 


def plot_logpower_data(log_powers, times):
    """Plots the logpower of the product of voltage and current against time."""
    plt.plot(times, log_powers, "k-")
    plt.title("Change in power over time for an electronic circuit:")
    plt.xlabel("Time (s)")
    plt.ylabel("Power (W)")
    plt.show()


def main():
    """Executes the main functionality of the program.""" 
    # Prompts a user for a filename from which to read data, and stores it as a
    # string in filename.
    filename = input("Please enter a file name to be read: ")
    # Calls the read_data method with the filename provided by a user as an
    # argument, which returns a tuple, containing two lists, one of voltages and
    # one of currents and stores them in two separate variables.
    voltages, currents = read_data(filename)
    times = []
    log_powers = []
    # Loops through the range 0 to the number of readings, hence the length of
    # voltage, list.
    for i in range(len(voltages)):
        # For each number in the loop range divides by the rate at which
        # readings are recorded to derive the time and appends it to the list of
        # times.
        times.append(i/25000)
        # Calls the logpower function with a the currently accessed voltage and
        # time and appends the result to the log_powers list.
        log_powers.append(logpower(voltages[i], currents[i]))
    # Calls the plot_logpower_data function to plot the power against time.
    plot_logpower_data(log_powers, times)

main()