'''19.Define a generator to print the numbers between o to n (including) which are divisible 
by 5 and should be even

N = 20

Output : 10 20'''

def DivisibleByFive(N):
    for i in range(1,N+1):
        if i%5 == 0 and i%2 == 0:
            yield i

for i in DivisibleByFive(20):
    print(i)