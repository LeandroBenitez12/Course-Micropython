from machine import Pin
import bluetooth
from BLE import BLEUART

PIN_LED_BLUE = 2
PIN_LED_YELLOW = 14

led_blue =Pin(PIN_LED_BLUE , Pin.OUT)
led_yellow =Pin(PIN_LED_YELLOW , Pin.OUT)

led_yellow.off()
led_blue.off()
# INIT BLUETOOTH 
name = "ESP32"
ble = bluetooth.BLE()
uart = BLEUART(ble, name, rxbuf=1000)

# bluetooh rx 
rx = uart.read().decode().strip()
uart.write('Esp32 says: '+ str(rx)+ '\n')
if rx == 'B':
    led_blue.on()
    
elif rx == 'Y':
    led_yellow.on()
    led_blue.off()
elif rx == 'A':
    led_yellow.on()
    led_blue.on()