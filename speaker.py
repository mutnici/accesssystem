import RPi.GPIO as GPIO
import time

# Pin-Definition
SPEAKER_PIN = 12  # GPIO 18 unterstützt PWM

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKER_PIN, GPIO.OUT)

# PWM starten
pwm = GPIO.PWM(SPEAKER_PIN, 449)  # Frequenz: 449 Hz (Tonhöhe)
pwm.start(50)  # Duty Cycle: 50% (Lautstärke)

# Ton für 2 Sekunden abspielen
time.sleep(2)

# PWM stoppen
pwm.stop()
GPIO.cleanup()
