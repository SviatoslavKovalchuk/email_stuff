import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from CONSTANTS import ROOT_DIR

FOLDER_TO_STORE_DOWNLOADED_IMAGE = f'{ROOT_DIR}/downloads'
IMAGE_FILE_PATH = os.path.join(FOLDER_TO_STORE_DOWNLOADED_IMAGE, 'google_logo.png')

driver = webdriver.Chrome()
driver.get("https://www.google.com.ua/?hl=uk")

google_logo_img = driver.find_element(By.XPATH, "//img[@src = '/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png']")
with open(IMAGE_FILE_PATH, 'wb') as GoogleLogoImage:
    GoogleLogoImage.write(google_logo_img.screenshot_as_png)

driver.quit()
