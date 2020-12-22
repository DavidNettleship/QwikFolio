import requests
import json


class Crypto:

    def __init__(self, assets, currency):
        self.assets = assets
        self.currency = currency


    def ls_assets(self):
       print(self.assets)
    

    #full list of coins
    def coingecko_coins(self):
        response = requests.get('https://api.coingecko.com/api/v3/coins/list')
        data = response.json()

        return data
    

    #live price
    def coingecko_live(self):
        data = []
        for asset in self.assets:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+ asset + '&vs_currencies=' + self.currency)
            data.append(response.json())

        return data