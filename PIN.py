from pad4pi import rpi_gpio
import time

# GPIO-Konfiguration für die Tastatur
ROWS = [17, 27, 22, 23]  # Zeilen-Pins
COLS = [5, 6, 13, 19]    # Spalten-Pins

# Erstellen Sie ein Layout für die Tastatur
KEYPAD = [
    ["D", "C", "B", "A"],  # Reihen 1 bis 4
    ["#", "9", "6", "3"],
    ["0", "8", "5", "2"],
    ["*", "7", "4", "1"]
]


factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROWS, col_pins=COLS)

# PIN zur Überprüfung
CORRECT_PIN = "1234"  # Beispiel-PIN
entered_pin = ""

def process_key(key):
    global entered_pin
    if key == "#":  # "#" dient als Enter-Taste
        if entered_pin == CORRECT_PIN:
            print("Zugang erlaubt!")
        else:
            print("Falscher PIN!")
        entered_pin = ""  # Zurücksetzen
    elif key == "*":  # "*" dient als Zurücksetzen
        entered_pin = ""
        print("Eingabe zurückgesetzt!")
    else:
        entered_pin += key
        print(f"Eingegebener Code: {entered_pin}")

keypad.registerKeyPressHandler(process_key)

try:
    print("Bitte geben Sie den PIN ein. Mit '#' bestätigen.")
    while True:
        time.sleep(0.1)  # Für Stabilität
except KeyboardInterrupt:
    print("\nProgramm beendet.")
finally:
    keypad.cleanup()
