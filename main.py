import thread
import time
import os
import shutil

import ftse
import dow
import sse
import snp

# Create four threads that independently run the scrapers
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
except:
    print "Error while getting data from Yahoo finance api"
