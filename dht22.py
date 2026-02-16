# /// script
# requires-python = ">=3.9"
# dependencies = ["adafruit-circuitpython-dht", "adafruit-blinka", "rpi.gpio"]
# ///
"""
Lecture du capteur DHT22 (protocole one-wire sur GPIO)

Laboratoire Semaine 2 : GPIO, capteurs et Git
Cours 243-413-SH, Semaine 2
"""

import board
import adafruit_dht
import time

# Initialisation du capteur sur GPIO 4 (Pin 7)
# Le DHT22 utilise un protocole one-wire, PAS I2C
dht = adafruit_dht.DHT22(board.D4)

print("=== Lecture du DHT22 ===")
print("Protocole : one-wire sur GPIO 4")
print()

def lire_avec_retry(max_tentatives=5):
    """
    Lit le DHT22 avec plusieurs tentatives.
    Le DHT22 peut echouer occasionnellement (comportement normal).
    """
    for tentative in range(max_tentatives):
        try:
            temperature = dht.temperature
            humidite = dht.humidity

            if temperature is not None and humidite is not None:
                return temperature, humidite

        except RuntimeError as e:
            # Erreurs de lecture sont normales pour le DHT22
            print(f" Tentative {tentative + 1}/{max_tentatives} : {e}")
            time.sleep(2) # Attendre 2 secondes avant de reessayer

    return None, None

# Lecture avec retry
print("Lecture en cours (peut prendre quelques secondes)...")
temperature, humidite = lire_avec_retry()

if temperature is not None:
    print()
    print(f"Temperature : {temperature:.1f} C")
    print(f"Humidite : {humidite:.1f} % RH")
else:
    print()
    print("ERREUR : Impossible de lire le capteur apres 5 tentatives")
    print("Verifiez :")
    print(" 1. Le cablage (DATA sur Pin 7 / GPIO 4)")
    print(" 2. L'alimentation (VCC sur Pin 1 / 3.3V)")
    print(" 3. La bibliotheque (adafruit-circuitpython-dht)")

# Nettoyage
dht.exit()
print("\n=== Termine ===")