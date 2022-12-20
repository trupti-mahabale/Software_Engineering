#libraries are imported
import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("truptimahabale000@gmail.com", "ltkw lmkn bcwg vzvs")
emailid = "trupti02@dbatu.ac.in"
s.sendmail('truptimahabale000@gmail.com',emailid,msg)
a = input("Enter Your OTP >>:")

if a == OTP:
        print("Verified")
else:
        print("PLease Check your OTP again")
