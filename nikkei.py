#!/usr/bin/env python

import urllib2
import pytz
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
import pandas_datareader.data as web
import finsymbols


SSE = "https://en.wikipedia.org/wiki/Nikkei_225"
COMPANY_SECTOR = 1
SSE_NUMBER = 2
START = datetime(1900, 1, 1, 0, 0, 0, 0, pytz.utc)
END = datetime.today().utcnow()


def scrape_sse_list(site):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    table = soup.find('table', {'class': 'wikitable sortable'})
    sector_tickers = dict()
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            sector = col[COMPANY_SECTOR].getText().lower().replace(' ', '_')
            ticker = str(col[SSE_NUMBER].string.strip())
            if sector not in sector_tickers:
                sector_tickers[sector] = list()
            sector_tickers[sector].append(ticker)
    return sector_tickers

def download_ohlc(sector_tickers, start, end):
    sector_ohlc = {}
    for sector, tickers in sector_tickers.iteritems():
        print 'Downloading data from Yahoo for %s sector' % sector
        data = web.DataReader(tickers, 'yahoo', start, end)
        for item in ['Open', 'High', 'Low']:
            data[item] = data[item] * data['Adj Close'] / data['Close']
        data.rename(items={'Open': 'open', 'High': 'high', 'Low': 'low',
                           'Adj Close': 'close', 'Volume': 'volume'},
                    inplace=True)
        data.drop(['Close'], inplace=True)
        sector_ohlc[sector] = data
    print 'Finished downloading data'
    return sector_ohlc


def store_HDF5(sector_ohlc, path):
    with pd.get_store(path) as store:
        for sector, ohlc in sector_ohlc.iteritems():
            store[sector] = ohlc

def get_nikkei():
    sector_tickers = scrape_nikkei_list(DOW)
    sector_ohlc = download_ohlc(sector_tickers, START, END)
    store_HDF5(sector_ohlc, 'nikkei.h5')

if __name__ == '__main__':
    get_nikkei()