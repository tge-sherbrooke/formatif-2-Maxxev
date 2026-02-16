# /// script
# requires-python = ">=3.9"
# dependencies = ["adafruit-blinka", "rpi.gpio"]
# ///
"""
Chenillard RGB - Controle de 3 LEDs
Cours 243-413-SH, Semaine 2
"""

import board
import digitalio
import time

# Configuration des LEDs
led_rouge = digitalio.DigitalInOut(board.D17) # GPIO 17 = Pin 11
led_rouge.direction = digitalio.Direction.OUTPUT

led_verte = digitalio.DigitalInOut(board.D27) # GPIO 27 = Pin 13
led_verte.direction = digitalio.Direction.OUTPUT

led_jaune = digitalio.DigitalInOut(board.D22) # GPIO 22 = Pin 15
led_jaune.direction = digitalio.Direction.OUTPUT

leds = [led_rouge, led_verte, led_jaune]

print("Chenillard RGB demarre (Ctrl+C pour arreter)")

try:
    while True:
        for led in leds:
            led.value = True
            time.sleep(0.3)
            led.value = False

except KeyboardInterrupt:
    print("\nArret")

finally:
    for led in leds:
        led.value = False
        led.deinit()
        print("GPIO libere")