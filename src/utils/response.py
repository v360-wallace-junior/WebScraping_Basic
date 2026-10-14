import requests

def get_response(url: str, headers: dict[str, str], symbol: str) -> requests.Response:
    response = requests.get(
        url.format(symbol=symbol),
        headers=headers,
        timeout=15,
    )
    response.raise_for_status()
    return response