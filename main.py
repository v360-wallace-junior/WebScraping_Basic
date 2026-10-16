from src.static.yaholl_finance import extract_quote_data
from src.static.sp500_companies_extract import extract_sp500_companies
from src.utils import get_response


HEADERS = {"User-Agent": "Mozilla/5.0"}
URL_TEMPLATE = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
URL_FINANCE_TEMPLATE = "https://finance.yahoo.com/quote/{symbol}/"


def get_finance_datails(company: str) -> None:
    try:
        response = get_response(URL_FINANCE_TEMPLATE, HEADERS, company)
        quote_data = extract_quote_data(response.text)
        for item in quote_data:
            print(f"{item['name']}: {item['value']}")

    except Exception as e:
        print(f"Error occurred while extracting finance details for {company}: {e}")

  

def sp500_companies() -> list[dict[str, str]]:
    try:
        response = get_response(URL_TEMPLATE, HEADERS, "")
        companies = extract_sp500_companies(response.text)
        return companies

    except Exception as e:
        print(f"Error occurred while extracting S&P 500 companies: {e}")
        return []

if __name__ == "__main__":
    companies = sp500_companies()
    get_finance_datails("AAPL")
    for company in companies:
        get_finance_datails(company["symbol"])
        print("--------------------------------------------------")
    