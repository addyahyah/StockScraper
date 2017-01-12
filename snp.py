#!/usr/bin/env python
import stock


FTSE = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
COMPANY = 1
COMPANY_SYMBOL = 0
STOCK_TYPE = ''
INDEX = 'snp'

def get_snp():
    stock.get_historical_stock_data(FTSE, COMPANY, COMPANY_SYMBOL, STOCK_TYPE, INDEX)

def get_index():
    return INDEX