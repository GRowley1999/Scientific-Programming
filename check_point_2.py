import math

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


def calculate_complex_roots(a, b, c):
    """
    Calculates the roots of a quadratic with no real roots, hence complex
    roots.
    """
    # Calculates the real part of each of the two imaginary roots.
    real_part = -b/(2*a)
    # Calls the calculate_discriminant function, to get a value for the 
    # discriminant.
    discriminant = calculate_discriminant(a, b, c)
    # Calculates the imaginary part of each of the two imaginary roots.
    imaginary_part = math.sqrt(math.fabs(discriminant))/(2*a)

    return complex(real_part, imaginary_part)


def calculate_real_roots(a, b, c):
    """Calculates the roots of quadratic with two real roots."""
    # Calculates the discriminant by calling the calculate_discriminant 
    # function.
    discriminant = calculate_discriminant(a, b, c)
    if discriminant == 0:
        return -b/(2*a)
    else:
        # Calculates the first real root.
        root1 = (-b/(2*a)) - (math.sqrt(discriminant)/(2*a))
        # Calculates the second real root.
        root2 = (-b/(2*a)) + (math.sqrt(discriminant)/(2*a))

        return root1, root2


def calculate_roots(a, b, c):
    """
    Calculate the roots of a quadratic, using the function 
    calculate_discriminant to determine the nature of the roots to be 
    calculated.
    """
    # Checks to see if the disriminant is less than 0, if so it calls the 
    # calculate_complex_roots function.
    if calculate_discriminant(a, b, c) < 0:
        x= calculate_complex_roots(a, b ,c)
        return display_complex_roots(x)
    else:
        # If the discriminant is greater than or equal to zero, then an
        # if statement checks if the first coefficient is equal to zero or not,
        # if it is then the simple linear equation is solved for x, the one real
        # root.
        if a == 0:
            return display_roots(-c/b)
        else:
            if calculate_discriminant(a, b, c) == 0:
                x = calculate_real_roots(a, b, c)
                return display_roots(x)
            # If the first coefficient of the quadratic function is non-zero,
            # then the two real roots of the quadratic function are calculated,
            # by calling the calculate_real_roots function.
            else:
                x1, x2 = calculate_real_roots(a, b, c)
                return display_roots(x1, x2)


def display_roots(x1, x2=False):
    """
    Displays the roots of the quadratic function defined by the coefficents
    entered by the user.
    """
    if x2:
        print("The roots of the quadratic equation are: " +
            "x1 = {0:2.4f} & x2 = {1:2.4f}".format(x1, x2))
    else:
        print("This equation only has one solution: x = {0:2.2f}".format(x1))


def display_complex_roots(x):
    """
    Displays the complex roots of the quadratic function defined by the 
    coefficients entered by the user.
    """
    print("The roots of the quadratic equation are: " +
            "x1 = {0:2.1f} + {1:2.4f}i & ".format(x.real, x.imag) +
            "x2 = {0:2.1f} - {1:2.4f}i".format(x.real, x.imag))


def main():
    """
    The main function, where all other functions are called to be executed.
    """
    a, b, c = get_coefficients()
    if a == 0:
        calculate_roots(a, b, c)
    else:
        calculate_roots(a, b, c)

main()