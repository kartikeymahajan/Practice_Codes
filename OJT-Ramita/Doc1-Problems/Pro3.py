'''3. Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this
tuple and the
output should also be in the form of tuple. Make a note that tuples are immutable in
nature so you
need to find some idea to make modification and print the updated tuple.'''

t1 = ("Msys", "Technologies", "2007")
s1 = "Python" 

t1 = tuple(list(t1)+[s1])

print(t1)
