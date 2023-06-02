'''7. Write a function that accepts two strings and returns True if the two strings are
anagrams of each other.'''

def check_anagram(str1, str2):
    return sorted(str1)==sorted(str2)

str1 = "care"
str2 = "race"
obj = check_anagram(str1,str2)
print(obj)