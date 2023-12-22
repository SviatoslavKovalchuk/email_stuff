import random
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import user_data

UNIQUE_SUBJECT_ID = random.randint(1111, 99999)


def send_email_via_smtp_ssl(
        recipients: list,
        subject: str,
        email_body: str = None,
        attachment_path: str = None):
    message = MIMEMultipart()
    message['From'] = user_data.ukr_net_user_mail
    message['To'] = ', '.join(recipients)
    message['Subject'] = subject
    body = email_body

    if email_body is not None:
        message.attach(MIMEText(body, 'plain'))
    if attachment_path:
        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f"attachment; filename= {attachment_path}")
        message.attach(part)
    try:
        with smtplib.SMTP_SSL('smtp.ukr.net', 465) as server:
            print(f'Login to the serv as {user_data.ukr_net_user_mail}')
            server.login(user_data.ukr_net_user_mail, user_data.ukr_net_password)
            print(f'Going to send email to {recipients}')
            server.sendmail(user_data.ukr_net_user_mail, recipients, message.as_string())
            print('Email sent successfully')
    except Exception as e:
        print(f'Error sending email: {e}')


if __name__ == "__main__":
    send_email_via_smtp_ssl(
        ['raptor-auto@raptorauto1.onmicrosoft.com'],
        f'CAPE:m6nMHb9oaaRi7:SCAM:tCpfQ5HDArSTc:MALICIOUS:585cHbRhx8bfd:HIGH, ID = {UNIQUE_SUBJECT_ID}')
