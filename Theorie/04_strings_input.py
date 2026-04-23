# ============================================================
# BLOCK 4 – Strings, input() und f-Strings
# ============================================================
# Lies jede Frage durch und schreib deine Antwort hinter # ANTWORT:
# Danach kommt direkt eine kleine Code-Aufgabe zum Ausprobieren.
# Wenn du nicht weiterkommst, frag Google, eine KI oder mich.
#
# Wenn du fertig bist: Datei einmal komplett ausführen (Run).
# Du siehst dann für jede Aufgabe, ob sie korrekt ist.
# ============================================================


# ------------------------------------------------------------
# 4.1 – String Grundlagen
# ------------------------------------------------------------

# FRAGE: Was ist ein String? Wie erkennt man ihn im Code?
# ANTWORT: ...

# FRAGE: Was ist der Unterschied zwischen diesen beiden Zeilen?
#         alter = 15
#         alter = "15"
# ANTWORT: ...

# CODE-AUFGABE: Fülle die Lücken aus – was gibt dieser Code aus?
#               Ersetze jeweils None durch deine Antwort.
#               Führe danach die Datei aus um zu prüfen ob du richtig lagst.

text = "Tictactoe"

laenge        = None   # <- wie lang ist der String? (Zahl)
erstes_zeichen = None  # <- welches Zeichen hat Index 0? (String)
letztes_zeichen = None # <- welches Zeichen hat Index -1? (String)
grossbuchstaben = None # <- text komplett in Großbuchstaben (String)
kleinbuchstaben = None # <- text komplett in Kleinbuchstaben (String)

print(laenge)
print(erstes_zeichen)
print(letztes_zeichen)
print(grossbuchstaben)
print(kleinbuchstaben)

# --- TEST 4.1 ---
assert laenge is not None,          "laenge ist noch leer – schau nochmal in die Aufgabe"
assert erstes_zeichen is not None,  "erstes_zeichen ist noch leer – schau nochmal in die Aufgabe"
assert letztes_zeichen is not None, "letztes_zeichen ist noch leer – schau nochmal in die Aufgabe"
assert grossbuchstaben is not None, "grossbuchstaben ist noch leer – schau nochmal in die Aufgabe"
assert kleinbuchstaben is not None, "kleinbuchstaben ist noch leer – schau nochmal in die Aufgabe"
assert laenge         == len(text),       "laenge ist nicht korrekt – schau nochmal in die Aufgabe"
assert erstes_zeichen == text[0],         "erstes_zeichen ist nicht korrekt – schau nochmal in die Aufgabe"
assert letztes_zeichen == text[-1],       "letztes_zeichen ist nicht korrekt – schau nochmal in die Aufgabe"
assert grossbuchstaben == text.upper(),   "grossbuchstaben ist nicht korrekt – schau nochmal in die Aufgabe"
assert kleinbuchstaben == text.lower(),   "kleinbuchstaben ist nicht korrekt – schau nochmal in die Aufgabe"
print("Test 4.1 bestanden: String Grundlagen korrekt")
print()


# ------------------------------------------------------------
# 4.2 – String Methoden
# ------------------------------------------------------------

# FRAGE: Was macht .strip()? Wann ist das nützlich?
# ANTWORT: ...

# FRAGE: Was macht .replace()? Gib ein Beispiel.
# ANTWORT: ...

# CODE-AUFGABE: Ein Spieler gibt seinen Namen ein aber mit versehentlichen
#               Leerzeichen davor und danach: "  Anna  "
#               Bereinige den Namen mit .strip() und speichere ihn in bereinigt.

spieler_eingabe = "  Anna  "
bereinigt = None   # <- ersetze None durch den bereinigten String

print(bereinigt)

# --- TEST 4.2 ---
assert bereinigt is not None,      "bereinigt ist noch leer – schau nochmal in die Aufgabe"
assert bereinigt == "Anna",        "strip() wurde nicht korrekt angewendet – schau nochmal in die Aufgabe"
assert bereinigt[0] != " ",        "Am Anfang sind noch Leerzeichen – schau nochmal in die Aufgabe"
assert bereinigt[-1] != " ",       "Am Ende sind noch Leerzeichen – schau nochmal in die Aufgabe"
print("Test 4.2 bestanden: strip() korrekt angewendet")
print()


