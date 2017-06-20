#!/usr/bin/env python3
"""
MIT License
Copyright (c) 2017
Nicholas Purdy
nicholaswpurdy@gmail.com
github.com/NicholasPurdy/QOTDserverd
"""

import socket
import time
from random import randint

# modify these to your liking
quotesPerDay = 1000000
quotesPerIP = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 17))
s.listen(5)
quotes = open("/etc/QOTDserverd/quotes.txt","r")
quotes = quotes.read().splitlines()
day = time.strftime("%d")
quotesSent = 0
requestByIP = dict()
while True:
    try:
        conn, addr = s.accept()
        log = open("/etc/QOTDserverd/connection_log.txt","a")
        log.write("Connection made with: " + str(addr[0]) + "\n")
        log.close()
        if day != time.strftime("%d"):
            quotesSent = 0
            day = time.strftime("%d")
            requestByIP.clear()

        if requestByIP.setdefault(addr[0], 0) < quotesPerIP and quotesSent < quotesPerDay:
            q = quotes[randint(0, len(quotes)-1)] + "\n"
            conn.send(q.encode('utf-8'))
            quotesSent += 1
            requestByIP[addr[0]] += 1
        conn.close()
    except socket.error:
        pass
