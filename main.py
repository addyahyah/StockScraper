import thread
import time
import ftse
import dow
import nikkei
import sse

# Create four threads that independently run the scrapers
try:
    thread.start_new_thread(ftse.get_ftse(), ("FTSE Scraper"))
    thread.start_new_thread(dow.get_dow, ("DOW Scraper"))
    thread.start_new_thread(sse.get_sse(), ("SSE Scraper"))
except:
    print "Error: unable to start thread"
