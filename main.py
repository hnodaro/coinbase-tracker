from pycoingecko import CoinGeckoAPI

if __name__ == "__main__":
    cg = CoinGeckoAPI()
    print(cg.get_price(ids='bitcoin', vs_currencies='usd'))
