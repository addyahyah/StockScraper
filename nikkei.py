#!/usr/bin/env python
import stock


NIKKEI = "http://indexes.nikkei.co.jp/en/nkave/index/component"
COMPANY = 1
TYO_NUMBER = 0
STOCK_TYPE = '.F'
INDEX = 'nikkei'

def get_nikkei():
    stock.get_historical_stock_data(NIKKEI, COMPANY, TYO_NUMBER, STOCK_TYPE, INDEX)

def get_index():
    return INDEX
    