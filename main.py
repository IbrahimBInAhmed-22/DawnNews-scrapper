
from printRecords import PrintRecords
from scrapWrapper import wrapper
from fileHandling import saveToFile
import time

def DawnNews(queries, r1, r2):

    records = []
    wrapper(queries, r1, r2, records)
    PrintRecords(records)
    saveToFile(records)

def main():
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
    query = [ "Lahore", "quetta"]
    DawnNews(query, r1, r2)


if __name__ == "__main__":
    main()

