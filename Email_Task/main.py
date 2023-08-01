import json
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# from memory_profiler import profile

# @profile
def send_Emails(data_file):
    """This is the main funtion which is used to send emails
    It takes a file which is having emails as a argument"""

    # Email configuration
    sender_email = "kartikeymahajan321@gmail.com"
    # receiver_email = "kmahajan@msystechnologies.com"

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "kartikeymahajan321@gmail.com"
    smtp_password = "ubcdwhdsqlgkgtqg"

    # Load recipient emails from JSON file
    data_file_path = f"F:\Kartikeya\Git\Email_Task\{data_file}"
    with open(data_file_path) as json_file:
        recipients = json.load(json_file)

    # Iterate over recipients and send emails
    for recipient in recipients:
        receiver_email = recipient["email"]
        reciver_name = recipient["name"]

        subject = f"Dummy Mail"
        message = f"""Hi {reciver_name},
    This is a auto-generated mail. 
    Please don't reply.
            
    Thanks and Regards,
    Kartikeya Mahajan"""

        # Create a multipart message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Add the message body
        msg.attach(MIMEText(message, "plain"))

        # List of files which is having file names in the directory
        files = ["file.txt", "file2.txt"]

        # Open the files to be attached
        for file in files:
            file_path = f"F:\Kartikeya\Git\Email_Task\{file}" 
            with open(file_path, "rb") as file:
                attachment = MIMEApplication(file.read(), _subtype="txt")
                attachment.add_header("Content-Disposition", "attachment", filename="file.txt")
                msg.attach(attachment)

        # Create a SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Enable TLS encryption
            server.starttls()

            # Login to the SMTP server
            server.login(smtp_username, smtp_password)

            # Send the email
            server.send_message(msg)

            print(f"Email sent successfully to {reciver_name}")

            # Delay between sending emails
            # time.sleep(2)  # Adjust the time interval as needed

file = "emails.json"
# while True:
#     send_Emails(file)
#     time.sleep(15)

send_Emails(file)

