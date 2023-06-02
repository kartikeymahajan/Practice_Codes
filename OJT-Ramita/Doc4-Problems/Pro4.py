'''4.Define a function which returns dictionary that stores the words and it's length 
from the given text
text = "Be happy"
Expected Output: {"Be":2,"happy":5}'''


def WordsCount(text):
    op = {}
    text = text.split(" ")
    for i in text:
        op[i] = len(i)
    return op

text = "Be happy"
obj = WordsCount(text)
print(obj)