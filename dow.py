#!/usr/bin/env python
import stock


DOW = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"
COMPANY = 0
COMPANY_SYMBOL = 2
STOCK_TYPE = ''

if __name__ == '__main__':
    stock.get_historical_stock_data(DOW, COMPANY, COMPANY_SYMBOL, STOCK_TYPE)
