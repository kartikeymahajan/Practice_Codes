equations = ["c==c","b==d","x!=z"]
for i in equations:
    exec(f'{i[0]} = 1')
    exec(f'{i[3]} = 1')
    print(c)
print(equations)f'{e[0]}'