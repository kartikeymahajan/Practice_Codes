'''5.Let's consider there is a list which contains usernames, You have received requirement 
to add one more username to the list (without using append and assignment approaches)

input: ["user1","user2"]
output: ["user1","user2","user3"]'''

input_list = ["user1","user2"]
new_input = "user3"

input_list.extend([new_input])

print(input_list)