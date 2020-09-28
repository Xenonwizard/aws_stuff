from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import hashlib
import random
import string
import time
import os

options = Options()

options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = browser = webdriver.Chrome(options=options)

letters = string.ascii_letters
queryString = ''.join(random.choice(letters) for i in range(10))

ip = os.environ["ip"]
url = f"{ip}?id={queryString}"


def tc001():
    driver.get(f"http://{url}")
    time.sleep(2.5)

    hashFound = driver.find_element_by_xpath("/html/body/pre").text
    hashCheck = hashlib.sha512(f"{queryString}".encode("utf-8")).hexdigest()

    assert hashFound == hashCheck, "Wrong hash"

    print("Correct hash")
    driver.quit()


tc001()