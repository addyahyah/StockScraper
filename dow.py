#!/usr/bin/env python
import stock


DOW = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"
COMPANY = 0
COMPANY_SYMBOL = 2
STOCK_TYPE = ''
INDEX = 'dow'

def get_dow():
    stock.get_historical_stock_data(DOW, COMPANY, COMPANY_SYMBOL, STOCK_TYPE, INDEX)

def get_index():
    return INDEX