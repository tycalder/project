import datetime 
from time import sleep
import os 
#from Modules import *
from picamera import PiCamera
from gps import *
import time, inspect


def return_GPS_data(): 

    gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

    try:
        while True:
            report = gpsd.next()
            if report['class'] == 'TPV':
                lat = str(getattr(report,'lat',0.0)),
                lon = str(getattr(report,'lon',0.0)),
                time = str(getattr(report,'time','')),
                speed = str(getattr(report,'speed','nan')),
                # time.sleep(1)

    return (lat+ "\t" + lon + "\t" + time + "\t" + speed)