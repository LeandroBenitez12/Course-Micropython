from machine import Pin
import time

PIN_RED_LED = 12
PIN_YELLOW_LED = 14
PIN_BLUE_LED = 2
# variables
time_red  = 500
time_yellow = 500
time_blue = 500
state_red = 0
state_yellow = 1
state_blue = 2
changed_state = True
id = state_red

led_red = Pin(PIN_RED_LED, Pin.OUT)
led_yellow = Pin(PIN_YELLOW_LED, Pin.OUT)
led_blue = Pin(PIN_BLUE_LED, Pin.OUT)

led_red.off()
led_yellow.off()
led_blue.off()

while True:
    if id == state_red:
        led_red.on()
        led_yellow.off()
        led_blue.off()
        time.sleep(12)
        changed_state = True
        id = state_yellow

    if id == state_yellow:
        led_red.off()
        led_yellow.on()
        led_blue.off()
        time.sleep(1)
        if changed_state:
            id = state_blue
        else:
            id = state_red

    if id == state_blue:
        led_red.off()
        led_yellow.off()
        led_blue.on()
        time.sleep(4)
        changed_state = False
        id = state_yellow
        