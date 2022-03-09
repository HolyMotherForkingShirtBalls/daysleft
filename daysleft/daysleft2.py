import datetime
import numpy as np
import time

today = datetime.date.today()
d1 = today.strftime("%m/%d/%y")
end = datetime.date(2022,5,18)
springbreak = ['2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-04-15', '2022-04-13', '2022-04-14', '2022-04-18']
diff = np.busday_count(today, end, holidays=springbreak)


while True:
    t = time.localtime()
    H = int(time.strftime("%H", t))
    M = int(time.strftime("%M", t))
    S = int(time.strftime("%S", t))
    if H < 15:    
        RH = 14 - H
    elif H == 15:
            RH = 23
    else:
        RH = 39 - H
    RM = 59 - M
    RS = 59 - S
    RD = diff
    if H > 15:
        RD = diff - 1
    print ("Days Remaining:",RD, "Time Remaining:",RH,":",RM,":",RS)

    time.sleep(1)

