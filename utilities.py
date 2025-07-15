from selenium import webdriver
import time
import random
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait

def make_driver():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options = chrome_options)
    driver = webdriver.Firefox()
    #hello

    return driver
def natural_wait(low_range = 5, high_range = 20):
    wait_time = random.uniform(low_range, high_range)
    time.sleep(wait_time)

def inrange(r1, r2, date):
    if(date.find("hours") != -1):
        return True
    if(len(date.split("-")) < 3):
        return False
    date_no = 0
    if(date.find("days")):
        date_no = int([digit for digit in date if digit.isdigit()][0])

    format_string = "%Y-%m-%d"

    r1 = datetime.strptime(r1, format_string)
    r2 = datetime.strptime(r2, format_string)

    d, m, y = date.split("-")
    d = int(d)
    y = int(y)
    m = monthToNumber(m)
    date = datetime(y, m, d) - timedelta(days = date_no)
    # print(type(date))
    return date <= r2 and date >= r1
def monthToNumber(month):
    return (datetime.strptime(month[:3].lower(),'%b').month)