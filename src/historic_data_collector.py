from yahoo_fin.stock_info import get_data
import time
import json

def get_quote(interval):

  stock_codes = []
  start_time = time.time()
  #Gets Stock codes from JSON
  with open('data/stock_code.txt', 'r') as fp:
    stock_codes = json.load(fp)
    
  #Gets Monthly data for codes
  historic_data = {}
  failed_codes = []
  for stock in (stock_codes):
    try:
      data = get_data(stock, start_date = '01/01/2017' , end_date = '05/01/2017', interval = interval)
      historic_data[stock] = data.to_dict('records')
      print("Getting... ",stock)
    except Exception:
      failed_codes.append(stock)
  # Writing data to file
  with open( 'data/monthly_data.txt', 'w' ) as fp:
        json.dump(historic_data, fp)
  end_time = time.time()
  print("Time taken : ", end_time-start_time)
  print("Failed stocks... ", failed_codes)
