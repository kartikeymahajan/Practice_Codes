'''25. Given an Integer n, count the total number of times 1 is appearing in all non-
negative integers
less than or equal to n.
Ex - n = 13, output should be 6
method - 1 is coming 6 times starting from number 0 till 13 in '1', '10', '11', '12', '13'.
Also note 1
is coming 2 times in 11. That is why 6 is the output'''

def countOne(num):
    count = 0
    for i in range(num+1):
        temp = str(i)
        for j in range(len(temp)):
            if temp[j] == "1":
                count += 1
    return count

obj = countOne(14)
print(obj)