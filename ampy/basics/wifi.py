from machine import Pin 
import network  
PIN_LED_BLUE = 2
PIN_LED_YELLOW = 14

led_blue =Pin(PIN_LED_BLUE , Pin.OUT)
led_yellow =Pin(PIN_LED_YELLOW , Pin.OUT)

led_blue.off()
led_yellow.on()

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wifi_list = wlan.scan()        # scan for access points

print(wifi_list)

for item in wifi_list:
    print(item)