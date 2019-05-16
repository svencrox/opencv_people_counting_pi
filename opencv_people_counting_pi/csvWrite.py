#!/usr/bin/env python
import csv
import random
import time
from datetime import datetime

def saveToFile(total):
    ttl = total
    print("ttl: " + str(ttl))

    # current time and print it
    dt = datetime.fromtimestamp(time.time())
    print("dt: " + str(dt))

    row = [dt, ttl]

    with open('example.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(row)

    writeFile.close()