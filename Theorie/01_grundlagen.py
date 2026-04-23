# ============================================================
# BLOCK 1 – Grundlagen: Variablen, Typen, Listen, Funktionen
# ============================================================
# Lies jede Frage durch und schreib deine Antwort hinter # ANTWORT:
# Danach kommt direkt eine kleine Code-Aufgabe zum Ausprobieren.
# Wenn du nicht weiterkommst, frag Google oder mich.
#
# Wenn du fertig bist: Datei einmal komplett ausführen (Run).
# Du siehst dann für jede Aufgabe, ob sie korrekt ist.
# ============================================================


# ------------------------------------------------------------
# 1.1 – Was ist eine Variable?
# ------------------------------------------------------------

# FRAGE: Was ist eine Variable? Erkläre es in deinen eigenen Worten.
# ANTWORT: ...

# FRAGE: Stell dir vor, du spielst TicTacToe – was könnte man in einer
#         Variable speichern? Nenne 2 Beispiele.
# ANTWORT: ...

# CODE-AUFGABE: Erstelle zwei Variablen – deinen Namen und dein Alter.
#               Gib beide mit print() aus.

name = None       # <- deinen Namen als String eintragen, z.B. "Max"
alter = None      # <- dein Alter als Zahl eintragen, z.B. 15

print(name)
print(alter)

# --- TEST 1.1 ---
assert name is not None,   "name ist noch leer – trag deinen Namen ein"
assert type(name) == str,  "name hat den falschen Typ – schau nochmal in die Aufgabe"
assert alter is not None,  "alter ist noch leer – trag dein Alter ein"
assert type(alter) == int, "alter hat den falschen Typ – schau nochmal in die Aufgabe"
print("Test 1.1 bestanden: name =", name, "| alter =", alter)
print()


# ------------------------------------------------------------
# 1.2 – Datentypen: int, float, str, bool
# ------------------------------------------------------------

# FRAGE: Was ist ein Datentyp? Warum braucht man verschiedene Typen?
# ANTWORT: ...

# FRAGE: Ordne zu – welcher Typ passt?
#         "Hallo" -> Typ: ...
#         42        -> Typ: ...
#         3.14      -> Typ: ...
#         True      -> Typ: ...

# CODE-AUFGABE: Die Variablen sind schon gesetzt.
#               Schreib hinter jede Variable als Kommentar den Typ.
#               Führe dann die Datei aus – die Tests zeigen, ob du richtig lagst.

punkte = 100          # Typ: ___
spieler_name = "Anna" # Typ: ___
ist_gewonnen = False  # Typ: ___
temperatur = 36.5     # Typ: ___

print(type(punkte))
print(type(spieler_name))
print(type(ist_gewonnen))
print(type(temperatur))

# --- TEST 1.2 ---
assert type(punkte) == int,        "punkte hat den falschen Typ – schau nochmal in die Aufgabe"
assert type(spieler_name) == str,  "spieler_name hat den falschen Typ – schau nochmal in die Aufgabe"
assert type(ist_gewonnen) == bool, "ist_gewonnen hat den falschen Typ – schau nochmal in die Aufgabe"
assert type(temperatur) == float,  "temperatur hat den falschen Typ – schau nochmal in die Aufgabe"
print("Test 1.2 bestanden: alle Typen korrekt")
print()


# ------------------------------------------------------------
# 1.3 – Listen (Arrays)
# ------------------------------------------------------------

# FRAGE: Was ist eine Liste (auch "Array" genannt)?
#         Wofür könnte man sie beim TicTacToe-Spiel brauchen?
# ANTWORT: ...

# FRAGE: Was ist der Unterschied zwischen einer Liste und einer einzelnen Variable?
# ANTWORT: ...

# FRAGE: Listen haben Indizes – was bedeutet das?
#         Bei welchem Index fängt Python an zu zählen?
# ANTWORT: ...

# CODE-AUFGABE A: Das TicTacToe-Spielfeld hat 9 Felder.
#                 Erstelle eine Liste mit 9 leeren Feldern (" ").

spielfeld = None   # <- ersetze None durch deine Liste

# CODE-AUFGABE B: Gib das erste und das letzte Element der Liste aus.
#                 Ersetze die None-Werte durch den richtigen Index.

erstes_element = None    # <- spielfeld[?]
letztes_element = None   # <- spielfeld[?]

print(erstes_element)
print(letztes_element)

# CODE-AUFGABE C: Setze das mittlere Feld (Index 4) auf "X".

spielfeld[4] = "X"
print(spielfeld)

