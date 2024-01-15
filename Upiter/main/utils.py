import requests

def get_exchange_rates(api_key):
    url = f'http://data.fixer.io/api/latest?access_key={api_key}&symbols=USD,EUR,GBP'
    response = requests.get(url)
    data = response.json()
    return {
        'eur_to_usd': round(data['rates']['USD'] / data['rates']['EUR'], 4),
        'gbp_to_usd': round(data['rates']['USD'] / data['rates']['GBP'], 4)
    }

def get_alternative_assets():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,gold,silver&vs_currencies=usd"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    bitcoin_to_usd = data.get('bitcoin', {}).get('usd', 0)
    ethereum_to_usd = data.get('ethereum', {}).get('usd', 0)
    gold_to_usd = round(data.get('gold', {}).get('usd', 0), 5)
    silver_to_usd = round(data.get('silver', {}).get('usd', 0),5)

    return {
        'usd_to_bitcoin': bitcoin_to_usd,
        'usd_to_ethereum': ethereum_to_usd,
        'usd_to_gold': gold_to_usd,
        'usd_to_silver': silver_to_usd
    }