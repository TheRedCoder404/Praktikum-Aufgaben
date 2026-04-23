# ============================================================
# BLOCK 3 – Bedingungen: if, elif, else, Vergleichsoperatoren
# ============================================================
# Lies jede Frage durch und schreib deine Antwort hinter # ANTWORT:
# Danach kommt direkt eine kleine Code-Aufgabe zum Ausprobieren.
# Wenn du nicht weiterkommst, frag Google, eine KI oder mich.
#
# Wenn du fertig bist: Datei einmal komplett ausführen (Run).
# Du siehst dann für jede Aufgabe, ob sie korrekt ist.
# ============================================================


# ------------------------------------------------------------
# 3.1 – Vergleichsoperatoren
# ------------------------------------------------------------

# FRAGE: Was machen Vergleichsoperatoren? Was ist das Ergebnis eines Vergleichs?
# ANTWORT: ...

# FRAGE: Was bedeuten diese Operatoren? Schreib es als Kommentar dahinter.
#         ==    ->  ...
#         !=    ->  ...
#         >     ->  ...
#         <     ->  ...
#         >=    ->  ...
#         <=    ->  ...

# CODE-AUFGABE: Fülle die Lücken aus – was ist das Ergebnis dieser Vergleiche?
#               Ersetze jeweils None durch True oder False.
#               Führe danach die Datei aus um zu prüfen, ob du richtig lagst.

ergebnis_1 = None    # 5 == 5
ergebnis_2 = None    # 5 != 3
ergebnis_3 = None    # 10 > 20
ergebnis_4 = None    # 3 <= 3

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)
print(ergebnis_4)

# --- TEST 3.1 ---
assert ergebnis_1 is not None, "ergebnis_1 ist noch leer – trag True oder False ein"
assert ergebnis_2 is not None, "ergebnis_2 ist noch leer – trag True oder False ein"
assert ergebnis_3 is not None, "ergebnis_3 ist noch leer – trag True oder False ein"
assert ergebnis_4 is not None, "ergebnis_4 ist noch leer – trag True oder False ein"
assert ergebnis_1 == (5 == 5),   "ergebnis_1 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_2 == (5 != 3),   "ergebnis_2 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_3 == (10 > 20),  "ergebnis_3 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_4 == (3 <= 3),   "ergebnis_4 ist nicht korrekt – schau nochmal in die Aufgabe"
print("Test 3.1 bestanden: Vergleichsoperatoren korrekt")
print()


# ------------------------------------------------------------
# 3.2 – if / else
# ------------------------------------------------------------

# FRAGE: Was macht eine if-Bedingung? Erkläre in deinen eigenen Worten.
# ANTWORT: ...

# FRAGE: Wann wird der else-Block ausgeführt?
# ANTWORT: ...

# CODE-AUFGABE A: Was gibt dieser Code aus?
#                 Schreib deine Erwartung als Kommentar BEVOR du ihn ausführst.

punkte = 10

if punkte > 5:
    print("Gut gemacht!")
else:
    print("Versuch es nochmal!")

# Ich erwarte: ...

# CODE-AUFGABE B: Schreibe eine Funktion die prüft, ob ein TicTacToe-Feld frei ist.
#                 Ein freies Feld enthält" " (Leerzeichen).
#                 Gib "Feld ist frei" oder "Feld ist belegt" zurück.

def pruefe_feld(feld):
    if None:    # <- ersetze None durch die richtige Bedingung
        return "Feld ist frei"
    else:
        return "Feld ist belegt"

print(pruefe_feld(" "))
print(pruefe_feld("X"))

# --- TEST 3.2 ---
assert pruefe_feld(" ") == "Feld ist frei",   "Ein leeres Feld wird nicht korrekt erkannt – schau nochmal in die Aufgabe"
assert pruefe_feld("X") == "Feld ist belegt", "Ein belegtes Feld wird nicht korrekt erkannt – schau nochmal in die Aufgabe"
assert pruefe_feld("O") == "Feld ist belegt", "Ein belegtes Feld wird nicht korrekt erkannt – schau nochmal in die Aufgabe"
print("Test 3.2 bestanden: if/else korrekt")
print()


# ------------------------------------------------------------
# 3.3 – if / elif / else
# ------------------------------------------------------------

# FRAGE: Wofür braucht man elif? Was ist der Unterschied zu mehreren if-Blöcken?
# ANTWORT: ...

# CODE-AUFGABE A: Was gibt dieser Code aus?
#                 Schreib deine Erwartung als Kommentar BEVOR du ihn ausführst.

runde = 5

if runde == 1:
    print("Erste Runde!")
elif runde < 5:
    print("Mittendrin!")
