from nsetools import Nse
import json

nse = Nse()

def get_codes(): 
  #Getting script's code
  stock_list = nse.get_stock_codes()
  stock_codes = [*stock_list]
  stock_codes = stock_codes[1:]
  tickers = []
  for stock in stock_codes:
    tickers.append(stock+'.NS')
  with open( 'stock_code.txt', 'w' ) as fp:
    json.dump(tickers, fp)

if __name__ == '__main__':
  get_codes()

