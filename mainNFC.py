#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# RFID-Leser initialisieren
reader = SimpleMFRC522()

try:
    print("Bitte RFID-Chip scannen...")
    _, text = reader.read()  # Nur den Text auslesen
    text = text.strip()  # Leerzeichen oder Zeilenumbrüche entfernen
    
    # Zutrittsbedingungen prüfen
    if text == "1701":
        print("Eintritt zu Nicis Haus erlaubt!")
    elif text == "2702":
        print("Eintritt zu Noahs Haus erlaubt!")
    else:
        print("Zutritt verweigert!")
        
finally:
    GPIO.cleanup()  # GPIO-Ressourcen freigeben
