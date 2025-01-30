# Access System Projekt

## **Projektbeschreibung**
Dieses Projekt implementiert ein Zugangssystem basierend auf einem **Raspberry Pi Zero 2**. Der Zugang kann entweder durch Eingabe eines PIN-Codes über eine Tastatur oder durch die Verwendung eines **RFID-Chips** oder einer **RFID-Karte** erfolgen. Ein Lautsprecher gibt ein akustisches Feedback, um anzuzeigen, ob der Zugang gewährt oder verweigert wurde.

---

## **Hardware-Komponenten**
1. **Raspberry Pi Zero 2**
   - Hauptcontroller des Systems.
2. **PIN-Tastatur**
   - Ermöglicht die Eingabe eines Zugangscodes.
3. **RFID-Reader (RC522)**
   - Liest RFID-Chips oder -Karten zur Zugangskontrolle.
4. **Lautsprecher** (angeschlossen an den PWM-Pin)
   - Gibt akustische Signale für Erfolg oder Fehler aus.

---

## **Funktionsweise**
1. **PIN-Tastatur**:
   - Der Benutzer gibt einen Zugangscode ein und bestätigt mit `#`.
   - **Richtiger Code**: Ein hoher Ton ertönt, und der Zugang wird gewährt.
   - **Falscher Code**: Ein tiefer Ton ertönt, und der Zugang wird verweigert.

2. **RFID-Reader (RC522)**:
   - Der Benutzer hält einen RFID-Chip oder eine Karte an den Reader.
   - **Richtiger Chip/Karte**: Ein hoher Ton ertönt, und der Zugang wird gewährt.
   - **Falscher Chip/Karte**: Ein tiefer Ton ertönt, und der Zugang wird verweigert.

3. **Lautsprecher**:
   - Über PWM (z. B. GPIO 18) angeschlossen.
   - Gibt akustisches Feedback für die Zugangsergebnisse:
     - **Hoher Ton**: Zugriff erlaubt.
     - **Tiefer Ton**: Zugriff verweigert.

---

## **GPIO-Belegung**
| **Komponente**       | **GPIO-Pin**       |
|----------------------|--------------------|
| Lautsprecher (PWM)   | GPIO 18            |
| PIN-Tastatur (Zeilen)| GPIO 17, 27, 22, 23|
| PIN-Tastatur (Spalten)| GPIO 5, 6, 13, 19 |
| RFID-Reader (RC522)  | SPI (MOSI, MISO, SCK, SS, IRQ) |

---
# **Zuvor benötigte Einstellungen**
## **1. Installation der benötigten Bibliotheken**
Vor der Nutzung des Zugangssystems müssen einige Python-Bibliotheken installiert werden:
```sh
sudo apt update
sudo apt install python3-pip
pip3 install RPi.GPIO mfrc522 pad4pi
```

Falls es Probleme mit `mfrc522` gibt, kann stattdessen folgendes verwendet werden:
```sh
pip3 install spidev
```

---

## **2. SPI-Schnittstelle aktivieren**
Der MFRC522 RFID-Leser kommuniziert über SPI. Um die SPI-Schnittstelle auf dem Raspberry Pi zu aktivieren, folge diesen Schritten:
1. Öffne die Raspberry Pi Konfiguration:
   ```sh
   sudo raspi-config
   ```
2. Navigiere zu **Interfacing Options** → **SPI**
3. Aktiviere SPI und bestätige mit **OK**
4. Starte den Raspberry Pi neu:
   ```sh
   sudo reboot
   ```

---


# **Erklärung der angefügten Dateien**
## **RFID**
- *onlynfc.py* ist nur für NFC-Überprüfung.
- *write.py* ist für das Beschreiben der RFID-Chips.
- *read.py* ist für das Auslesen der RFID-CHIPS
## **PIN**
- *PIN.py* ist nur für PIN-Überprüfung.
- *pinwspeaker.py* ist für PIN-Überprüfung und Speaker Ausgabe. 
- *speaker.py* ist Testcode für den Speaker. 
## **Gesamter Code**
- *mainall.py* ist der gesamte Code (Anleitung unten!).


# **Anleitung zur Nutzung des Zugangssystems mit PIN und RFID**

## **1. System starten**
1. Verbinde alle Komponenten gemäß der Hardware-Konfiguration.
2. Starte das Raspberry Pi und öffne ein Terminal.

---

## **2. Zugangsmethode wählen**
Nach dem Start wird folgende Auswahl angezeigt:
   ```sh
   echo "Wählen Sie die Zugangsmethode:"
   echo "1 - RFID"
   echo "2 - PIN"
   read -p "Eingabe: " method
   ```
   
Gib entweder **„1“** für den RFID-Zugang oder **„2“** für den PIN-Code ein und drücke **Enter**.

---

## **3. Zugang mit RFID**
1. Falls RFID ausgewählt wurde, erscheint die Aufforderung:
   ```sh
   echo "Bitte RFID-Chip scannen..."
   ```
2. Halte einen RFID-Tag an den Leser.
3. Falls der Chip registriert ist (z. B. "1701" für Haus 1), erscheint:
   ```sh
   echo "Eintritt zu Haus 1 erlaubt!"
   echo "Zugang gewährt!"
   ```
   und das Programm beendet sich.
4. Falls der Chip unbekannt ist, erscheint:
   ```sh
   echo "Unbekannter RFID-Chip! Bitte erneut versuchen."
   echo "Zugang verweigert!"
   ```
   und es kann erneut versucht werden.

---

## **4. Zugang mit PIN-Code**
1. Falls PIN gewählt wurde, erscheint:
   ```sh
   echo "Bitte geben Sie den PIN ein. Mit '#' bestätigen."
   ```
2. Gib den PIN über die Tastatur ein (z. B. **„1234#“** für den richtigen PIN).
3. Falls der PIN korrekt ist:
   ```sh
   echo "Zugang gewährt!"
   ```
   und das Programm beendet sich.
4. Falls der PIN falsch ist:
   ```sh
   echo "Falscher PIN! Bitte erneut versuchen."
   echo "Zugang verweigert!"
   ```
   und es kann ein neuer PIN eingegeben werden.

---

## **5. Programm beenden**
Falls das Programm manuell beendet werden soll, kann **Strg + C** im Terminal gedrückt werden.

---

## **Einsatzmöglichkeiten**
- Zugangskontrolle für Türen.
- Sichere Zutrittsberechtigungen für Büros, Schulen oder private Bereiche.
- Kombination von PIN und RFID zur Erhöhung der Sicherheit.

---
## **Zukunftserweiterungen**
- Implementierung eines **Webinterfaces** zur Verwaltung von PINs und RFID-Daten.
- Integration von **Cloud-Diensten** für Echtzeitüberwachung.
- Hinzufügen eines Displays zur visuellen Anzeige von Statusmeldungen.



