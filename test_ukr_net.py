
def test_asert_data_subject(login_to_ukr_net_via_imap, email_parser):
    data = email_parser
    assert data['Subject'] == 'Test'


def test_asert_email(login_to_ukr_net_via_imap, email_parser):
    data = email_parser
    assert 'sviatoslav.kovalchuk97@gmail.com' in data['From']


def test_asert_data_to(login_to_ukr_net_via_imap, email_parser):
    data = email_parser
    assert data['To'] == 'sviatoslavio@ukr.net'


def test_expected_text_in_email_body(login_to_ukr_net_via_imap, email_parser):
    data = email_parser
    expected_text = 'Test Assert Python'
    for part in data.walk():
        if part.get_content_type() == 'text/plain':
            assert expected_text in part.get_payload()
