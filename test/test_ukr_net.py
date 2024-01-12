from PIL import Image
import imagehash
from selenium.webdriver.common.by import By
from CONSTANTS import ROOT_DIR
import os

FOLDER_TO_STORE_DOWNLOADED_IMAGE = f'{ROOT_DIR}/downloads'
IMAGE_FILE_PATH = os.path.join(FOLDER_TO_STORE_DOWNLOADED_IMAGE, 'google_logo.png')


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


def test_check_difference_of_image_preview(download_attachment_from_email, base_image_to_compare):
    image_to_compare = imagehash.average_hash(Image.open(base_image_to_compare))
    image_from_email = imagehash.average_hash(Image.open(download_attachment_from_email))
    assert image_to_compare == image_from_email


def test_download_image_and_compare(create_driver_and_login, google_image_to_compare):
    google_logo_img = create_driver_and_login.find_element(By.XPATH,
    "//img[@src = '/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png']")
    with open(IMAGE_FILE_PATH, 'wb') as GoogleLogoImage:
        GoogleLogoImage.write(google_logo_img.screenshot_as_png)
    downloaded_image = imagehash.average_hash(Image.open(IMAGE_FILE_PATH))
    base_image_to_compare = imagehash.average_hash(Image.open(google_image_to_compare))
    assert downloaded_image == base_image_to_compare
    os.remove(IMAGE_FILE_PATH)
