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
    if ctM == 0:
        countHr()
countMin()

def countHr():
    global ctH
    ctH = int(time.strftime("%H", t))
    if ctH == 0:
        getDate()
countHr()

def init():
    getDate()
    getTime()
    countSec()
    countMin()
    countHr()

def countdown():
    pass

def countDayTime():
    H = int(time.strftime("%H", t))
    M = int(time.strftime("%M", t))
    S = int(time.strftime("%S", t))

    if H == 0:
        if M == 0 and S < 5:
            getDate()
            RD = diff
            RH = 15 - H
            RM = 19 - M
            RS = 59 - S
        if M < 20:
            RD = diff
            RH = 15 - H
            RM = 19 - M
            RS = 59 - S
        elif M == 20:
            RD = diff
            RH = 14 - H
            RM = 59
            RS = 59 - S
        elif M > 20:
            RD = diff
            RH = 14 - H
            RM = 79 - M
            RS = 59 - S
    elif H < 15:
        RD = diff
        if M < 20:
            RH = 15 - H
            RM = 19 - M
            RS = 59 - S
        elif M == 20:
            RH = 14 - H
            RM = 59
            RS = 59 - S
        elif M > 20:
            RH = 14 - H
            RM = 79 - M
            RS = 59 - S
    elif H == 15:
        if M < 20:
            RD = diff
            RH = 15 - H
            RM = 19 - M
            RS = 59 - S
        elif M == 20:
            RD = diff - 1
            RH = 23
            RM = 59
            RS = 59 - S
        elif M > 20:
            RH = 14 - H
            RM = 79 - M
            RS = 59 - S
    elif H > 15:
        if M < 20:
            RD = diff - 1
            RH = 24 - H + 15
            RM = 19 - M
            RS = 59 - S
        elif M == 20:
            RD = diff - 1
            RH = 23 - H + 15
            RM = 0
            RS = 59 - S
        elif M > 20:
            RD = diff - 1
            RH = 23 - H + 15
            RM = 79 - M
            RS = 59 - S
        

    
    print ("Days Remaining:",RD, "Time Remaining:",RH,":",RM,":",RS)

 

    if H == 0 and M == 0:
        getDate()

while True:
    countDayTime()
    countSec()
    print (ctH,":",ctM,":",ctS)
    time.sleep(1)