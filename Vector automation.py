from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import shutil


# Open Chrome browser in incognito mode
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://vectorization.eu/")

# Wait for the cookie banner to appear and click accept
wait = WebDriverWait(driver, 4)
cookie_banner = driver.find_element(By.CLASS_NAME, "css-47sehv")
cookie_banner.click()

# Wait till the upload button is visible
wait = WebDriverWait(driver, 4)
file_input = driver.find_element(By.CSS_SELECTOR, '.col-md-12.col-2')
file_input.click()

# Wait for the dropdown menu to appear and select the svg output option
choose = driver.find_element(By.CSS_SELECTOR, '.col-md-12.col-3 select')
dropdownmenu = Select(choose)
dropdownmenu.select_by_value('svg')

# Wait for the "start_conversion" button to appear and click on it
start_conversion = driver.find_element(By.CSS_SELECTOR, '.col-md-12.col-4')
start_conversion.click()

# Keep trying to convert untill download link is visible
MAX_TRIES = 20
for i in range(MAX_TRIES):
    try:
        start_conversion.click()
        download_link = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@download]')))
        download_link.click()
        break
    except TimeoutException:
        if i + 1 == MAX_TRIES:
            raise Exception("Reached maximum number of tries, download not found")
        try:
            missing_data = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="missing data"]')))
            continue
        except TimeoutException:
            pass

# Wait till the script is finished downloading and open the download folder
time.sleep(1)
folder_path = 'C:\\Users\\Łukasz\\Downloads'
os.startfile(folder_path)

