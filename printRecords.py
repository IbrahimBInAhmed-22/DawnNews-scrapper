def PrintRecords(records =[]):
    for record in records:
        print(f"Headline: {record['headline']}")
        print(f"URL: {record['url']}" )
        print(f"Date:  {record['date']}")
        print(f"Description: {record['description']}")
        print("-"*40)
    