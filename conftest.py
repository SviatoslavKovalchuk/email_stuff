import email
import imaplib
from user_data import user_data
import pytest
from CONSTANTS import ROOT_DIR
import os
from selenium import webdriver

abs_path_of_base_image_to_compare = f'{ROOT_DIR}/images/base_image_to_compare.jpeg'
abs_path_to_google_img = f'{ROOT_DIR}/images/google_logo.png'


@pytest.fixture
def create_server():
    server = imaplib.IMAP4_SSL('imap.ukr.net.', 993)
    return server


@pytest.fixture
def user():
    return 'sviatoslavio@ukr.net'


@pytest.fixture
def user_password():
    return '8HDwWLOaZuua147D'


@pytest.fixture
def login_to_ukr_net_via_imap(create_server, user, user_password):
    with create_server as imap_server:
        imap_server.login(user, user_password)
        imap_server.select()
        yield imap_server


@pytest.fixture
def email_parser(login_to_ukr_net_via_imap):
    _, messages = login_to_ukr_net_via_imap.search(
        None,
        '(FROM "sviatoslav.kovalchuk97@gmail.com")')
    emails_list = []
    for num in messages[0].split():
        _, data = login_to_ukr_net_via_imap.fetch(num, '(RFC822)')
        emails = email.message_from_bytes(data[0][1])
        emails_list.append(emails)
    if emails_list:
        return emails_list[-2]


@pytest.fixture
def base_image_to_compare():
    return abs_path_of_base_image_to_compare


@pytest.fixture
def google_image_to_compare():
    return abs_path_to_google_img


@pytest.fixture
def download_attachment_from_email():
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
        if emails.is_multipart():
            for part in emails.walk():
                if part.get_content_type().startswith('image/'):
                    attachment_file_from_body = part.get_filename()
                    attachment_path = os.path.join(f'{ROOT_DIR}/downloads', attachment_file_from_body)
                    with open(attachment_path, 'wb') as file:
                        file.write(part.get_payload(decode=True))
                    yield attachment_path
                    os.remove(attachment_path)
    imap_gmail_server.close()
    imap_gmail_server.logout()


@pytest.fixture
def create_driver_and_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com.ua/?hl=uk")
    yield driver
    driver.quit()
