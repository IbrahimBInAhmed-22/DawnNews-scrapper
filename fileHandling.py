import pandas as pd
def saveToFile(records):
    data = pd.DataFrame(records)
    with pd.ExcelWriter(f"DawnNews.xlsx" , engine = "openpyxl") as writer: 
        data.to_excel(writer,index = False) 