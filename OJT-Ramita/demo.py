import json

with open("emails.json") as json_file:
    recipients = json.load(json_file)

print(recipients)


for recipient in recipients:
    receiver_email = recipient["email"]
    print(receiver_email)