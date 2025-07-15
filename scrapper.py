from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from botDetected import BotDetected
from utilities import natural_wait, inrange


def DawnNewsScrapper(queries, r1, r2, driver, current_page = 1, records = []):
    natural_wait(4, 5)
    print("Starting Dawn News Scrapper...")
    for query in queries:
        try:
            check_point = query
            wait = WebDriverWait(driver, 20)
            action = ActionChains(driver)
            driver.get(f"https://www.dawn.com/search?q={query}")
            natural_wait(3, 5)

            if(BotDetected(driver,current_page)):
                return query, current_page
            
            pages = driver.find_elements(By.CSS_SELECTOR, ".gsc-cursor-page")
            no_of_pages = len(pages)

            for page in range(current_page,no_of_pages):


                nxt_button = driver.find_element(By.XPATH, f"//div[@class ='gsc-cursor-page' and @aria-label='Page {page + 1}']")
                driver.execute_script("arguments[0].scrollIntoView(true);", nxt_button)
                natural_wait(3, 5)
                nxt_button.click()
                natural_wait(3, 5)
                
                print(f"Scrapping page no: {page}...")
                current_page = page 
                if (BotDetected(driver, page)):
                    return query, current_page
                
                
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

                            details = snippet.split("...") 
                            if (len(details) >=2 ):
                                date, description = details[0].strip(), details[1].strip()
                            else:
                                date = "Unknown"
                                description = snippet.strip()
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

                
                except Exception as e:
                    print(f"Error while finding results: ",e)
                
                current_page = 1

        except Exception as e:
            print("There was an error while searching query ,", check_point, "Error: ",e)
            
    return None
