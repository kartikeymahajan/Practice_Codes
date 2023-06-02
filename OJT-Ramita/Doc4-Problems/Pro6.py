'''6.Define the logic for generating the email id based on username and department Get 
the username and department as a input and create a email id from it input:

username : msys 
department: automation
output: msys.automation@gmail.com
Note : Generated email id should contain @ and should end with .com'''

username = "msys" 
department = "automation"

print(f'{username}.{department}@gmail.com')
