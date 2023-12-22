import email
import imaplib

import pytest


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
        return emails_list[-1]