# ------------------------------------------------------------
# 4.3 – Strings zusammensetzen
# ------------------------------------------------------------

# FRAGE: Wie kann man zwei Strings zusammensetzen? Nenne zwei Wege.
# ANTWORT: ...

# CODE-AUFGABE A: Setze Name und Zeichen mit + zusammen.
#                 Ausgabe soll sein: "Spieler Anna spielt mit X"

spieler_name = "Anna"
zeichen = "X"

ausgabe = None   # <- ersetze None durch den zusammengesetzten String mit +
print(ausgabe)

# CODE-AUFGABE B: Mache dasselbe mit einem f-String.
#                 Ausgabe soll sein: "Spieler Anna spielt mit X"

ausgabe_f = None   # <- ersetze None durch einen f-String
print(ausgabe_f)

# --- TEST 4.3 ---
assert ausgabe is not None,   "ausgabe ist noch leer – schau nochmal in die Aufgabe"
assert ausgabe_f is not None, "ausgabe_f ist noch leer – schau nochmal in die Aufgabe"
assert ausgabe   == "Spieler Anna spielt mit X", "Die Ausgabe mit + ist nicht korrekt – schau nochmal in die Aufgabe"
assert ausgabe_f == "Spieler Anna spielt mit X", "Die Ausgabe mit f-String ist nicht korrekt – schau nochmal in die Aufgabe"
print("Test 4.3 bestanden: Strings korrekt zusammengesetzt")
print()


# ------------------------------------------------------------
# 4.4 – input()
# ------------------------------------------------------------

# FRAGE: Was macht input()? Was gibt input() immer zurück?
# ANTWORT: ...

# FRAGE: Was ist das Problem mit dieser Zeile?
#         position = input("Wähle eine Position: ")
#         position + 1
# ANTWORT: ...

# CODE-AUFGABE A: Frage den Spieler nach seinem Namen und gib ihn aus.
#                 Ausgabe soll sein: "Willkommen, [Name]!"
#                 Entferne die # um die Aufgabe zu testen.
#                 Kommentiere sie danach wieder aus.

# name = input("Wie heißt du? ")
# print(None)   # <- ersetze None durch den richtigen f-String

# CODE-AUFGABE B: Eine Spielerin hat ihre Position als String eingegeben.
#                 Wandle den String in eine Zahl um mit int()
#                 und speichere das Ergebnis in position.

eingabe_simuliert = "5"
position = None   # <- wandle eingabe_simuliert in einen int um

print(position)
print(type(position))

# --- TEST 4.4 ---
assert position is not None,    "position ist noch leer – schau nochmal in die Aufgabe"
assert type(position) == int,   "position hat den falschen Typ – schau nochmal in die Aufgabe"
assert position == 5,           "position hat nicht den richtigen Wert – schau nochmal in die Aufgabe"
print("Test 4.4 bestanden: int() Umwandlung korrekt")
print()


# ------------------------------------------------------------
# 4.5 – Alles zusammen
# ------------------------------------------------------------

# CODE-AUFGABE: Schreibe eine Funktion spieler_info(name, zeichen)
#               die folgenden Text zurückgibt:
#               "Spieler [name] spielt mit [zeichen]"
#               Benutze einen f-String.

def spieler_info(name, zeichen):
    return None   # <- ersetze None durch den richtigen f-String

print(spieler_info("Anna", "X"))
print(spieler_info("Ben", "O"))

# --- TEST 4.5 ---
assert spieler_info("Anna", "X") == "Spieler Anna spielt mit X", "spieler_info() gibt nicht den richtigen Text zurück – schau nochmal in die Aufgabe"
assert spieler_info("Ben", "O")  == "Spieler Ben spielt mit O",  "spieler_info() gibt nicht den richtigen Text zurück – schau nochmal in die Aufgabe"
assert spieler_info("Max", "X")  == "Spieler Max spielt mit X",  "spieler_info() gibt nicht den richtigen Text zurück – schau nochmal in die Aufgabe"
print("Test 4.5 bestanden: spieler_info() funktioniert korrekt")
print()


# ------------------------------------------------------------
# Alle Tests bestanden!
# ------------------------------------------------------------
print("============================================")
print("Alle Tests in Block 4 bestanden.")
print("Du kannst mit Block 5 weitermachen.")
print("============================================")
