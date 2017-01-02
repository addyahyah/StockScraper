#!/usr/bin/env python
import stock


NIKKEI = "http://indexes.nikkei.co.jp/en/nkave/index/component"
COMPANY = 1
TYO_NUMBER = 0
STOCK_TYPE = '.F'

if __name__ == '__main__':
    stock.get_historical_stock_data(NIKKEI, COMPANY, TYO_NUMBER, STOCK_TYPE)
