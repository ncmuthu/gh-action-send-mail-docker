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
#!/usr/bin/env python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # Get environment variables
    sender_email = os.getenv('FROM_EMAIL')
    receiver_email = os.getenv('TO_EMAIL')

    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Email content
    subject = 'Hello from GitHub Actions'
    body = 'This is a test email sent from GitHub Actions.'

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print('Email sent successfully!!')

if __name__ == "__main__":
    send_email()