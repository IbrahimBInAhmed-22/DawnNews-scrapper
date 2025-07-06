import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import random
import pandas as pd

def make_driver():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options = chrome_options)
    driver = webdriver.Chrome()

    return driver
def natural_wait(low_range = 5, high_range = 20):
    wait_time = random.uniform(low_range, high_range)
    time.sleep(wait_time)

def inrange(r1, r2, date):

    format_string = "%Y-%m-%d"

    r1 = datetime.strptime(r1, format_string)
    r2 = datetime.strptime(r2, format_string)

    d, m, y = date.split("-")
    d = int(d)
    y = int(y)
    m = monthToNumber(m)
    date = datetime(y, m, d)
    # print(type(date))
    return date <= r2 and date >= r1
def monthToNumber(month):
    return (datetime.strptime(month[:3].lower(),'%b').month)

def scrap(query, r1, r2):
    driver = make_driver()
    wait = WebDriverWait(driver, 2)
    action = ActionChains(driver)
    driver.get(f"https://www.dawn.com/search?q={query}")
    sleep = (input("How much wait do you want\n"))
    time.sleep(0)
    page = 0
    records = []

    
    pages = driver.find_elements(By.CSS_SELECTOR, ".gsc-cursor-page")
    no_of_pages = len(pages)
    for page in range(1,no_of_pages + 1):
        print(f"Scrapping page no: {page}...")
        try:
            print("Fetching results...")
            results = driver.find_elements(By.CSS_SELECTOR,".gsc-webResult.gsc-result")

            if not results:
                print("No more result found...")

            for result in results:

                try:
                    body = result.find_element(By.CSS_SELECTOR, ".gs-title")
                    headline = body.text.strip()
                    url = body.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
                    snippet = result.find_element(By.CSS_SELECTOR,".gs-snippet").text.strip()
                    date, description = snippet.split("...")[:2]
                except Exception as e:
                    print(f"Error while fetching result{page}, {e}")

                if inrange(r1, r2, date):
                    records.append({
                    "headline": headline,
                    "url": url,
                    "date": date,
                    "description": description
                })
            # -------------------------commented out next line for better understanding----------------------------------#

            #nxt_button = driver.find_element(By.XPATH, f"//div[contains(@class, 'gsc-cursor-page') and @aria-label='Page {page + 1}']")
            nxt_button = driver.find_element(By.XPATH, f"//div[@class ='gsc-cursor-page' and @aria-label='Page {page + 1}']")
            driver.execute_script("arguments[0].scrollIntoView(true);", nxt_button)
            natural_wait(3, 5)
            nxt_button.click()
            natural_wait(2, 4)
        except Exception as e:
            print(f"Couldn't find results: ",e)



    for record in records:
        print(f"Headline: {record['headline']}")
        print(f"URL: {record['url']}" )
        print(f"Date:  {record['date']}")
        print(f"Description: {record['description']}")
        print("-"*40)

    data = pd.DataFrame(records)
    with pd.ExcelWriter(f"U:\\university\\4thSummerBreak\\python\\DawnNews.xlsx" , engine = "openpyxl") as writer: 
        data.to_excel(writer,index = False)
    driver.quit()
def scrapper():
    r1 = "2024-01-01"
    r2 = "2025-12-01"
    # while True:
    #     r1 = input("Enter the lower range (format: yyyy-mm-dd)")
    #     r2 = input("Enter the upper range (format: yyyy-mm-dd)")
    #     y, m, d = r1.split("-")
    #     y1, m1, d1 = r2.split("-")
    #     if y and m and d and y1 and m1 and d1:
    #         break
    # query = input("Enter the city name whose news you want to extract...")
    query = "Lahore"
    scrap(query, r1, r2)

def main():
    scrapper()


main()
