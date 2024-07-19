
from selenium import webdriver
from selenium.webdriver.chrome import service, options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64./chromedriver.exe')

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(20)  # seconds

try:
    driver.get('https://www.amazon.com/performance')

    load_time_element = driver.find_element(By.ID, 'loadTime')
    load_time = load_time_element.text
    print(f"Page load time: {load_time}")

    requests_element = driver.find_element(By.ID, 'numRequests')
    num_requests = requests_element.text
    print(f"Number of requests: {num_requests}")


finally:
    driver.quit()

