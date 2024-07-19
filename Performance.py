from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os.path

csv_path = "classic_run3.csv"
try:
    file = open(csv_path, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["backendPerformance_calc","frontendPerformance_calc"])
except:
    print("error opening or writing to the CSV file!")
finally:
    file.close()

if os.path.isfile('PATH'):
    print ("Chrome WebDriver found")
else:
    print ("Chrome WebDriver not found!")
    exit()

driver = webdriver.Chrome('C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64')
hyperlink = "http://www.teamrge.com"
driver = webdriver.Chrome()

iterations = 100

for i in range(iterations):
    driver = webdriver.Chrome('C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64')
    driver.get(hyperlink)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart


    writer.writerow([backendPerformance_calc,frontendPerformance_calc])
    driver.close()
    print("start next iteration")

