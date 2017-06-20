# QOTDserverd
A simple QOTD server that caps the number of quotes per day (total and per IP) to prevent pingpong DOS attacks

Modify the quotesPerDay and quotesPerIP variables to change the limits.

## Installation guide
1. Create *QOTDserverd* directory in */etc*
2. Create **connection_log.txt** and **quotes.txt** in */etc/QOTDserverd*
3. Fill **quotes.txt** with whatever quotes you want. Quotes are seperated by a newline
4. ```chmod +x``` on **QOTDserverd.py**
5. Move **QOTDserverd.py** to */usr/bin*
6. Move **QOTDserver.service** to */etc/systemd/system/*
7. ```sudo systemctl enable QOTDserverd.service```
8. ```sudo systemctl daemon-reload```
9. ```sudo systemctl start QOTDserverd.service```
10. ```sudo systemctl status QOTDserverd.service```

## Try it out
```$ nc nicholaspurdy.net 17```