# --- TEST 1.3 ---
assert type(spielfeld) == list,           "spielfeld hat den falschen Typ – schau nochmal in die Aufgabe"
assert len(spielfeld) == 9,               "spielfeld hat nicht die richtige Anzahl an Feldern"
assert spielfeld[4] == "X",               "das mittlere Feld ist nicht korrekt gesetzt"
assert erstes_element == spielfeld[0],    "erstes_element ist nicht korrekt – welcher Index ist der erste?"
assert letztes_element == spielfeld[-1],  "letztes_element ist nicht korrekt – welcher Index ist der letzte?"
print("Test 1.3 bestanden: Spielfeld korrekt")
print()


# ------------------------------------------------------------
# 1.4 – Funktionen
# ------------------------------------------------------------

# FRAGE: Was ist eine Funktion? Warum benutzt man sie?
# ANTWORT: ...

# FRAGE: Was bedeutet "Parameter" bei einer Funktion?
#         Was bedeutet "return"?
# ANTWORT: ...

# CODE-AUFGABE A: Was gibt diese Funktion aus?
#                 Schreib deine Erwartung als Kommentar BEVOR du sie ausführst.

def begruesse(name):
    print("Hallo, " + name + "!")

begruesse("Anna")
# Ich erwarte: ...

# CODE-AUFGABE B: Schreibe eine Funktion berechne_summe(a, b)
#                 die zwei Zahlen addiert und das Ergebnis zurückgibt.

def berechne_summe(a, b):
    return None   # <- ersetze None durch die richtige Berechnung

ergebnis = berechne_summe(3, 7)
print(ergebnis)

# --- TEST 1.4 ---
assert berechne_summe(3, 7)  == 10, "berechne_summe(3, 7) gibt nicht das richtige Ergebnis zurück"
assert berechne_summe(0, 0)  == 0,  "berechne_summe(0, 0) gibt nicht das richtige Ergebnis zurück"
assert berechne_summe(10, 5) == 15, "berechne_summe(10, 5) gibt nicht das richtige Ergebnis zurück"
assert berechne_summe(-1, 1) == 0,  "berechne_summe(-1, 1) gibt nicht das richtige Ergebnis zurück"
print("Test 1.4 bestanden: berechne_summe() funktioniert korrekt")
print()


# ------------------------------------------------------------
# 1.5 – Klassen & Methoden
# ------------------------------------------------------------

# FRAGE: Was ist eine Klasse? Erkläre es mit einem Alltagsbeispiel
#         (z.B. Auto, Tier, Spieler...)
# ANTWORT: ...

# FRAGE: Was ist der Unterschied zwischen einer Funktion und einer Methode?
# ANTWORT: ...

# FRAGE: Was bedeutet "self" in einer Klasse?
# ANTWORT: ...

# CODE-AUFGABE: Schau dir die Klasse an und beantworte die Fragen darunter.

class Spieler:
    def __init__(self, name, zeichen):
        self.name = name
        self.zeichen = zeichen

    def vorstellen(self):
        print("Ich bin " + self.name + " und spiele mit " + self.zeichen)

spieler1 = Spieler("Anna", "X")
spieler1.vorstellen()

# FRAGE: Was ist hier die Klasse?
# ANTWORT: ...

# FRAGE: Was sind die Methoden?
# ANTWORT: ...

# FRAGE: Was passiert wenn du spieler1.vorstellen() ausführst?
# ANTWORT: ...

# BONUS: Erstelle einen zweiten Spieler "Ben" mit dem Zeichen "O"
#         und rufe vorstellen() auf.

spieler2 = None   # <- ersetze None durch den neuen Spieler

# --- TEST 1.5 ---
assert spieler1.name == "Anna",   "spieler1 hat den falschen Namen – schau nochmal in die Aufgabe"
assert spieler1.zeichen == "X",   "spieler1 hat das falsche Zeichen – schau nochmal in die Aufgabe"
assert spieler2 is not None,      "spieler2 wurde noch nicht erstellt"
assert type(spieler2) == Spieler, "spieler2 ist kein Spieler-Objekt – schau nochmal in die Aufgabe"
assert spieler2.name == "Ben",    "spieler2 hat den falschen Namen – schau nochmal in die Aufgabe"
assert spieler2.zeichen == "O",   "spieler2 hat das falsche Zeichen – schau nochmal in die Aufgabe"
print("Test 1.5 bestanden: beide Spieler korrekt erstellt")
print()


# ------------------------------------------------------------
# Alle Tests bestanden!
# ------------------------------------------------------------
print("============================================")
print("Alle Tests in Block 1 bestanden.")
print("Du kannst mit Block 2 weitermachen.")
print("============================================")
