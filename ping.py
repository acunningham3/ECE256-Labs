#!/bin/python

import os
import time
import socket
import urllib2

hostname = "eng-svr-1"
port = 8877

def internet_on():
    try:
        urllib2.urlopen('http://eng-svr-1:8877', timeout=1)
	print hostname, 'is up!'
	time.sleep(2)
        return True
    except urllib2.URLError as err: 
	print hostname, 'is down!'
	time.sleep(2)
        return False

while(True):

	internet_on()
