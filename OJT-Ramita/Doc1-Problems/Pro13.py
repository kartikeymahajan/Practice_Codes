'''13. Write a lambda function which takes two input arguments x and y. If x is greater
than y then it
should return square of y and if y is greater than x, then it should return square of x.'''

lam = lambda x, y: y*y if x > y else x*x
print(lam(8,6))