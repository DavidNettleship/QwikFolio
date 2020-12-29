import crypto_api as cr
import stocks_api as st
import read as rd
import group as gp

#vars
currency = 'gbp'


def main():

    ra = rd.ReadAssets('../data/assets.json')
    alist = ra.fetch_assets()
    gr = gp.AssetList(alist)
    cg = gr.group_crypto()
    api_assets = ra.get_api_name(cg)

    cc = cr.Crypto(api_assets, currency)
    cprices = cc.coingecko_live()

    cl = gr.current_value(cg, cprices)
    print(cl)
    print(cl[8:9]) #Total

    s1 = st.Stocks(currency)
    print(s1.alpha())


main()