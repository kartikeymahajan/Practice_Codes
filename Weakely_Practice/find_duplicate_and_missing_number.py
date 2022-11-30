
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
