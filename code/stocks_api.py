import requests
import json
import yfinance as yf


class Stocks:

    def __init__(self, assets):
        self.assets = assets


    def ls_assets(self):
       print(self.assets)
       
    
    #intraday stock price from alphavantage api
    def alpha(self):
        file = open('../data/av_key.txt',"r")
        key = file.readline().strip("\n")
        data = []

        for stock in self.assets:
                response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+stock+ '&interval=5min' +'&apikey='+key)
                data.append(response.json())

        return data
    

    #latest close price from yahoofinance (yfinance)
    def yfinance_close(self):
        data = []
        temp_data = {}

        for stock in self.assets:
            temp_data = {stock,yf.download(stock, period="1d", interval="1m")["Close"][-1]}
            data.append(temp_data)
        
        return data
