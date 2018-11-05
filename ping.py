#!/bin/python

import os
import time
import socket
import urllib2
import sys

hostname = sys.argv[1]
port = sys.argv[2]

def internet_on():
    try:
        urllib2.urlopen(hostname + ':' + port, timeout=1)
	print hostname + ':' + port, 'is up!'
	time.sleep(2)
        return True
    except urllib2.URLError as err: 
	print hostname + ':' + port, 'is down!'
	time.sleep(2)
        return False

while(True):

	internet_on()
