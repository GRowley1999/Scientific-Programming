"""
Scientific Programming Check Point 5 Task 1
Gregor Rowley 
s1705159
"""
import matplotlib.pyplot as plt
import math

def get_variables():
    """Prompts the user to enter data required by the program."""
    v_initial = float(input("Please enter the magnitude of the intial velocity" 
        + "in ms^-1: "))
    theta = float(input("Please enter the angle from the horizontal of the" + 
        " initial velocity in degrees: "))
    beta = float(input("Please enter the normalised drag coefficient: "))
    delta_t = float(input("Please enter the time interval in seconds: "))

    return v_initial, theta, beta, delta_t

    
def set_initial(v_initial, theta):
    """   
    Set inital conditions for x and y components of position and velocity.
    """
    x = 0
    y = 0
    vx = v_initial*math.cos(math.radians(theta))
    vy = v_initial*math.sin(math.radians(theta))

    return x,y,vx,vy


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


def calculate_range(v_initial, theta):
    """Calculates the range of the projectile."""
    return ((v_initial**2)*math.sin(math.radians(2*theta)))/9.81


def plot_trajectory(x_values, y_values):
    """
    Plots the path of a projectile from launch to the point at which 
    it returns to the ground hence y = 0, acted on by gravity and drag.
    """
    plt.plot(x_values, y_values, "k-")
    plt.title("Trajectory of a projectile acted on by gravity and drag:")
    plt.xlabel("Horizontal Component of Displament (m)")
    plt.ylabel("Vertical Component of Displacement (m)")
    plt.show()

def main():
    """
    Main program to read in from terminal, do iteration, and plot out graph
    """
    # Gets the initial required data from the user.
    v_initial, theta, beta, delta_t = get_variables()
    # Sets the initial values of the position and velocity.
    x, y, vx, vy = set_initial(v_initial, theta)
    x_values = []
    y_values = []
    # Appends the initial positions to the lists containing the x and y
    # components of position.
    x_values.append(x)
    y_values.append(y)

    while(True):
        # Calls the step forward function to step each component of position and
        # velocity forward.
        step_forward_values = step_forward(x_values[-1], y_values[-1], vx, vy, 
            beta, delta_t)
        # Tests to see if the y component of position is greater than zero,
        # hence above the ground.
        if (step_forward_values[1]) > 0.0:
            # Appends the current x and y components of position to the lists of
            # x and y values.
            x_values.append(step_forward_values[0])
            y_values.append(step_forward_values[1])
            # Updates the latest horizontal and vertical velocities.
            vx = step_forward_values[2]
            vy = step_forward_values[3]
        else:
            # If the value tested in the if statement for vertical displacement
            # is found to be less than zero, the break statement is called, to
            # end the while loop.
            break

    plot_trajectory(x_values, y_values)

    # Prints the value of the projectile's range to the terminal.
    print("The range of this projectile is: " 
        + str(calculate_range(v_initial, theta)))

main()

    

