#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import threading
from threading import Thread
from bs4 import BeautifulSoup
import urllib2
import urllib
import html.parser
import pandas as pd
import random
def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
    return random.choice(uastrings)

def logo():
    print ('''
.d88b. 8                           
YPwww. 8d8b. .d88 8d8b.d8b. Yb  dP 
    d8 8P Y8 8  8 8P Y8P Y8  YbdP  
`Y88P' 8   8 `Y88 8   8   8   dP   
                             dP    
    ''')
try:
    wtype = str(sys.argv[1])
    findme = str(sys.argv[2])
except:
    logo()
    print ('shamy.py <dns/ip> <domain.com/1.1.1.1>')
    print ('Ex: shamy.py dns example.com or shamy.py ip 127.0.1.1')
    exit(0)
#try:
if wtype == 'dns':
    stype = 'domain'
elif wtype == 'ip':
    stype = 'ip-history'
elif wtype == 'isp':
    stype = 'isp-history'
else:
    logo()
    exit(0)
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', GET_UA())]
get_it = BeautifulSoup(opener.open('https://dnsdatabase.net/{}/{}'.format(stype,findme)), features="lxml")
tables = pd.read_html(str(get_it))
logo()
print (tables)





#except:
#    print 'oof'
