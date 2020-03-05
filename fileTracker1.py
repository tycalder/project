import datetime 
from time import sleep
import os 
#from Modules import *
from picamera import PiCamera
from gps import *
import time, inspect

#camera = PiCamera()

#def newSnippet(textFile, videoFile, Position):
#updateLatest()
#updateEarliest()
#updateCurrent()
#PiCam Function()

#Creates a txt file with filename and format: Date    Time    GPS Data    Speed
# def create_file(filename:str):
#     fileName = filename + ".txt"
#     f = open(fileName, "w")
#     f.write(fileName + "\n")
#     f.write("Date        Time        GPS Co-ords    Speed [km/h]\n")
#     f.close

#Function to get GPS Data
   

#def get_GPS_data():
""" f = open(time.strftime("%Y%m%d-%H%M%S")+'_GSPData.csv','w')
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
print 'latitude\tlongitude\ttime utc\t\t\taltitude\tepv\tept\tspeed\tclimb'
f.write ("latitutde,longitude,time,altitude,epv,speed,climb")

try:
    while True:
        report = gpsd.next()
        if report['class'] == 'TPV':
            lat = str(getattr(report,'lat',0.0)),
            lon = str(getattr(report,'lon',0.0)),
            time = str(getattr(report,'time','')),
            alt = str(getattr(report,'alt','nan')),
            epv = str(getattr(report,'epv','nan')),
            ept = str(getattr(report,'ept','nan')),
            speed = str(getattr(report,'speed','nan')),
            climb = str(getattr(report,'climb','nan')),
            
            print lat, "\t",
            print lon, "\t",
            print time, "\t\t",
            print alt, "\t",
            print ept, "\t",
            print speed, "\t",
            print climb, "\t",
            
            f.write(lat + ',' + lon ',' + time ',' + alt + ',' + ept + ',' + speed + ',' + climb + '\n')

            time.sleep(1)

except (KeyboardInterrupt, SystemExit):
    print "Done. \nExiting" 
    f.close()    
 """

#def return_GPS_data(): 
f = open(time.strftime("%Y%m%d-%H%M%S")+'_GPSData.txt','w')
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
print 'latitude\tlongitude\ttime\tspeed\tclimb'
f.write ('latitutde'+'\t'+'longitude'+'\t'+'time'+'\t'+'speed')

try:
    while True:
        report = gpsd.next()
        if report['class'] == 'TPV':
            lat = str(getattr(report,'lat',0.0)),
            lon = str(getattr(report,'lon',0.0)),
            time = str(getattr(report,'time','')),
            speed = str(getattr(report,'speed','nan')),
         
            print lat, "\t",
            print lon, "\t",
            print time, "\t\t",            
            print speed, "\t",
  
            f.write(lat + '\t' + lon +'\t'+ time +'\t'+ speed + '\n')

            time.sleep(1)

except (KeyboardInterrupt, SystemExit): #also need to add the bit if crash has occured
    print "Done. \nExiting" 
    f.close()

#return lat, lon, time, speed


#Function to get speed, not needed anymore taken care of in previous funciton


# def add_to_file(fileName: str):
#     f = open(fileName, "a")
#     for i in range(2):
#         dateTime = datetime.datetime.now()
#         date = str(dateTime.year) +":" + str(dateTime.month) + ":" + str(dateTime.day)
#         tm = str(dateTime.hour) + ":" + str(dateTime.minute) + ":" + str(dateTime.second)
#         info = date + "    " + tm
#         #gpsData = callfunction
#         f.write(info + "     GPS Data\n")
#         time.sleep(1)
#     f.close

# #Initiates an array with 10 strings
# def initiate(arrayName):
#     arrayName = []
#     for i in range(11):
#         trackingArray.append(str(i))
       
#def recycle(filename):

#initiate(test)
#filename Function