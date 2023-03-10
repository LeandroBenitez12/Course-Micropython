from machine import Pin
from machine import ADC
from machine import Timer

PIN_CNY70 = 32
PIN_YELLOW_LED = 14

yellow_led = Pin(PIN_YELLOW_LED, Pin.OUT)

cny70 = ADC(Pin(PIN_CNY70))
cny70.atten(ADC.ATTN_11DB)
read_cny70 = cny70.read()

tim1= Timer(1)
tim1.init(period=500, mode= Timer.PERIODIC, callback = lambda t:
    print(read_cny70)
)