'''8. Take the input marks from user using input() function and find out the grade of the
students. Note the grading will be in this 
manner - (100 - 91) - A1, (90 - 81) - A2, (80 - 71) - B1, (70 - 61) - B2, (60 - 51) - C1 (50-40) - 
C2 and less than 40 students will 'Fail'. Also make sure user should input the marks in 
the range 0&lt;=marks&lt;=100, if user will input some other marks in should print invalid marks.'''

marks = int(input("Please Enter your Marks: "))

if marks in range(91,101):
    print("A1")
elif marks in range(81, 91):
    print("A2")
elif marks in range(71, 81):
    print("B1")
elif marks in range(61, 71):
    print("B2")
elif marks in range(51, 61):
    print("C1")
elif marks in range(40, 51):
    print("C2")
elif marks < 40:
    print("Fail")
else:
    print("Invalid Marks!")





