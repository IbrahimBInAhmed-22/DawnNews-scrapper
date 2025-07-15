from utilities import make_driver, natural_wait
from scrapper import DawnNewsScrapper

def wrapper(queries, r1 , r2, records =[]):
    driver = make_driver()
    current_page  = 1
    check_point = ""

    tries = 0
    manual_removal = False
    while(True):
        try:
            natural_wait(5,6)
            manual_removal = False
            result = DawnNewsScrapper(queries, r1, r2, driver, current_page, records)
            if result is None:
                tries = 0
                break

            tries += 1
            if tries > 2:
                print("The CAPTCHA couldn't be removed automatically (remove it manually)")
                input("Press any key to continue...")
                manual_removal = True
                
        
            query, current_page = result
            queries = queries[queries.index(query): ]
            if not manual_removal:
                driver.quit()
                driver = make_driver()
        
        except Exception as e:
            print("Error ocurred while solving CAPTCHA, ERROR: ", e)
    driver.quit()