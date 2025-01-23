from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time

# GPIO-Konfiguration für die Tastatur
ROWS = [17, 27, 22, 23]  # Zeilen-Pins
COLS = [5, 6, 13, 19]    # Spalten-Pins

# GPIO-Konfiguration für den Lautsprecher
SPEAKER_PIN = 12  

# Layout für die Tastatur
KEYPAD = [
    ["D", "C", "B", "A"],  # Reihen 1 bis 4
    ["#", "9", "6", "3"],
    ["0", "8", "5", "2"],
    ["*", "7", "4", "1"]
]

# PIN zur Überprüfung
CORRECT_PIN = "1234"  #korrekter PIN
entered_pin = ""

# GPIO-Setup für den Lautsprecher
GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKER_PIN, GPIO.OUT)

# PWM-Instanz erstellen
pwm = GPIO.PWM(SPEAKER_PIN, 440)  # 440 Hz

# Funktion für Zugriff erlaubt (hoher Ton)
def access_granted():
    pwm.ChangeFrequency(1000)  # 1kHz
    pwm.start(50)  # Lautstärke 50%
    time.sleep(1)  # 1 Sekunde Ton
    pwm.stop()
   

# Funktion für Zugriff verweigert (tiefer Ton)
def access_denied():
    pwm.ChangeFrequency(200)  # Frequenz 440 Hz
    pwm.start(50)  # Lautstärke 50%
    time.sleep(1)  # 1 Sekunde Ton
    pwm.stop()

# Funktion zur Verarbeitung der Tastenereignisse
def process_key(key):
    global entered_pin
    if key == "#":  # "#" dient als Enter-Taste
        if entered_pin == CORRECT_PIN:
            print("Zugang erlaubt!")
            access_granted()  # Lautsprecher: Zugang erlaubt
        else:
            print("Falscher PIN!")
            access_denied()  # Lautsprecher: Zugang verweigert
        entered_pin = ""  
    elif key == "*":  # "*" dient als Zurücksetzen
        entered_pin = ""
        print("Eingabe zurückgesetzt!")
    else:
        entered_pin += key
        print(f"Eingegebener Code: {entered_pin}")

# Tastatur-Setup
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROWS, col_pins=COLS)
keypad.registerKeyPressHandler(process_key)

try:
    print("Bitte geben Sie den PIN ein. Mit '#' bestätigen.")
    while True:
        time.sleep(0.1)  # Für Stabilität
except KeyboardInterrupt:
    print("\nProgramm beendet.")
finally:
    keypad.cleanup()
    GPIO.cleanup()
