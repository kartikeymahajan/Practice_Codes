'''Tue: 18-Oct-2022:problems:

1) Need to print prime numbers till 100'''

def prime_between(rangeFrom: int, rangeTo: int):   
    li = [] 
    for num in range(rangeFrom, rangeTo): #Traversing through given range.
        flag = True
        if num > 1:
            while flag:
                for i in range(2, num): 
                    if num % i == 0:
                        flag = False
                        break
                else:
                    li.append(num)
                    break
    return li

obj = prime_between(0,100)
print(obj)


'''2) Given list, need to find the duplicate number and missing number'''
def missing_or_doubled(inputlist):
    counts = {} 
    result =[]
    for n in inputlist: # Traversing through given list.
        counts[n] = counts.get(n, 0) + 1  # storing elements and their counts.
    
    start = min(counts) 
    end = max(counts)
    
    for i in range(start, end + 1):
        #Checking is the element having more than 1 count? or is the element is None? 
        # if yes appending element in result.
        if counts.get(i) in range(2, len(li)) or counts.get(i) is None: 
            result.append(i)

    return result

li = [28,31,31,29,30,33] 
obj = missing_or_doubled(li)
print(obj) # in result first one is repeating element and second is missing element.
