#!/usr/bin/env python

import urllib2
import pytz
import pandas as pd
import os
import json

from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import pandas_datareader.data as web

START = datetime(1900, 1, 1, 0, 0, 0, 0, pytz.utc)
END = datetime.today().utcnow()
special_cases = dict()
special_cases['RR.'] = 'RR.L'

def scrape_list(site, company_name, company_symbol, stock_type, index):
    companies = dict()
    try:
        with open(os.getcwd() + '/' + str(index) + '.json', 'r') as f:
            companies = json.load(f)
    # if the file is empty the ValueError will be thrown
    except:
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
                t = str(col[company_symbol].string.strip())
                try:
                    t = special_cases[t]
                except:
                    t = t.replace('.', '') + stock_type
                ticker = t 
                companies[company] = list()
                companies[company].append(ticker)
    return companies

def scrape_nikkei(site, company_name, company_symbol, stock_type):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    table = soup.find('div', {'class': 'col-xs-12 col-sm-8'})
    companies = dict()
    for row in table.findAll('div', {'class': 'row component-list'}):
        if len(row) > 0:
            company = str(row.a.getText())
            ticker = str(row.div.string.strip()).replace('.', '') + stock_type
            companies[company] = list()
            companies[company].append(ticker)
    return companies

def download_ohlc(companies, start, end, index):
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
        df = data.to_frame()
        df.to_csv(str(index) + '/' + company.replace(' ', '_') + '.csv')
    print 'Finished downloading data'
    return company_ohlc

def get_historical_stock_data(site, company, company_symbol, stock_type, index):
    companies = ''
    if stock_type == '.F':
        companies = scrape_nikkei(site, company, company_symbol, stock_type)
    else:
        companies = scrape_list(site, company, company_symbol, stock_type, index)
    company_ohlc = download_ohlc(companies, START, END, index)
    # store_HDF5(company_ohlc, 'dow.h5')
