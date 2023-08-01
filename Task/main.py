import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import json

# port and server
smtp_port = 587
smtp_server = "smtp.gmail.com"

# email address from we sent the email
email_from = "areakingapp@gmail.com"

#email_list = ["areakingpanna@gmail.com","hemantkurmi1998@gmail.com"]


# authuntication password for the login of the email
PASSWORD = 'vbwmytcpdbajzohe'

# subject of the email
subject = "Email with attachments"


#message = 'Hey , I am Patel'


# fetch data from the json file
with open('Task/one.json',) as file:
    data = json.load(file)
data = data['recipients']


# this function takes data as the arguments and
# automatically send the email as the respectively data


def send_emails(data):
    # fetch one by one emails from the data
    for person in data:

        body = f"""
        Hi all,
        this is the python scripted program .
        Thanks & regards 
        Hemant Patel

"""
        
        # email formating
        msg = MIMEMultipart()
        msg['From'] = email_from # sender address
        msg['To'] = person  # reciever address
        msg['Subject'] = subject # subject of the email

        msg.attach(MIMEText(body,'plain')) # attachment of the email

        filename = 'Task/file.txt'    # filename is the variable that we pass indicate the file address

        attachment = open(filename,'rb')

        attachment_pakage = MIMEBase('application','octet-stream')
        attachment_pakage.set_payload((attachment).read())
        encoders.encode_base64(attachment_pakage)
        attachment_pakage.add_header('Content-Disposition',"attachments;filename="+filename)
        msg.attach(attachment_pakage)

        text = msg.as_string()

        print("Connecting to server.....")
        TIE_server = smtplib.SMTP(smtp_server,smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from,PASSWORD)
        print("Successfully connected to the server")
        print()

        print(f"sending email to {person}")
        TIE_server.sendmail(email_from,person,text)
        print(f"Email sent to {person}")
        print()

        TIE_server.quit()

# this is the time interval that takes the time to run the program
time_interval = 60 # in second

while True:
    if filesize > definedsize:
        send_emails(Email_data)
    else:
        send_emails(Email_data)
    time.sleep(time_interval)
    print('Email sent successfully.')
    