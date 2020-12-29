import requests
import json


class Stocks:

    def __init__(self, assets):
        self.assets = assets


    def ls_assets(self):
       print(self.assets)
       
       
    def alpha(self):
        file = open('../data/av_key.txt',"r") #av_key.txt contains api key
        key = file.readline().strip("\n")
        stonks = "MSFT:SWKS:O:FB:SNOW"

        for stock in stonks.split(":"):
                response_av = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol='+stock+'&apikey='+key)
                data = (response_av.json())

        return data