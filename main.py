from machine import Pin
from time import sleep
led1=Pin(1,Pin.OUT)
led2=Pin(5,Pin.OUT)
led3=Pin(13,Pin.OUT)
led4=Pin(20,Pin.OUT)
led5=Pin(19,Pin.OUT)
led6=Pin(18,Pin.OUT)
while True:
  led1.on()
  led6.on()
  led2.off()
  led3.off()
  led4.off()
  led5.off()
  sleep(1)

  led2.on()
  led5.on()
  led1.off()
  led3.off()
  led4.off()
  led6.off()
  sleep(1)


  led4.on()
  led3.on()
  led2.off()
  led1.off()
  led6.off()
  led5.off()
  sleep(1)

  led5.on()
  led2.on()
  led1.off()
  led3.off()
  led4.off()
  led6.off()
  sleep(1)
  
 
 
  
   
  


