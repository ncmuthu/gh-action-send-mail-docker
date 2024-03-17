#!/usr/bin/env python
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password, subject, body):
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    try:
        # Send email with timeout
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')
    except smtplib.SMTPConnectError:
        print('Connection timed out. Unable to connect to SMTP server.')
        exit(1)  # Exit with non-zero status
    except smtplib.SMTPAuthenticationError:
        print('Authentication error. Check SMTP username and password.')
        exit(1)  # Exit with non-zero status
    except Exception as e:
        print(f'An error occurred: {e}')
        exit(1)  # Exit with non-zero status

def main():
    parser = argparse.ArgumentParser(description='Send an email using SMTP server configuration.')
    parser.add_argument('--sender-email', required=True, help='Sender\'s email address')
    parser.add_argument('--receiver-email', required=True, help='Recipient\'s email address')
    parser.add_argument('--smtp-server', required=True, help='SMTP server address')
    parser.add_argument('--smtp-port', type=int, required=True, help='SMTP server port')
    parser.add_argument('--smtp-username', required=True, help='SMTP server username')
    parser.add_argument('--smtp-password', required=True, help='SMTP server password')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body')
    args = parser.parse_args()

    send_email(args.sender_email, args.receiver_email, args.smtp_server, args.smtp_port, args.smtp_username, args.smtp_password, args.subject, args.body)

if __name__ == "__main__":
    main()
