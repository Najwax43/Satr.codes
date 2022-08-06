# DATES AND NUMBERS

number=-999     # ايجادالقيمة المطلقة
print(abs(number))

number=3.673   # لتقريب العدد الى اقرب عدد صحيح
print(round(number))

number=3.673   # لتقريب العدد الى اقرب جزء من مئة
print(round(number,2))

number= 3  # الرفع للأس
print(pow(number,2))


print(pow(3, 2)) # الرفع للأس بطريقة ابسط

numbers=300,600,786,1000,276  # ايجاد اكبر واصغر قيمة
print(max(numbers))
print(min(numbers))

numbers=300,600,786,1000,276  # جمع مجموعة من الارقام
print(sum(numbers))


import math
number=144
print(math.sqrt(number)) # لايجاد الجذر التربيعي


# import math تم استدعائها في الاعلى
print(math.remainder(9,3)) # لايجاد باقي قسمة ٩


import random

print(random.randint(1,100) ) # لايجاد رقم عشوائي من ١- ١٠٠ وفي كل مرة تنفيذ يعطي رقم مختلف


import datetime
data= datetime.date(2020,2,13) # انشاء تاريخ
print(data.year) #  or (. day )or (. month)


#import datetime تم استدعائها في الاعلئ
time=datetime.time(12,14,15) # hours, minute, seconds انشاء الوقت
print(time.minute) # or (. minute) or ( .secnod)

#import datetime تم استدعائها في الاعلئ
now=datetime.datetime.today()
print(now.day) # or (.month) or ( .year)


#import datetime تم استدعائها في الاعلئ
data= datetime.date(2020,2,13)
time=datetime.time(14,5,17)

print(data)
print(time)
print(data.strftime('%A %B %Y')) # day ,month , year تحويل التاريخ الئ نص
print(time.strftime('%I %M  %S')) # hours , minute , second
