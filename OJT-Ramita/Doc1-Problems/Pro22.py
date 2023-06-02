'''22. Find the palindrome words with the count value from the given string.Output
should be in form of dict. key will be palidrome word and value will be number of occurence.
i/p given a string - Nittin & his mom went to a park last friday. His Mom observed
that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then 
we also get 1331.
o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2} '''

st = '''Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331.'''

def countPanlindrome(st):
    di = {}
    li = st.split(" ")
    for i in li:
        if i[-1] in [".", ",", "?", ";", ":", "!"]:
            temp = i[:-1]
        else:
            temp = i
        if len(temp) > 1 and temp.lower() == temp[::-1].lower():
            if temp.lower() not in di:
                di[temp.lower()] = 1
            else:
                di[temp.lower()] += 1
    print(di)

countPanlindrome(st)
