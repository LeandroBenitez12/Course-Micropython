from machine import Pin

PIN_BUTTON = 32
PIN_LED_B = 2
PIN_LED_Y = 14
#variables PWM
freq = 500
id = 0
ledY = Pin(PIN_LED_Y, Pin.OUT)
ledB = Pin(PIN_LED_B, Pin.OUT)

button = Pin(PIN_BUTTON, Pin.PULL_DOWN)
ledB.off()
ledY.off()
print("Getting started")
while True:
    state_button = button.value()
    if id == 0:
        ledB.off()
        ledY.off()
    if state_button == 1:
        id = id + 1

    if id ==1:
        ledB.on()
        ledY.off()
    if id ==2:
        ledY.on()
        ledB.off()
    if id == 3:
        ledB.on()
        ledY.on()
    if id > 3:
        id = 0
    if state_button == 1:
        print("Press button || id: ",id)
# def highLed():
#     global count, led
    
#     if count == 0:
#         ledB.on()
#         ledY.off()
#         print('Blue led on')
#     if count == 1:
#         ledB.off()
#         ledY.on()
#         print('Yellow led on')
#     if count == 2:
#         ledB.off()
#         ledY.off()
#         print('Red led on')

#     count += 1
#     if count > 2:
#         count = 0

# state_button.irq(handler= highLed, trigger= Pin.IRQ_RISING)
