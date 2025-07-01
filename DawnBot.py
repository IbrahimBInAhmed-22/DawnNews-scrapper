import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


def make_driver():
    driver = webdriver.Chrome()
    return driver

def scrap(query, r1, r2):
    driver = make_driver()
    driver.get(f"https://www.dawn.com/search?q={query}")
    time.sleep(30)
    page = 1
    records = []
    while True:
        print(f"Scrapping page number {page}....")
        results = driver.find_elements(By.CSS_SELECTOR,".gsc-webResult.gsc-result")
        if not results:
            print("No more result found...")
            break
        for result in results:
            body = result.find_element(By.CSS_SELECTOR, ".gs-title")
            # print(body.text)
            headline = body.text.strip()
            url = body.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            
            snippet = result.find_element(By.CSS_SELECTOR,".gs-snippet").text.strip()

            date, description = snippet.split("...")[:2]
            if inrange(r1, r2, date):
                records.append({
                "headline": headline,
                "url": url,
                "date": date,
                "description": description
            })
        break

    for record in records:
        print(f"Headline: {record['headline']}")
        print(f"URL: {record['url']}" )
        print(f"Date:  {record['date']}")
        print(f"Description: {record['description']}")
        print("-"*40)

    time.sleep(10)

    driver.quit()

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


def scrapper():
    r1 = ""
    r2 = ""
    while True:
        r1 = input("Enter the lower range (format: yyyy-mm-dd)")
        r2 = input("Enter the upper range (format: yyyy-mm-dd)")
        y, m, d = r1.split("-")
        y1, m1, d1 = r2.split("-")
        if y and m and d and y1 and m1 and d1:
            break
    query = input("Enter the city name whose news you want to extract...")
    scrap(query, r1, r2)

# inrange("0", 1, "13-Oct-2024")

def main():
    scrapper()


main()
