import requests
import format_price as fp
from datetime import datetime


def price_of_coin_date(coin, date):
    # date format "dd-mm-yyyy"
    # returns coin price on specified date in usd
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "market_data" in data and "current_price" in data["market_data"]:
            coin_price = data["market_data"]["current_price"]["usd"]
            return coin_price
        else:
            print(f"error fetching {coin} price on {date}")
    else:
        print(f"Error code {response.status_code}")
    return None


def max_price_in_range(coin, start_date, days):
    # start date format "dd-mm-yyyy"
    # returns the highest price in specified range    
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range"
    headers = {"accept": "application/json"}

    # api requires date in unix timestamp format
    start_timestamp = int(datetime.strptime(start_date, '%d-%m-%Y').timestamp())
    end_timestamp = start_timestamp + (days * 24 * 60 * 60)

    params = {
        'vs_currency': 'usd',  
        'from': start_timestamp,
        'to': end_timestamp,
        'precision': 'full',   
    }
    response = requests.get(url, params=params, headers = headers)

    if response.status_code == 200:
        data = response.json()        
        prices = data.get("prices", [])
        # response is dictionary, key "prices" contains list of lists as [timestamp, price]
        if prices:
            max_price = max(prices, key=lambda x: x[1])
            return max_price[1]
    else:
        print(f'Error in getting price range data, code: {response.status_code}')
    return None


def current_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    headers = {"accept": "application/json"}
    params = {
        "ids": coin,
        "vs_currencies" : "usd",
        "precision" : "full"
    }

    response = requests.get(url, params = params, headers = headers)

    if response.status_code == 200:
        data = response.json()
        #price = data.get(coin, {}).get("usd")
        price = data.get(f"{coin}")
        if price:
            return price.get("usd")
    else:
        print(f"error getting current price data, code {response.status_code}")
        return None


def peak_crypto_era_price(coin):    
    peak = max_price_in_range(coin, "01-03-2021", 35)
    return peak
    

def all_time_high(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/ohlc?vs_currency=usd&days=max"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # data is list of lists as [timestamp, o, h, l c]
        if data:
            highs = []
            for entry in data:
                highs.append([entry[2], entry[0]])
            if highs:
                highest_price_index = highs.index(max(highs))
                highest_price = highs[highest_price_index]
                date = datetime.utcfromtimestamp(highest_price[1] / 1000).strftime('%d-%m-%Y')
                return [highest_price[0], date]
    else:
        print(f"error getting highest price data, code {response.status_code}")
        return None

def print_stats(coin):
    current = current_price(coin)
    data = {
        "current": current,
        "peak": peak_crypto_era_price(coin) if current is not None else None,
        "peak_diff": None,
        "ath": None,
        "ath_diff": None,
        "ath_date": None,
        "all_stats": None
    }
    if data["current"] is None:
        data["all_stats"] = f"unable to find any data for {coin}."    
        return data

    if data["peak"]:    
        diff = abs(data["peak"]-data["current"])
        data["peak_diff"] = (diff/data["peak"])*100

    ath_tuple = all_time_high(coin)
    if ath_tuple and ath_tuple[0] > 0:        
        data["ath"] = ath_tuple[0]
        data["ath_date"] = ath_tuple[1]
        data["ath_diff"] = ((data["ath"] - data["current"])/data["ath"])*100

    if data["peak"] is None:
       data["all_stats"] = (f"{coin} was not around during the peak crypto-rush-era of 2021."
            f" {coin} is currently at ${fp.format_price(data['current'])},"
            f" which is {data['ath_diff']:.01f}% below its all time high of {data['ath']} from {data['ath_date']}")
    else:
        data["all_stats"] = (f"current price of {coin} is ${fp.format_price(data['current'])}," 
           f" which is ${fp.format_price(diff)} {'below' if data['peak']>data['current'] else 'above'}"
           f" its peak 2021 crypto-rush-era price of ${fp.format_price(data['peak'])}; "          
           f"a{' decline' if data['peak']>data['current'] else ' gain'} of "
           f"{data['peak_diff']:.01f}%."
           f" {coin} is also {data['ath_diff']:.01f}% below its all time high of {fp.format_price(data['ath'])} from {data['ath_date']}")
    
    return data