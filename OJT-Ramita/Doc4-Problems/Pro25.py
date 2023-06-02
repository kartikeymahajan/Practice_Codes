'''25.Define a logic to print the combinations from the two the below input data Input:
{

'Department': ['Bakkt', 'Cisco'],

'Team'	: ['Red', 'Yellow', 'Black']

}

Output:



{ 'Department': 'Bakkt', 'Team': 'Red'},

{ 'Department': 'Bakkt', 'Team': 'Yellow'}

{ 'Department': 'Bakkt', 'Team': 'Block'}

{ 'Department': 'Cisco', 'Team': 'Red'}

{ 'Department': 'Cisco', 'Team': 'Block'}

{ 'Department': 'Cisco', 'Team': 'Yellow'}'''

data = {
    'Department': ['Bakkt', 'Cisco'],
    'Team'	: ['Red', 'Yellow', 'Black']
}

for i in data['Department']:
    for j in data['Team']:
        print({'Department':i, "Team":j})
    