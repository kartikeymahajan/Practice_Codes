'''18. Create your own exception.'''

num = 4
try:
   result = num/0
except:
   print("Zero Division Error")
else:
   print(result)
