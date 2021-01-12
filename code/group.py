import json
import requests

class AssetList:


    def __init__(self, assets):
        self.assets = assets
    

    def group_crypto(self):
        cgroup = []

        for asset in self.assets:
            if asset['Class'] == 'crypto':
                cgroup.append(asset)
        
        return cgroup
 

    def group_equities(self):
        egroup = []

        for asset in self.assets:
            if asset['Class'] == 'equity':
                egroup.append(asset)
        
        return egroup
    

    def usd_to_gbp(self):
        file = open('../data/av_key.txt',"r")
        key = file.readline().strip("\n")

        response = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=GBP' +'&apikey='+key)
        rate = response.json()
        forex = (dict(rate).get(list(rate)[0])).get('5. Exchange Rate')

        return forex


    def crypto_current_value(self, group, prices):
        current_value = []
        total = 0

        for asset in group:
            api_name = asset['API Name']

            for price in prices:
                if list(price)[0] == api_name:
                    pr = float((dict(price).get(list(price)[0])).get('gbp'))

            value = asset['Quantity']
            value = str(round(value * pr, 2))

            total = round(total + float(value),2)
            current_value.append("Asset: " + asset['Ticker'] + " | Quantity: " + str(asset['Quantity']) + " | Market Value: " + str(pr) +" | Portfolio Value: " + value)

        current_value.append("Total: " + str(total))
        return current_value
 

    def equity_current_value(self, group, prices):
        current_value = []
        total = 0
        forex = self.usd_to_gbp()

        for asset in group:
            ticker = (asset.get(list(asset)[2]))
            api_name = asset['API Name']

            for price in prices:
                if price.get('Meta Data').get('2. Symbol') == api_name:

                    tick = price.get('Time Series (5min)')
                    last_updated = list(tick)[0]
                    price_data = tick.get(last_updated)

                    pr = price_data.get(list(price_data)[3])

                    value = asset['Quantity']

                    value = str(round((value * float(pr)* float(forex)), 2))
                    total = round(total + float(value),2)

                    current_value.append("Asset: " + asset['Ticker'] + " | Quantity: " + str(asset['Quantity']) + 
                    " | Market Value: " + str(round(float(pr) * float(forex),2)) + " | Portfolio Value: " + value)
        
        current_value.append("Total: " + str(total))
        return current_value


    def chart_group(self, assets):

        asa = []
        vals = []
        tot = []

        for a_class in assets:
            tot.append(a_class[-1].split(': ')[1])
            del a_class[-1]

            for asset in a_class:
                name = (asset.split('|')[0].split(': ')[1])
                val = (asset.split('|')[3].split(': ')[1])

                asa.append(name)
                vals.append(val)

        return asa, vals, tot
