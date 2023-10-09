import requests

def get_ohlc(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/ohlc"
    headers = {"accept": "application/json"}

    params = {
        'vs_currency': 'usd',
        'days': 'max'
    }

    response = requests.get(url, params=params, headers = headers)

    if response.status_code == 200:
        data = response.json()
        # response is list of lists with format: [timestamp, o, h, l, c]
        if not data:
            print("prices is empty")
    else:
        print(f'Error getting price data, code: {response.status_code}')
        return None
    return data

if __name__ == "__main__":
    get_ohlc("bitcoin")