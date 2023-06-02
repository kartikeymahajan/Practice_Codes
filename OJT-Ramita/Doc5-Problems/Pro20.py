'''20.Use a nested list comprehension to find all of the numbers from 1-1000 
that are divisible by any single digit besides 1 (2-9)'''
result = []

result = [i for i in range(1,1000) if True in [True for j in range(2,10) if i % j == 0]]
print(len(result))

# result = []

# for i in range(1,1000):
#     for j in range(2, 10):
#         if i % j == 0:
#             result.append(i)
#             break
# print(result)

