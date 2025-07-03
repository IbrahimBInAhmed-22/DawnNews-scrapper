from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time

def make_driver():
    driver = webdriver.Chrome()
    return driver
def natural_wait(low_range = 5, high_range = 20):
    wait_time = random.uniform(low_range, high_range)
    time.sleep(wait_time)
def main():
    driver = make_driver()
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)
    try:
        print("Opening AliExpress...")
        driver.get("https://aliexpress.com")
        close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pop-close-btn")))
        print("Button Detected...")
        close_button.click()
        print("PopUp closed....")
    except TimeoutException:
        print("Timeout while surfing...")


main()

