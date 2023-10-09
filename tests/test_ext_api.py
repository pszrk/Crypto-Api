import requests

def test_endpoint_return_structure():
    url = f"https://api.coingecko.com/api/v3/coins/{'bitcoin'}/ohlc"
    headers = {"accept": "application/json"}

    params = {
        'vs_currency': 'usd',
        'days': 'max'
    }
    response = requests.get(url, params = params, headers = headers)
    
    assert response.status_code == 200
    
    data = response.json()

    assert isinstance(data, list)

    for internal_list in data:
        assert isinstance(internal_list, list)
        assert len(internal_list) == 5