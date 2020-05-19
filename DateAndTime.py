# To get current Date And Time 

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

# To get current Date


import datetime

date_object = datetime.date.today()
print(date_object)

# Todays Day Month and Year 


from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# To Print hour, minute, second and microsecond

from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)