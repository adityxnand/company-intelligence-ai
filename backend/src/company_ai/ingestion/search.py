import requests


def get_companies()->dict:

    # Fetch all listed companies from SEC EDGAR API and returns as a DICT

    url = "https://www.sec.gov/files/company_tickers_exchange.json"
    headers = {"User-Agent":"Aditya Anand adianand069@gmail.com"}

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    data = response.json() # {"fields: ["cik", "name", "ticker", "exhange"], "data": [12345, "Apple Inc.","AAPL",YYYY]"}
    return data

if __name__ == "__main__":
    get_companies()