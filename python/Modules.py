# import Inheritance as Inh

# fa1 = Inh.Father("Mehran" , "Shafiei" , 3 , 47 , "Akram Nazari" , 1 , 21 , "Amir hossain" , job = "worker" , company = "erish khodro")
# fa1.About_father()

# #(------------------------------------------------------------------------------------------------------------------------------------------)

# from Inheritance import Mother
# m1 = Mother("Akram" , "Nazari" , 3 , 39 , "Mehran Shafiei" , 1 , 21 , "Amir hossain" , job = "Disput resolution council" , location = "Qazvin")
# m1.About_Mother()

# #(------------------------------------------------------------------------------------------------------------------------------------------)

from Functions import friends , G_mail_password , Converter

print(friends["first"])

password = input("Pleas inter your G mail password : ")
password = password.replace(" ", "")

while G_mail_password(password) == False :
    password = input("you wrong :( \ntry again : ")
    password = password.replace(" ", "")
else :   
    print("your G mail password successfully saved :)")

print(password)

while True :
    day = int(input("Pleas inter your birth day : "))
    month = int(input("Pleas inter your birth month: "))
    year = int(input("Pleas inter your birth year : "))

    Converter(day , month , year)

# #(------------------------------------------------------------------------------------------------------------------------------------------)

# from Notes import *

# Hello("Amir hossain Shafiei")
# Goodbuy("Amir hossain")
# Test()
# print(x)

# # * = every things

# #(==========================================================================================================================================)

# import platform

# print(platform.processor)
# print(platform.architecture)
# print(platform.system)
# print(platform.version)
# print(platform.release)

# import random

# list = ["Amir hossain" , "Sina" , "Parham" , "Mohammad ali" , "Sadra" , "Parham zg"]

# print(random.randint(100 , 999))
# print(random.randrange(0 , 20))
# print(random.choice(list))

## mudule baady kheyly moham 

# import datetime 

# # ba cntl + click mitony vared datetime beshy
# import pytz
# x = datetime.datetime.now()

# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.minute)
# print(x.second)

# x = datetime(2023 , 2 , 7)
# print(x)
# print(x.strftime("%a"))
# print(x.strftime("%A"))
# print(x.strftime("%b"))
# print(x.strftime("%B"))

# import pytz
# tz = pytz.timezone("Asia/Tehran")
# x = datetime.timetz(tz)
# print(tz)

# # (---------------------------------------------------------------------------------------------)

# from datetime import datetime , timedelta 

# start = datetime.now()

# end1 = start + timedelta(days=30)
# x = end1 - start

# print(x)
# print(x.days)
# print(start)
# print(end)

# print(x.total_seconds())            # secound
# print(x.total_seconds() / 60)       # minute 
# print(x.total_seconds() / 3600)     # hour
# print(x.total_seconds() / 86400)    # day

# end2 = start  + timedelta(hours=48)
# x = end2 - start

# print(x.total_seconds() / 3600)     # hour
# print(x.days)

# end3 = start + timedelta(minutes=4200)
# x = end3 - start

# print(x.days)
# print(x.total_seconds() / 3600)

# # mitavanim ba estefade az int اعشار an ra hazf konim.

# # ماژوووووووووووووووووووووووووووووول  :)