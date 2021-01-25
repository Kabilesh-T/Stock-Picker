# from nsetools import Nse
from yahoo_fin.stock_info import get_data
from pprint import pprint
import time
import json

def get_quote(stock_codes):
  start_time = time.time()
  historic_data = {}
  for stock in (stock_codes):
    try:
      data = get_data(stock, start_date = '01/01/2017' , end_date = '05/01/2017', interval = '1mo')
      historic_data[stock] = data.to_dict('records')
      print(historic_data)
      # historic_data[stock] = data.to_json(orient = "records")
      # if quote['totalTradedVolume'] >= 2000000 and quote['lastPrice'] <= quote[low52]:
      #   pprint(stock+": "+str(quote['lastPrice']))
    except Exception:
      pass
  # print(historic_data['infy'])
  end_time = time.time()
  with open( 'data/monthly_data_dummy.txt', 'w' ) as fp:
    json.dump(historic_data, fp)
  print("Time taken : ", end_time-start_time)


if __name__ == '__main__':
  # with open('stock_code.txt', 'r') as fp:
  #   stock_codes = json.load(fp)
  get_quote(['infy', 'voltas.ns'])
