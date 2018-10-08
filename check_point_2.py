import cmath

def get_coefficients():
    """
    Prompts the user to enter the three coefficients of a quadratic function.
    """
    # x^2 coefficient
    a = float(input("Please enter the x^2 coefficent: "))
    if a == "":
        a = 0
    # x coefficient
    b = float(input("Please enter the x coefficent: "))
    # Constant term
    c = float(input("Please enter the constant term: "))

    return a, b, c


def calculate_discriminant(a, b, c):
    """
    Calculates the discriminant of a quadratic with the coefficients, 
    entered by the user.
    """
    return b*b - 4 * a * c


def calculate_roots(a, b, c, discriminant):
    """
    Calculates the roots or solutions of a quadratic function, both real and
    complex.
    """
    if a == 0:
        display_roots(-c/b)
    elif discriminant == 0:
        display_roots(-b/(2*a))
    elif discriminant < 0:
        root1 = -b/(2*a) + cmath.sqrt(abs(discriminant))/(2*a)*1j
        root2 = -b/(2*a) - cmath.sqrt(abs(discriminant))/(2*a)*1j
        
        display_roots(root1, root2)
    elif discriminant > 0:
        root1 = -b/(2*a) + cmath.sqrt(discriminant)/(2*a)
        root2 = -b/(2*a) + cmath.sqrt(discriminant)/(2*a)

        display_roots(root1, root2)
        

def display_roots(root1, root2=False):
    """Displays the roots of the quadratic function."""    
    if root2:
        print("The roots of the quadratic equation are: " +
            "x1 = {0:2.4f} & x2 = {1:2.4f}".format(root1, root2))
    else:
        print("This equation only has one solution, x = {0:2.1f}".format(root1))


def main():
    """
    The main function, where all other functions are called to be executed.
    """
    a, b, c = get_coefficients()
    discriminant = calculate_discriminant(a, b, c)
    calculate_roots(a, b, c, discriminant)

main()