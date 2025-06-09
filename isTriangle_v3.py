import math

# This function takes input from the user
# and returns a list of floats (coordinates of a point)
def getPoint(n):
    while True:
        x = input(f"Enter the point {n} : ")
        xs = x.split()
        if len(xs) <= 1:                     
            print("Please enter atleast 2 values")
        else:
            try:
                fx = [float(item) for item in xs]
                return fx
            except ValueError:
                print("Please enter a valid point")

def distance(p1, p2):
    # Calculation of length of the sides using the distance formula
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))  # This sum() will iterate the (a[n] - b[n]) ^ 2 for the number of dimenstions (expantion of the dimensionality of the distance formula)

# This function checks if the points can form a triangle
def isTriangle(a, b, c):
   # global ab, bc, ac
    ab = distance(a, b)
    bc = distance(b, c)
    ac = distance(a, c)
    
    # Check if the sum of lengths of any two sides is greater than the third side i.e Triangular Inequality (a + b > c)
    return (ab + bc > ac) and (bc + ac > ab) and (ab + ac > bc)  

# loop to ensure all points are in the same dimension
while True:
    p1 = getPoint(1)
    p2 = getPoint(2)
    p3 = getPoint(3)

    if len(p1) == len(p2) and len(p2) == len(p3):   # Check if all points are in the same dimension
        break
    else:
        print("Enter all the points in the same the dimension")

if isTriangle(p1, p2, p3):
    print("The points can form a Triangle")
else:
    print("The points can't form a Triangle")

# print(f"Length of side AB: {ab} units")
# print(f"Length of side BC: {bc} units")   
# print(f"Length of side AC: {ac} units")
