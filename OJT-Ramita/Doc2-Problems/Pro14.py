'''14. Write a command-line program which helps a traveler keep track of the
restaurants they've visited in different cities and what they thought of each. The

program will accept two CSV files of restaurants, a "primary list" CSV and a
"sublist" one, and update the primary one with new restaurants from the trip one.'''

import pandas as pd

# Using Concat()
df1 = pd.read_csv('PrimaryList.csv')
df2 = pd.read_csv('Sublist.csv')

mainfile = pd.concat([df1, df2], ignore_index=True)

print(mainfile)
# ----------------------------------------------------------------------


# Using append()
# mainfile = pd.DataFrame()

# df1 = pd.read_csv('PrimaryList.csv')
# df2 = pd.read_csv('Sublist.csv')

# df1 = df1.append(df2, ignore_index = True)

# print(df1)

# ----------------------------------------------------------------------
# Using marge()

# df1 = pd.read_csv('PrimaryList.csv')
# df2 = pd.read_csv('Sublist.csv')

# df1 = df1.merge(df2, how='outer')

# print(df1)

