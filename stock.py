#!/usr/bin/env python

import urllib2
import pytz
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
import pandas_datareader.data as web

START = datetime(1900, 1, 1, 0, 0, 0, 0, pytz.utc)
END = datetime.today().utcnow()

def scrape_list(site, company_name, company_symbol, stock_type):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    table = soup.find('table', {'class': 'wikitable sortable'})
    companies = dict()
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            company = col[company_name].getText()
            print company
            ticker = str(col[company_symbol].string.strip()) + stock_type
            print ticker
            companies[company] = list()
            companies[company].append(ticker)
    return companies

def download_ohlc(companies, start, end):
    company_ohlc = {}
    for company, ticker in companies.iteritems():
        print 'Downloading data from Yahoo for %s' % company
        data = web.DataReader(ticker, 'yahoo', start, end)
        for item in ['Open', 'High', 'Low']:
            data[item] = data[item] * data['Adj Close'] / data['Close']
        data.rename(items={'Open': 'open', 'High': 'high', 'Low': 'low',
                           'Adj Close': 'close', 'Volume': 'volume'},
                    inplace=True)
        data.drop(['Close'], inplace=True)
        company_ohlc[company] = data
    print 'Finished downloading data'
    return company_ohlc


def store_HDF5(company_ohlc, path):
    with pd.get_store(path) as store:
        for company, ohlc in company_ohlc.iteritems():
            store[company] = ohlc

def get_historical_stock_data(site, company, company_symbol, stock_type):
    companies = scrape_list(site, company, company_symbol, stock_type)
    company_ohlc = download_ohlc(companies, START, END)
    # store_HDF5(company_ohlc, 'dow.h5')
