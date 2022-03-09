import datetime
import numpy as np
import time

#initialize variables
end = datetime.date(2022,5,27)
daysOff = ['2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-04-15']

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
    getTime()
    ctM = int(time.strftime("%M", t))
    if ctM == 0 and 0 <= ctS < 2:
        countHr()
countMin()

def countHr():
    global ctH
    getTime()
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
    cRS = 59  - ctS
    if ctS == 0:
        countRemMin()
    if ctM == 20:
        ctRemHr()
countRemSec()

def countRemMin():
    global cRM
    countMin()
    if ctM < 20:
       cRM = 19 - ctM
    elif ctM >= 20:
        cRM = 79 - ctM
    if ctM == 20:
        ctRemHr()
countRemMin()

def ctRemHr():
    global cRH
    countHr()
    if ctM < 20:
        if ctH < 15:
           cRH = 15 - ctH
        elif ctH == 15:
           cRH = 15 - ctH
        elif ctH > 15:
            cRH = 23 - ctH
    elif ctM >= 20:
        if ctH < 15:
           cRH = 14 - ctH
        elif ctH == 15:
           cRH = 23
        elif ctH > 15:
            cRH = 23 - ctH
ctRemHr()

def countRemDay():
    global cRD
    cRD = diff
    if cRH == 0 and cRM == 0:
        cRD = diff - 1
countRemDay()

while True:
    #countDayTime()
    countRemSec()
    #countSec()
    print ("Days Remaining:",cRD,"Time Remaining:",cRH,":",cRM,":",cRS)
    time.sleep(1)