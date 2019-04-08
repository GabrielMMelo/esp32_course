import time
from machine import Pin

blue_led = Pin(18, Pin.OUT)
red_led = Pin(19, Pin.OUT)


def purple_rain():
    while True:
        blue_led.on()
        red_led.on()
        time.sleep_ms(1000)
        blue_led.off()
        red_led.off()
        time.sleep_ms(1000)
