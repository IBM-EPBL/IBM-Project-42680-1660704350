import RPi.GPIO as GPIO  
import time  
#assign numbering for the GPIO using BCM  
GPIO.setmode(GPIO.BCM)  
#assingn number for the GPIO using Board  
#GPIO.setmode(GPIO.BOARD)  
  
cnt = 0  
MAIL_CHECK_FREQ = 1  
RED_LED = 4  
GPIO.setup(RED_LED, GPIO.OUT)  
while True:   
 GPIO.output(RED_LED, False)  
 cnt = 1
 ifcnt==0
else:  
 GPIO.output(RED_LED, True)  
 cnt = 0  
  
time.sleep(MAIL_CHECK_FREQ)  
GPIO.cleanup()  
