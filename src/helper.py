from code_getter import get_codes
from historic_data_collector import get_quote

if __name__ == '__main__':
  option = True
  while option:
    print("""
    1. Get Stock codes
    2. Get Monthly data
    3. Get Weekly data
    4. Exit
    """)
    option = input("Enter Option: ")
    if option == '1':
      print("Getting Stock Codes...")
      get_codes()
    elif option == '2':
      print("Getting Monthly data...")
      get_quote('1mo')
    elif option == '3':
      print("Getting Weekly data...")
    elif option == '4':
      print("Terminating...")
      option = None
    else:
      print("Invalid entry")
    
