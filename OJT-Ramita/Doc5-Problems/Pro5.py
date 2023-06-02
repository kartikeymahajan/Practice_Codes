'''5.From given list of numbers, create a list of square of prime numbers . 
l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]'''

l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30, 17, 9, 81, 49]

def func(l1):
    for l in l1:
        temp = l//2
        for i in range(temp+1):
            if i*i == l:
                print(i, l)
                
func(l1)




