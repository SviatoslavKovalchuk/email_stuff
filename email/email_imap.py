import email
import imaplib
from user_data import user_data


def imap_email_reader():
    imap_gmail_server = imaplib.IMAP4_SSL('imap.ukr.net.', 993)
    imap_gmail_server.login(
        user_data.ukr_net_user_mail,
        user_data.ukr_net_password)
    imap_gmail_server.select()
    _, messages = imap_gmail_server.search(
        None,
        '(SUBJECT "IMAGE WITH ATTACHMENT IN BODY")')
    for num in messages[0].split():
        _, data = imap_gmail_server.fetch(num, '(RFC822)')
        emails = email.message_from_bytes(data[0][1])
        print('== Email details =====')
        print(f'From: {emails["from"]}')
        print(f'To: {emails["to"]}')
        print(f'Cc: {emails["cc"]}')
        print(f'Subject: {emails["subject"]}')
        print('== Email Content =====')
        if emails.is_multipart():
            for part in emails.walk():
                if part.get_content_type() == 'text/plain':
                    print(part.get_payload(decode=True).decode('utf-8'))

        else:
            print(emails.get_payload(decode=True).decode('utf-8'))
        print('\n' + '=' * 30 + '\n')
    imap_gmail_server.close()
    imap_gmail_server.logout()


imap_email_reader()

