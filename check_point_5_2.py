"""
Scientific Programming Check Point 5 Task 2
Gregor Rowley
s1705159
"""
import matplotlib.pyplot as plt
import math

def get_variables():
    """Prompts the user to enter data required by the program."""
    v_initial = float(input("Please enter the magnitude of the intial velocity" 
        + "in ms^-1: "))
    beta = float(input("Please enter the normalised drag coefficient: "))
    delta_t = float(input("Please enter the time interval in seconds: "))

    return v_initial, beta, delta_t


def set_initial(v_initial, theta):
    """
    Set inital conditions
    """
    vx = v_initial*math.cos(math.radians(theta))
    vy = v_initial*math.sin(math.radians(theta))

    return vx,vy


def acceleration(vx, vy, beta):
    """ 
    Calculate the acceleration 
    """
    # Calculates the magnitude of the acceleration
    maginitude_v = math.sqrt((vx**2) + (vy**2))
    # Calculates the x and y components of acceleration for the projectile.
    ax = (-beta)*maginitude_v*vx
    ay = ((-beta)*maginitude_v*vy)-9.81

    return ax, ay


def step_forward(x, y, vx, vy, beta, delta_t):
    """   
    Do a forward step
    """
    # Calls the acceleration function
    ax, ay = acceleration(vx, vy, beta)
    # Steps the x and y components of the position and velocity forward.
    x += (vx*delta_t) + (0.5*ax*math.pow(delta_t, 2))
    y += (vy*delta_t) + (0.5*ay*math.pow(delta_t, 2))
    vx += delta_t*ax
    vy += delta_t*ay

    return x, y, vx, vy


def calculate_kinetic_energy_ratio(v_initial, vx_final, vy_final):
    """Calculates the ratio of the final and initial kinetic energy"""
    
    v_final = math.sqrt((vx_final**2)+(vy_final**2))
    return (v_final**2)/(v_initial**2)



def plot_ratio_kinetic_energy(kinetic_energy_ratios, launch_angles):
    """
    Plots the path of a projectile from launch to the point at which 
    it returns to the ground hence y = 0, acted on by gravity and drag.
    """
    plt.plot(launch_angles, kinetic_energy_ratios, "k-")
    plt.title("Ratio of final kinetic energy to initial kinetic energy" + 
        " against lauch angle:")
    plt.xlabel("Launch Angle")
    plt.ylabel("Ratio of final kinetic energy to initial kinetic energy (J)")
    plt.show()


def main():
    """
    Main program to read in from terminal, do iteration, and plot out graph
    """
    # Gets the initial required data from the user.
    v_initial, beta, delta_t = get_variables()
    kinetic_energy_ratios = []
    launch_angles = []

    for launch_angle in range(91):
        x_values = []
        y_values = []
        # Appends the initial positions to the lists containing the x and y
        # components of position.
        x_values.append(0)
        y_values.append(0)
        # Sets the initial values of the velocity.
        vx, vy = set_initial(v_initial, launch_angle)
        while(True):
            # Calls the step forward function to step each component of position and
            # velocity forward.
            step_forward_values = step_forward(x_values[-1], y_values[-1], vx, 
                vy, beta, delta_t)
            # Tests to see if the y component of position is greater than zero,
            # hence above the ground.
            if (step_forward_values[1]) > 0.0:
            # Appends the current x and y components of position to the lists of
            # x and y values.
                x_values.append(step_forward_values[0])
                y_values.append(step_forward_values[1])
                vx = step_forward_values[2]
                vy = step_forward_values[3]
            else:
                # If the value tested in the if statement for vertical displacement
                # is found to be less than zero, the break statement is called, to
                # end the while loop.
                break
        # Calls the function to calculate the kinetic energy ratio and appends
        # it to the list of kinetic energy ratios for different lauch angles.
        kinetic_energy_ratio = calculate_kinetic_energy_ratio(v_initial, vx, vy)
        kinetic_energy_ratios.append(kinetic_energy_ratio)
        # Appends each launch angle to the list of launch angle.
        launch_angles.append(launch_angle)
    
    plot_ratio_kinetic_energy(kinetic_energy_ratios, launch_angles)

main()

