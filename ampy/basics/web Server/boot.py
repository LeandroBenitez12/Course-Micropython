from machine import Pin
import network 
import time 

PIN_BLUE_LED = 2
PIN_YELLOW_LED = 14

name = 'TeleCentro-2efe'
password= 'Famili43621'

blue_led = Pin(PIN_BLUE_LED, Pin.OUT)
yellow_led = Pin(PIN_YELLOW_LED, Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

blue_led.off()
yellow_led.off()

def connectWf(name, password):
    while not wlan.isconnected():
        print('Trying Connect... ,wait please')
        print('Status: ', wlan.status())
        time.sleep(1)
        if wlan.status() == 1001:
            pass
        else:
            wlan.connect(name, password)
        blue_led.off()
        yellow_led.on()
        
if not wlan.isconnected():
    connectWf(name, password)
else:
    print('Connected')
    wlan.ifconfig()
    blue_led.on()
    yellow_led.off()
    
    
