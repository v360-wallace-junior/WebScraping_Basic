import requests
from bs4 import BeautifulSoup

def extract_quote_data(html: str) -> list[dict[str, str | None]]:
    soup = BeautifulSoup(html, "html.parser")
    quote_data = []

    for item in soup.find_all("li", class_="yf-11op525"):
        label = item.find("span", class_="labelText")
        if label is None:
            continue

        value_element = item.find("span", class_="value")
        if value_element is not None:
            value = value_element.get_text(strip=True)
        else:
            value_element = next(
                (
                    element
                    for element in item.find_all("fin-streamer")
                    if (element.get("data-field") or "").startswith("regular")
                ),
                None,
            )
            value = (
                value_element.get("data-value") or value_element.get_text(strip=True)
                if value_element is not None
                else None
            )

        quote_data.append(
            {
                "name": label.get_text(strip=True),
                "value": value,
            }
        )

    return quote_data
