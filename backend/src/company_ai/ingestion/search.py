import requests

url = "https://www.sec.gov/files/company_tickers_exchange.json"
headers = {"User-Agent":"Aditya Anand adianand069@gmail.com"}

response = requests.get(url=url, headers=headers)
response.raise_for_status()

data = response.json()
print(len(data["data"]))