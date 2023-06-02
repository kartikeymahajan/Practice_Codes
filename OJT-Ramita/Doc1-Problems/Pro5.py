'''5. Given a dictionary {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh',
'TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'} make a list of all the values 
associated with keys in alphabetically sorted order.'''

di = {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh',
'TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}

values_list = [ i for i in di.values()]
values_list.sort()
print(values_list)