'''16.Write a function in Python that accepts one numeric parameter. 
This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value. 
Do not use inbuilt functions.
Note : Angle in Radians × 180°/π = Angle in Degrees.'''


def findDegree(AIR):
    return f"{round(AIR * 180 / 3.14,1)}°"

AIR = 0.524 # should be in range(0, 6.283)
obj = findDegree(AIR)
print(obj)
