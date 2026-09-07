from backend import extract_filing_documnets
from backend import create_document
from backend import create_chunks

doc = extract_filing_documnets()
doc = create_document(doc)
chunks = create_chunks(doc)
print(len(chunks))
print(chunks[0])


# import requests

# url = "https://www.sec.gov/files/company_tickers_exchange.json"
# headers = {"User-Agent":"Aditya Anand adianand069@gmail.com"}

# response = requests.get(url=url, headers=headers)
# response.raise_for_status()

# data = response.json()
# print(len(data["data"]))