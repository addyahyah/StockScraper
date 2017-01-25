import thread
import schedule
import time
import os
import shutil

import ftse
import dow
import sse
import snp
from subprocess import call

def job():
    try:
        current_dir = os.getcwd()
        ftse_dir = current_dir + '/' + ftse.get_index()
        dow_dir = current_dir + '/' + dow.get_index()
        sse_dir = current_dir + '/' + sse.get_index()
        snp_dir = current_dir + '/' + snp.get_index()
        if os.path.exists(ftse_dir):
            shutil.rmtree(ftse_dir)
        os.makedirs(ftse_dir)
        if os.path.exists(dow_dir):
            shutil.rmtree(dow_dir)
        os.makedirs(dow_dir)
        if os.path.exists(sse_dir):
            shutil.rmtree(sse_dir)
        os.makedirs(sse_dir)
        if os.path.exists(snp_dir):
            shutil.rmtree(snp_dir)
        os.makedirs(snp_dir)
        ftse.get_ftse()
        dow.get_dow()
        sse.get_sse()
        snp.get_snp()
        call("hadoop fs -put dow/ /tmp/StockData/dow/", shell=True)
        call("hadoop fs -put ftse/ /tmp/StockData/ftse/", shell=True)
        call("hadoop fs -put sse/ /tmp/StockData/sse/", shell=True)
        call("hadoop fs -put snp/ /tmp/StockData/snp/", shell=True)
    except:
        print "Error while getting data from Yahoo finance api"

schedule.every().day.at("4:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
