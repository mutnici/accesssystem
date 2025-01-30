#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from pad4pi import rpi_gpio
import time

# GPIO-Konfiguration
SPEAKER_PIN = 12
ROWS = [17, 27, 22, 23]  # Zeilen-Pins der Tastatur
COLS = [5, 6, 13, 19]    # Spalten-Pins der Tastatur

# Layout der Tastatur
KEYPAD = [
    ["D", "C", "B", "A"],
    ["#", "9", "6", "3"],
    ["0", "8", "5", "2"],
    ["*", "7", "4", "1"]
]

# PIN und RFID-Zugriffsrechte
CORRECT_PIN = "1234"
VALID_RFID_TAGS = {"1701": "Haus 1", "2702": "Haus 2"}
entered_pin = ""

# RFID-Leser initialisieren
reader = SimpleMFRC522()

# GPIO-Setup für den Lautsprecher
def setup_gpio():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SPEAKER_PIN, GPIO.OUT)

# PWM-Instanz erstellen
pwm = None
def setup_pwm():
    global pwm
    pwm = GPIO.PWM(SPEAKER_PIN, 440)

# Funktion für Zugriff erlaubt
def access_granted():
    pwm.ChangeFrequency(1000)
    pwm.start(50)
    time.sleep(1)
    pwm.stop()
    print("Zugang gewährt!")
    exit(0)

# Funktion für Zugriff verweigert
def access_denied():
    pwm.ChangeFrequency(200)
    pwm.start(50)
    time.sleep(1)
    pwm.stop()
    print("Zugang verweigert!")

# Funktion zur Verarbeitung der Tastenereignisse
def process_key(key):
    global entered_pin
    if key == "#":  # Bestätigungstaste
        if entered_pin == CORRECT_PIN:
            access_granted()
        else:
            access_denied()
            print("Falscher PIN! Bitte erneut versuchen.")
        entered_pin = ""
    elif key == "*":  # Eingabe zurücksetzen
        entered_pin = ""
        print("Eingabe zurückgesetzt!")
    else:
        entered_pin += key
        print(f"Eingegebener Code: {entered_pin}")

# Tastatur-Setup
def setup_keypad():
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROWS, col_pins=COLS)
    keypad.registerKeyPressHandler(process_key)
    return keypad

# RFID-Überprüfung
def check_rfid():
    while True:
        print("Bitte RFID-Chip scannen...")
        _, text = reader.read()
        tag = text.strip()
        if tag in VALID_RFID_TAGS:
            print(f"Eintritt zu {VALID_RFID_TAGS[tag]} erlaubt!")
            access_granted()
        else:
            print("Unbekannter RFID-Chip! Bitte erneut versuchen.")
            access_denied()

# Hauptprogramm
def main():
    setup_gpio()
    setup_pwm()
    keypad = setup_keypad()

    try:
        while True:
            print("Wählen Sie die Zugangsmethode:")
            print("1 - RFID")
            print("2 - PIN")
            method = input("Eingabe: ").strip()

            if method == "1":
                check_rfid()
            elif method == "2":
                print("Bitte geben Sie den PIN ein. Mit '#' bestätigen.")
                while True:
                    time.sleep(0.1)  # Warten auf Tastenereignisse
            else:
                print("Ungültige Auswahl! Bitte 1 oder 2 eingeben.")
    except KeyboardInterrupt:
        print("\nProgramm beendet.")
    finally:
        keypad.cleanup()
        GPIO.cleanup()

if __name__ == "__main__":
    main()