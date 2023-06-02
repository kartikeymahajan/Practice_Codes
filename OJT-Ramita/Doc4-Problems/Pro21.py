'''21.Imagine a scenario where you are required to fetch the employee names who joined after 
02 Sep 2022 and location is Hyderabad
employee_ '''

data= {
    "priya":{
        "location"	: "Hyderabad" ,
        "joining_date ": "05/09/2022"
    },
    "mahi": {
        "location"	: "Bangalore",
        "joining_date ": "20/02/2023"
    },
    "raja": {
        "location"	: "Hyderabad", 
        "joining_date ": "14/10/2022"
    },

    "prabhu":{
        "location"	: "Bangalore", 
        "joining_date ": "02/01/2023"
    }
}

import datetime
for i in data:
    temp = data[i]["joining_date "]
    dt = datetime.datetime.strptime(temp,'%d/%m/%Y')
    # print(datetime.datetime("2022/9/2", "%Y/%m/%d"))
    if data[i]["location"] == "Hyderabad" and dt > datetime.datetime.strptime("2022/9/2", "%Y/%m/%d"):
        print(i)

