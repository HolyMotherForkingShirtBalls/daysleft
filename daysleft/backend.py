import datetime
import numpy as np
import time

end = datetime.date(2022,5,27)
springbreak = ['2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-04-15']

def getDate():
    global today
    global d1
    global diff
    today = datetime.date.today()
    d1 = today.strftime("%m/%d/%y")
    diff = np.busday_count(today, end, holidays=springbreak)


getDate()

#today = datetime.date.today()
#d1 = today.strftime("%m/%d/%y")



def dayCount():
    t = time.localtime()
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
            RD = diff -1
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

    time.sleep(1)

    if H == 0 and M == 0:
        getDate()


while True:
    dayCount()