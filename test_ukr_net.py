
def test_simple_assert_ukr_net(login_to_ukr_net_via_imap, email_parser):
    data = email_parser
    assert data['Subject'] == 'Test'
    assert 'sviatoslav.kovalchuk97@gmail.com' in data['From']
    assert data['To'] == 'sviatoslavio@ukr.net'
    expected_text = 'Test Assert Python'
    for part in data.walk():
        if part.get_content_type() == 'text/plain':
            assert expected_text in part.get_payload()
