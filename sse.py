#!/usr/bin/env python
import stock


SSE = "https://en.wikipedia.org/wiki/SSE_50_and_SSE_180_Indexes"
COMPANY = 0
SSE_NUMBER = 2
STOCK_TYPE = '.SS'
INDEX = 'sse'

def get_sse():
    stock.get_historical_stock_data(SSE, COMPANY, SSE_NUMBER, STOCK_TYPE, INDEX)

def get_index():
    return INDEX
