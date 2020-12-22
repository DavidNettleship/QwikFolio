import json

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
    

    #works for crypto api - may need new function for stocks
    def current_value(self, group, prices):
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
 