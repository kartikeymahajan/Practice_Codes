'''17. Write a program to replace duplicate adjacent alphabets from given string with '_'.
For Example -- input given string : 'abcdaa hssbbye' and output : 'abcda_ hs_b_ye' '''

def replaceDuplicates(st):
    for i in range(len(st)):
        if st[i] == st[i-1]:
            st = st[:i]+"_"+st[i+1:]
    print(st)

st = 'abcdaa hssbbye'
replaceDuplicates(st)