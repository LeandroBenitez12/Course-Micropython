from machine import Pin 
import network  
import time

PIN_LED_BLUE = 2
PIN_LED_YELLOW = 14

led_blue =Pin(PIN_LED_BLUE , Pin.OUT)
led_yellow =Pin(PIN_LED_YELLOW , Pin.OUT)

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wifi_list = wlan.scan()        # scan for access points


    
for item in wifi_list:
    print(' Network: ' + str(item[0]) + '   Channel: ' + str(item[2]) + '   RSSI: ' + str(item[3])) 
    
def wifiConnect():
    while not wlan.isconnected():
        led_blue.off()
        led_yellow.on()
        print(' trying Connect...')
        time.sleep(1)
        print(wlan.status())
        if wlan.status() == 1001:
            pass
        else:
            wlan.connect('xxxxxxx-xxxx','xxxxxxx')
        led_blue.on()
        led_yellow.off()

if not wlan.isconnected():
    wifiConnect()
else:
    led_blue.on()
    led_yellow.on()

wlan.ifconfig()
