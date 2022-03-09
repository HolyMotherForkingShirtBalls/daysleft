import datetime
import numpy as np
import time

#initialize variables
end = datetime.date(2022,5,27)
daysOff = ['2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-04-15']
#t = time.localtime()
#ctS = int(time.strftime("%S", t))
#ctM = int(time.strftime("%M", t))
#ctH = int(time.strftime("%H", t))
#print ("int",ctH,":",ctM,":",ctS)

#define functions
def getDate():
    global today
    global diff
    today = datetime.date.today()
    diff = np.busday_count(today, end, holidays=daysOff)
getDate()

def getTime():
    global t
    t = time.localtime()
getTime()

def countSec():
    getTime()
    global ctS
    ctS = int(time.strftime("%S", t))
    if ctS == 0:
        countMin()
countSec()

def countMin():
    global ctM
    ctM = int(time.strftime("%M", t))
    if ctM == 0 and 0 <= ctS < 2:
        countHr()
countMin()

def countHr():
    global ctH
    ctH = int(time.strftime("%H", t))
    if ctH == 0 and ctS < 2:
        getDate()
countHr()

def init():
    getDate()
    getTime()
    countSec()
    countMin()
    countHr()

def countRemSec():
    global cRS
    countSec()
    cRS = 59 - ctS
    if cRS == 0:
        countRemMin()
countRemSec()

def countRemMin():
    global cRM
    countMin()
    if ctM <= 20:
       cRM = 19 - ctM
    elif ctM > 20:
        cRM = 79 - ctM
countRemMin()

def countRemHr():
    global cRH
    countHr()
    if ctH < 15:
        cRH = 15 - ctH
    elif ctH == 15 and ctM < 20:
        cRH = 15 - ctH
    elif ctH == 15 and ctM >= 20:
        cRH = 24 - ctH + 15
countRemHr()

def countRemDay():
    global cRD
    cRD = diff
    if cRH == 0 and cRM == 0:
        cRD = diff - 1
countRemDay()
        

def countDayTime():
   init()
   if ctH == 0:
        if ctM == 0 and ctS < 5:
            #getDate()
            RD = diff
            RH = 15 - ctH
            RM = 19 - ctM
            RS = 59 - ctS
        if ctM < 20:
            RD = diff
            RH = 15 - ctH
            RM = 19 - ctM
            RS = 59 - ctS
        elif ctM == 20:
            RD = diff
            RH = 14 - ctH
            RM = 59
            RS = 59 - ctS
        elif ctM > 20:
            RD = diff
            RH = 14 - ctH
            RM = 79 - ctM
            RS = 59 - ctS
   elif ctH < 15:
        RD = diff
        if ctM < 20:
            RH = 15 - ctH
            RM = 19 - ctM
            RS = 59 - ctS
        elif ctM == 20:
            RH = 14 - ctH
            RM = 59
            RS = 59 - ctS
        elif ctM > 20:
            RH = 14 - ctH
            RM = 79 - ctM
            RS = 59 - ctS
   elif ctH == 15:
        if ctM < 20:
            RD = diff
            RH = 15 - ctH
            RM = 19 - ctM
            RS = 59 - ctS
        elif ctM == 20:
            RD = diff - 1
            RH = 23
            RM = 59
            RS = 59 - ctS
        elif ctM > 20:
            RH = 14 - ctH
            RM = 79 - ctM
            RS = 59 - ctS
   elif ctH > 15:
        if ctM < 20:
            RD = diff - 1
            RH = 24 - ctH + 15
            RM = 19 - ctM
            RS = 59 - ctS
        elif ctM == 20:
            RD = diff - 1
            RH = 23 - ctH + 15
            RM = 0
            RS = 59 - ctS
        elif ctM > 20:
            RD = diff - 1
            RH = 23 - ctH + 15
            RM = 79 - ctM
            RS = 59 - ctS
        

    
   print ("Days Remaining:",RD, "Time Remaining:",RH,":",RM,":",RS)

while True:
    #countDayTime()
    countRemSec()
    #countSec()
    print ("Days Remaining:",cRD,"Time Remaining:",cRH,":",cRM,":",cRS)
    time.sleep(1)