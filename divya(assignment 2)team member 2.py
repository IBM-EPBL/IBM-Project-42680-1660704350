import os
import random
for i in range(30,80):
   h= random.uniform(10,99)
   t= random.uniform(10,99)
   temp=t
   humidity=h
   print(h)
   if (humidity>50 ):
     print("high alert")
   else:
     print("low")
   print(t) 
   if (temp>40):
     print("high alert")
   else:
     print("low")
   break
   
