from machine import Pin, PWM

PIN_RED_LED = 12
PIN_YELLOW_LED = 14
PIN_BLUE_LED = 2

led_red = PWM(Pin(PIN_RED_LED))
led_yellow = PWM(Pin(PIN_YELLOW_LED))
led_blue = PWM(Pin(PIN_BLUE_LED))