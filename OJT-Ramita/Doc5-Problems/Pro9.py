'''9.For the given sentence, return the average word length.
sentence = "I need to work very hard to learn more about algorithms in Python!" 
Note: Remember to remove punctuation first.'''

sentence = "I need to work very hard to learn more about algorithms in Python!"

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for ele in sentence:
    if ele in punc:
        sentence = sentence.replace(ele, "")

sentence = sentence.split(" ")
word_len = []

for ele in sentence:
    word_len.append(len(ele))

print(sum(word_len)//len(word_len))