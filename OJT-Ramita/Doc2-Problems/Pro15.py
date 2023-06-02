'''15. Write a function get_hypotenuse that returns the hypotenuse of a right triangle
given the other two sides.
>>> get_hypotenuse(0, 0)
0.0
>>> get_hypotenuse(3, 4)
5.0'''

def findHypotenuse(side1, side2):
    return (((side1 * side1) + (side2 * side2))**(1/2))

obj = findHypotenuse(5,5)
print(obj)
