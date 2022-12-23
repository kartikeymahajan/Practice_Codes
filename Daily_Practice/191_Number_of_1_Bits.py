def hammingWeight( n, count=0):
    return bin(n).count('1')
    # return hammingWeight(n & n-1, count+1) if n!=0 else count
n = 0b00000000000000000000000000001011
op = hammingWeight(n)
print(op)