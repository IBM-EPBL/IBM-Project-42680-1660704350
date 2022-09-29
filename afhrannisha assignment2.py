import random

temp= random.uniform(10.0,80.0)
print( "Temperature is",temp)
if (temp<46):
    print("Alram is on ")
else:
    print("Alram is off")
humidity= random.uniform(30,60)
print("Humidity is", humidity)
if (humidity<87):
     print("Alram is on ")
else:
     print("Alram is off")
