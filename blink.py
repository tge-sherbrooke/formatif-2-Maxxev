# /// script
# requires-python = ">=3.9"
# dependencies = ["adafruit-blinka", "rpi.gpio"]
# ///
"""
Script de clignotement LED
Cours 243-413-SH, Semaine 2
"""
import board
import digitalio
import time

# Configuration
led = digitalio.DigitalInOut(board.D17) # GPIO 17 = Pin 11
led.direction = digitalio.Direction.OUTPUT

print("Clignotement de la LED (Ctrl+C pour arreter)")

try:
    while True:
        led.value = True
        print("LED ON")
        time.sleep(0.5)
        led.value = False
        print("LED OFF")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nArret")

finally:
    led.deinit()
    print("GPIO libere")