
#!/usr/bin/env python
import stock


FTSE = "https://en.wikipedia.org/wiki/FTSE_100_Index"
COMPANY = 0
COMPANY_SYMBOL = 1
STOCK_TYPE = '.L'

if __name__ == '__main__':
    stock.get_historical_stock_data(FTSE, COMPANY, COMPANY_SYMBOL, STOCK_TYPE)
