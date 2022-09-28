import os
import random
for i in range(30,80):
   h= random.uniform(10,99)
   t= random.uniform(20,60)
   temp=t
   humidity=h
   print("the current temperature is:",h)
   if (humidity>80 ):
     print("alarm is on")
   else:
     print("alarm is off")
   print("the current temperature is:",t) 
   if (temp>50):
     print("alarm is on")
   else:
     print("alarm is off")
   break
   
