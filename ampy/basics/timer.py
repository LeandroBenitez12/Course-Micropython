from machine import Pin, Timer
import time

#declared pinouts
blueLed = Pin( 2, Pin.OUT)
yellowLed1 = Pin( 13, Pin.OUT)
yellowLed2 = Pin( 12, Pin.OUT)

#Variables for timer
led = 1 
period = 1000
#to set timer
tim1 = Timer(1)
tim1.init(period=period, mode=Timer.PERIODIC, callback=lambda t:
          setLed()
)

#function for to set Led
def setLed():
    global led 
    if led == 1:
        blueLed.value(1)
        yellowLed1.off()
        yellowLed2.off()
        
    elif led == 2:
        blueLed.value(0)
        yellowLed1.on()
        yellowLed2.off()
    elif led == 3:
        blueLed.value(0)
        yellowLed1.off()
        yellowLed2.on()
    else:
        blueLed.value(0)
        yellowLed1.off()
        yellowLed2.off()
    print(f'Led On: {led}')
    led +=1
    if led > 4:
        led =1