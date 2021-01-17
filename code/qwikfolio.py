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
    sg = gr.group_equities()
    crypto_assets = ra.get_api_name(cg)
    equity_assets = ra.get_api_name(sg)

    cc = cr.Crypto(crypto_assets, currency)
    cprices = cc.coingecko_live()

    cl = gr.crypto_current_value(cg, cprices)

    s1 = st.Stocks(equity_assets)
    #dat = s1.alpha()
    dat = s1.yfinance_close()

    sl = gr.equity_current_value_yf(sg, dat)

    for result in cl:
        print(result)

    for result in sl:
        print(result)


main()