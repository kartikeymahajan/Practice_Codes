'''14.Define a function which can read json file and displays the data present in it to 
the console in dictionary format
Note : Please create .json file and store the sample data in it and read the json file, 
display the data in dictionary format'''

import pandas as pd
import json

f = open("sample1.json", "r")

data = json.loads(f.read())
print(data)


# data = json.load(f)

# for i in data:
#     print(i)
# result = pd.read_json("sample1.json")
# print(result)

