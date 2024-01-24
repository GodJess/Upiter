import requests

def get_alternative_assets():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,gold,silver,&vs_currencies=usd"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    usd_to_eur_response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    eur_data = usd_to_eur_response.json()
    usd_to_eur = eur_data['rates']['EUR']  # Курс доллара к евро

    usd_to_gbp_response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    gbp_data = usd_to_gbp_response.json()
    usd_to_gbp = gbp_data['rates']['GBP']  # Курс доллара к фунту стерлингу


    bitcoin_to_usd = data.get('bitcoin', {}).get('usd', 0)
    ethereum_to_usd = data.get('ethereum', {}).get('usd', 0)
    gold_to_usd = round(data.get('gold', {}).get('usd', 0), 5)
    silver_to_usd = round(data.get('silver', {}).get('usd', 0),5)

    return {
        'usd_to_bitcoin': bitcoin_to_usd,
        'usd_to_ethereum': ethereum_to_usd,
        'usd_to_gold': gold_to_usd,
        'usd_to_silver': silver_to_usd,
        'eur_to_usd': round(1 / usd_to_eur, 5),
        'gbp_to_usd': round(1 / usd_to_gbp, 5)
    }