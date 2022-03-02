import datetime
import numpy as np

today = datetime.date.today()
d1 = today.strftime("%m/%d/%y")
end = datetime.date(2022,5,27)
print ("today:", d1)
#diff = end - today
springbreak = ['2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-04-15']
diff = np.busday_count(today, end, holidays=springbreak)
print ("days remaining:", diff)

 
