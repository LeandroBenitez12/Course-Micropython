from machine import Pin
import time

blueLed = Pin(2, Pin.OUT)
id = 0

while id < 4:
    blueLed.on()
    time.sleep(1.0)  # Delay for 1 second.

    blueLed.value(0)
    time.sleep(1.0)  # Delay for 1 second.
    id = id + 1
