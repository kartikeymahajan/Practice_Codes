'''4. In the dictionary {'India':'New Delhi', 'USA':'Washington D.C.',
'Nepal':'Kathmandu'} list out all the keys in a list named as 'list_keys' and list out all 
the values in a list named as 'list_values'.
Also find out the value of key 'Australia' in the list and as it is not existing in the list
print 'NA' as its value.'''

di = {'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'}

list_keys = [i for i in di.keys()]
list_values = [i for i in di.values()]

if "Australia" in di:
    print(di["Australia"])
else:
    print("NA")