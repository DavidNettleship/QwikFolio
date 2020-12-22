import json

class ReadAssets:


    def __init__(self, file):
        self.assets = file


    def fetch_assets(self):
        f = open(self.assets)
        self.assets = json.load(f)

        all_assets = []
        for asset in self.assets["Assets"]:
            all_assets.append(asset)

        return all_assets


    def get_api_name(self, all_assets):
        api_names = []
        for asset in all_assets:
            api_names.append(asset['API Name'])
    
        return api_names