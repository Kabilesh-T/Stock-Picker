# from nsetools import Nse
from yahoo_fin.stock_info import get_data
from pprint import pprint
import time
import json

def get_quote(stock_codes):
  start_time = time.time()
  # pprint(nse.get_quote('infy'))
  for stock in (stock_codes):
    try:
      historic_data = get_data(stock, start_date = '01/01/2017' , end_date = '05/01/2017', interval = '1mo')
      # if quote['totalTradedVolume'] >= 2000000 and quote['lastPrice'] <= quote[low52]:
      #   pprint(stock+": "+str(quote['lastPrice']))
      print(stock)
    except Exception:
      pass
  end_time = time.time()
  print("Time taken : ", end_time-start_time)


if __name__ == '__main__':
  with open('stock_code.txt', 'r') as fp:
    stock_codes = json.load(fp)
  get_quote(stock_codes)
