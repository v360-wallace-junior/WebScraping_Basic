from src.yaholl_apple_finance import extract_quote_data
from src.sp500_companies_extract import extract_sp500_companies
from src.utils import get_response


# URL_TEMPLATE = "https://finance.yahoo.com/quote/{symbol}/"
# HEADERS = {"User-Agent": "Mozilla/5.0"}

HEADERS = {"User-Agent": "Mozilla/5.0"}
URL_TEMPLATE = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


def apple_finance_datails() -> None:
    symbol = "AAPL"
    response = get_response(URL_TEMPLATE, HEADERS, symbol)
    

    for item in extract_quote_data(response.text):
        print(f"{item['name']}: {item['value']}")

def sp500_companies() -> None:
    response = get_response(URL_TEMPLATE, HEADERS, "")
    for item in extract_sp500_companies(response.text):
        print(f"{item['symbol']}: {item['name']}")


if __name__ == "__main__":
    # apple_finance_datails()
    sp500_companies()
