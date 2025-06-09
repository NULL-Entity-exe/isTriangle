# Function to find whether 3 points can form a triangle
# This is done by me as an experiment

import math

# This function takes input from the user
# and returns a list of floats (coordinates of a point)
def getPoint(n):
    while True:
        x = input(f"Enter the point {n} : ")
        xs = x.split()
        if len(xs) != 2:                     
            print("Please enter 2 values")
        else:
            try:
                fx = [float(item) for item in xs]
                return fx
            except ValueError:
                print("Please enter a valid point")


# This function checks if the points can form a triangle
def isTriangle(a, b, c):
    if (a[0] == b[0] == c[0]) or (a[1] == b[1] == c[1]):    # Not actual calculation; just to optimize the code
        return False
    else:
        # Calculation of length of the sides using the distance formula
        ab = math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
        bc = math.sqrt(((b[0] - c[0]) ** 2) + ((b[1] - c[1]) ** 2))
        ac = math.sqrt(((a[0] - c[0]) ** 2) + ((a[1] - c[1]) ** 2))

        # Check if the sum of lengths of any two sides is greater than the third side i.e Triangular Inequality (a + b > c)
        if (ab + bc > ac) and (bc + ac > ab) and (ab + ac > bc):
            return True
        else:
            return False


p1 = getPoint(1)
p2 = getPoint(2)
p3 = getPoint(3)

if isTriangle(p1, p2, p3):
    print("The points can form a Triangle")
else:
    print("The points can't form a Triangle")
