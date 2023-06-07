
st = "kdfsjletoiewgldgkldjl"
def func1(st):
    i = 0
    end = len(st)
    while i < end:
        temp = st[i]
        st = st[:i]+st[i+1:]
        end -= 1
        if temp in st:
            j = 0
            while j < end and temp in st:
                if st[j] == temp:
                    st = st[:j]+st[j+1:]
                    end -= 1
                    j-=1
                j += 1
        else:
            st = st[:i] + temp + st[i:]
            end += 1
            i += 1
    return st

def func2(st):
    left = 0
    right = len(st)
    while left < right:
        temp = st[left]
        if st.count(temp)>1:
            while temp in st:
                index = st.find(temp)
                st = st[:index]+st[index+1:]
                right -= 1
        else:    
            left += 1
    return st

obj = func1(st)
obj2 = func2(st)
print(obj)
print(obj2)