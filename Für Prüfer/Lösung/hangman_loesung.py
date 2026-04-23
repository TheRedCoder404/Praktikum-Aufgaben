# ============================================================
# PROJEKT – Hangman (MUSTERLÖSUNG)
# ============================================================
# Nur für den Betreuer – nicht an die Praktikantin weitergeben!
# ============================================================


import random


woerter = ["python", "schleife", "variable", "funktion",
           "liste", "klasse", "methode", "tastatur"]


# ============================================================
# SCHRITT 1 – Ein zufälliges Wort auswählen
# ============================================================

geheimwort = random.choice(woerter)

print("Geheimwort (nur zum Testen):", geheimwort)
print()


# ============================================================
# SCHRITT 2 – Wort als Liste von Buchstaben anzeigen
# ============================================================

def wort_anzeigen(wort, erratene_buchstaben):
    anzeige = []

    for buchstabe in wort:
        if buchstabe in erratene_buchstaben:
            anzeige.append(buchstabe)
        else:
            anzeige.append("_")

    print("Wort:   ", " ".join(anzeige))

wort_anzeigen("python", [])
wort_anzeigen("python", ["p", "n"])
print()


# ============================================================
# SCHRITT 3 – Buchstabe einlesen
# ============================================================

def buchstabe_einlesen():
    eingabe = input("Dein Buchstabe: ")
    return eingabe.lower()

buchstabe = buchstabe_einlesen()
print("Dein Buchstabe:", buchstabe)
print()


# ============================================================
# SCHRITT 4 – Buchstaben prüfen
# ============================================================

def buchstabe_pruefen(buchstabe, wort):
    return buchstabe in wort

print(buchstabe_pruefen("p", "python"))
print(buchstabe_pruefen("x", "python"))
print()


# ============================================================
# SCHRITT 5 – Spielstatus prüfen
# ============================================================

def hat_gewonnen(wort, erratene_buchstaben):
    for buchstabe in wort:
        if buchstabe not in erratene_buchstaben:
            return False
    return True

print(hat_gewonnen("python", ["p", "y", "t", "h", "o"]))
print(hat_gewonnen("python", ["p", "y", "t", "h", "o", "n"]))
print()


# ============================================================
# SCHRITT 6 – Hauptschleife
# ============================================================

geheimwort           = random.choice(woerter)
erratene_buchstaben  = []
falsche_buchstaben   = []
versuche             = 6

print("Willkommen zu Hangman!")
print(f"Das Wort hat {len(geheimwort)} Buchstaben.")
print()

while True:
    wort_anzeigen(geheimwort, erratene_buchstaben)
    print("Falsche Buchstaben:", falsche_buchstaben)
    print("Versuche noch:", versuche)
    print()

    buchstabe = buchstabe_einlesen()

    if buchstabe_pruefen(buchstabe, geheimwort):
        print(f'"{buchstabe}" ist im Wort!')
        erratene_buchstaben.append(buchstabe)
    else:
        print(f'"{buchstabe}" ist nicht im Wort!')
        falsche_buchstaben.append(buchstabe)
        versuche -= 1
    print()

    if hat_gewonnen(geheimwort, erratene_buchstaben):
        wort_anzeigen(geheimwort, erratene_buchstaben)
        print("Glückwunsch! Du hast das Wort erraten!")
        break

    if versuche == 0:
        print(f"Leider verloren! Das Wort war: {geheimwort}")
        break
