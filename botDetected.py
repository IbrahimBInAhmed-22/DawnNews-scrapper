from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utilities import natural_wait

def BotDetected(driver, page):

    try:
        driver.find_element(By.ID, "recaptcha-wrapper")
        print(f"The bot was flagged on page {page}.\n Reloading the page...")
    except NoSuchElementException:
        return False

    return True
