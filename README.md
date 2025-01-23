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

## **Software-Funktionen**
1. **PIN-Eingabe**:
   - Überprüft den eingegebenen Code mit einem vordefinierten PIN.
2. **RFID-Verifizierung**:
   - Liest die UID des RFID-Chips/Karte und vergleicht sie mit gespeicherten Werten.
3. **Audiofeedback**:
   - Hoher Ton für erfolgreiche Authentifizierung.
   - Tiefer Ton für fehlerhafte Authentifizierung.

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
