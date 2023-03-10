from machine import Pin, PWM
from machine import Timer

PIN_RED_LED = 2
PIN_BLUE_LED = 14
PIN_YELLOW_LED = 12
sum_duty = 5
DUTY_MAX= 1023
#variables globals
frequency= 100
duty= 1023
dutyOff= 0
led = 1
period= 20

# #declared pinouts
# led_blue = PWM(Pin(PIN_BLUE_LED))
# led_yellow = PWM(Pin(PIN_YELLOW_LED))
# led_red = PWM(Pin(PIN_RED_LED))

# #I declare the PWM Frequency (from 1Hz to 40MHz)
# #freq = pwm0.freq()         # get current frequency (default 5kHz)
# led_blue.freq(frequency)
# led_red.freq(frequency)
# led_yellow.freq(frequency)
# # get current duty cycle, range 0-1023 (default 512, 50%)
# led_blue.duty(dutyOff)
# led_yellow.duty(dutyOff)
# led_red.duty(dutyOff)       

#Method to get all in one line
led_blue = PWM(Pin(PIN_BLUE_LED), freq=frequency, duty=dutyOff)  # create and configure in one go
led_yellow = PWM(Pin(PIN_YELLOW_LED), freq=frequency, duty=dutyOff)# dutyOff inicializate off
led_red = PWM(Pin(PIN_RED_LED), freq=frequency, duty=dutyOff)

#timer functions Periodics
tim= Timer(1)
tim.init(period=period, mode=Timer.PERIODIC, callback=lambda t:
        setLed()         
)
#function for to set the leds
def setLed():
    global led, duty, dutyOff
    duty += sum_duty
    if duty > DUTY_MAX:
        duty = dutyOff
        led+=1
        if led > 3:
            led = 1
            
    if led == 1:
        led_blue.duty(duty)
        led_yellow.duty(dutyOff)
        led_red.duty(dutyOff)    
    elif led == 2:
        led_blue.duty(dutyOff)
        led_yellow.duty(duty)
        led_red.duty(dutyOff)    
    elif led == 3:
        led_blue.duty(dutyOff)        
        led_yellow.duty(dutyOff)
        led_red.duty(duty)            