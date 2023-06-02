'''22.Define the logic for verifying whether URL is Valid or Invalid Requirements for Valid URL·
•Should not contain any Special characters[,*,&,%,$,#,@,!] and Spaces
•Should start with https://
Input: URLs will be stored inside a file , read the URLs from the input file [input.txt]
Output: Generate a .txt file which contains the information whether URL is valid or not 
(URL, Status [valid/invalid])

Example:

Input
lnput.txt [text file]
https://m http s://m
Output:
1.https://m, valid
2.http s://m, invalid

Note: Define the logic with different approaches [1. Using RegEx 2. Without RegEx]'''

with open("input.txt") as file:
    for item in file:
        for i in ["*","&","%","$","#","@","!"," "]:
            if i in item:
                break
        
        