elif runde == 5:
    print("Halbzeit!")
else:
    print("Fast fertig!")

# Ich erwarte: ...

# CODE-AUFGABE B: Schreibe eine Funktion die den Gewinner zurückgibt.
#                 Wenn gewinner "X" ist  -> "Spieler X hat gewonnen"
#                 Wenn gewinner "O" ist  -> "Spieler O hat gewonnen"
#                 Sonst                  -> "Unentschieden"

def gewinner_ausgabe(gewinner):
    if None:       # <- ersetze None durch die richtige Bedingung
        return "Spieler X hat gewonnen"
    elif None:     # <- ersetze None durch die richtige Bedingung
        return "Spieler O hat gewonnen"
    else:
        return "Unentschieden"

print(gewinner_ausgabe("X"))
print(gewinner_ausgabe("O"))
print(gewinner_ausgabe(""))

# --- TEST 3.3 ---
assert gewinner_ausgabe("X") == "Spieler X hat gewonnen", "Der Fall 'X' wird nicht korrekt behandelt – schau nochmal in die Aufgabe"
assert gewinner_ausgabe("O") == "Spieler O hat gewonnen", "Der Fall 'O' wird nicht korrekt behandelt – schau nochmal in die Aufgabe"
assert gewinner_ausgabe("")  == "Unentschieden",           "Der Fall ohne Gewinner wird nicht korrekt behandelt – schau nochmal in die Aufgabe"
print("Test 3.3 bestanden: if/elif/else korrekt")
print()


# ------------------------------------------------------------
# 3.4 – Boolean Logik: and, or, not
# ------------------------------------------------------------

# FRAGE: Was bedeuten and, or, not? Erkläre jeden Begriff kurz.
#         and  ->  ...
#         or   ->  ...
#         not  ->  ...

# CODE-AUFGABE A: Fülle die Lücken aus – was ist das Ergebnis?
#                 Ersetze jeweils None durch True oder False.

ergebnis_and_1 = None    # True and True
ergebnis_and_2 = None    # True and False
ergebnis_or_1  = None    # True or False
ergebnis_or_2  = None    # False or False
ergebnis_not_1 = None    # not True

print(ergebnis_and_1)
print(ergebnis_and_2)
print(ergebnis_or_1)
print(ergebnis_or_2)
print(ergebnis_not_1)

# CODE-AUFGABE B: Schreibe eine Funktion die prüft ob ein Zug erlaubt ist.
#                 Ein Zug ist erlaubt wenn:
#                 - Das Feld frei ist (feld == " ")
#                 - Das Spiel noch läuft (spiel_laeuft == True)
#                 Benutze "and" um beide Bedingungen zu kombinieren.

def zug_erlaubt(feld, spiel_laeuft):
    return None   # <- ersetze None durch die richtige Bedingung

print(zug_erlaubt(" ", True))
print(zug_erlaubt("X", True))
print(zug_erlaubt(" ", False))

# --- TEST 3.4 ---
assert ergebnis_and_1 is not None, "ergebnis_and_1 ist noch leer – trag True oder False ein"
assert ergebnis_and_2 is not None, "ergebnis_and_2 ist noch leer – trag True oder False ein"
assert ergebnis_or_1  is not None, "ergebnis_or_1 ist noch leer – trag True oder False ein"
assert ergebnis_or_2  is not None, "ergebnis_or_2 ist noch leer – trag True oder False ein"
assert ergebnis_not_1 is not None, "ergebnis_not_1 ist noch leer – trag True oder False ein"

assert ergebnis_and_1 == (True and True),  "ergebnis_and_1 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_and_2 == (True and False), "ergebnis_and_2 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_or_1  == (True or False),  "ergebnis_or_1 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_or_2  == (False or False), "ergebnis_or_2 ist nicht korrekt – schau nochmal in die Aufgabe"
assert ergebnis_not_1 == (not True),       "ergebnis_not_1 ist nicht korrekt – schau nochmal in die Aufgabe"

assert zug_erlaubt(" ", True)  == True,  "Der Zug sollte erlaubt sein – schau nochmal in die Aufgabe"
assert zug_erlaubt("X", True)  == False, "Der Zug sollte nicht erlaubt sein – schau nochmal in die Aufgabe"
assert zug_erlaubt(" ", False) == False, "Der Zug sollte nicht erlaubt sein – schau nochmal in die Aufgabe"
print("Test 3.4 bestanden: Boolean Logik korrekt")
print()


# ------------------------------------------------------------
# Alle Tests bestanden!
# ------------------------------------------------------------
print("============================================")
print("Alle Tests in Block 3 bestanden.")
print("Du kannst mit Block 4 weitermachen.")
print("============================================")
