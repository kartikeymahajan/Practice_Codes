import re
instr = "3*qaz, 1*q, 4*tr, 2*pop"

def func(st):
    # output = ""
    # st = st.split(",")
    # for i in st:
    #     temp = i.split("*")
    #     output += int(temp[0])*temp[1]
    # return output

    return "".join([int([j for j in i.split("*")][0])*[j for j in i.split("*")][1] for i in st.split(",")])


obj = func(instr)
print(obj)