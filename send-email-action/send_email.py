#!/usr/bin/env python

"""
Script Name: send_email.py
Description: This script sends an email using SMTP server configuration provided via environment variables.
Owner: DevOps Team
Usage:
    1. Ensure the following environment variables are set:
        - FROM_EMAIL: Sender's email address
        - TO_EMAIL: Recipient's email address
        - SMTP_SERVER: SMTP server address
        - SMTP_PORT: SMTP server port
    2. Run the script.
Note: If the connection to the SMTP server is blocked or the authentication fails, appropriate error messages will be displayed.
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    # Get environment variables
    sender_email = os.getenv('FROM_EMAIL')
    #receiver_email = os.getenv('TO_EMAIL')
    receiver_email = "ncmuthu@gmail.com, ncmuthuaws@gmail.com"

    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Email content
    #subject = 'Hello from GitHub Actions'
    #body = 'This is a test email sent from GitHub Actions.'
    subject = os.getenv('SUBJECT')
    body = os.getenv('MAIL_BODY')
    with open('body.html', "r") as file:
        html_content = file.read() 

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    ##
    # Open the file to be sent
    attachment_path="test.zip"
    with open(attachment_path, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send via email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    # Add attachment to message and convert message to string
    message.attach(part) 
    ##

    # Add body to email
    #message.attach(MIMEText(body, "plain"))
    message.attach(MIMEText(html_content, "html"))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email.split(", "), message.as_string())

    print('Email sent successfully!!')
    print(f"Receiver_email : {receiver_email}")

if __name__ == "__main__":
    send_email()
