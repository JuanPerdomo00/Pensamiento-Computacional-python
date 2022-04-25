#!/usr/bin/python3
from datetime import datetime
import time
import sys

def relog_while_aninado():
    now = datetime.now()
    hrs = now.hour
    min = now.minute
    sec = now.second

    while hrs<24:
        while min<60:
            while sec<60:
                current = str(hrs).zfill(2) + " : " + str(min).zfill(2) + " : " + str(sec).zfill(2) + "\r"
                sys.stdout.write(current)
                sec += 1
                time.sleep(1)
            min += 1
            sec = 0
        hrs += 1
        min = 0


def while_sencillo():
    while True:
        now = datetime.now()
        print(f'{now.hour}:{now.minute}:{now.second}')
        time.sleep(1)



while_sencillo()
