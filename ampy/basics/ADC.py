from machine import Pin
from machine import ADC

PIN_CNY70 = 32
PIN_YELLOW_LED = 14

yellow_led = Pin(PIN_YELLOW_LED, Pin.OUT)

cny70 = ADC(PIN_CNY70)

read_cny70 = cny70.read()
while True:
    print(read_cny70)