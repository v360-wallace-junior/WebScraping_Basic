import re
from bs4 import BeautifulSoup


def extract_sp500_companies(html_content: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html_content, "html.parser")

    quote_data = []

    table = soup.find("table", attrs={'class': re.compile(r'^wikitable sortable')})
    # print(table)

    rows = table.find_all("tr", attrs={'id': re.compile(r'^mw')})
    # print(rows)

    for row in rows[1:]:
        # print([cell.get_text(strip=True) for cell in row.find_all("td")])
        cells = row.find_all("td")
        if len(cells) >= 8:
            quote_data.append(
                {
                    "symbol": cells[0].get_text(strip=True),
                    "name": cells[1].get_text(strip=True),
                    "sector": cells[2].get_text(strip=True),
                    "sub_sector": cells[3].get_text(strip=True),
                    "headquarters_location": cells[4].get_text(strip=True),
                    "date_first_added": cells[5].get_text(strip=True),
                    "cik": cells[6].get_text(strip=True),
                }
            )

    return quote_data
