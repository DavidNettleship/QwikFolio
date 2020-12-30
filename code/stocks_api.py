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
        data = []

        for stock in self.assets:
                response = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol='+stock+'&apikey='+key)
                data.append(response.json())

        return data