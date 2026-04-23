# ============================================================
# PROJEKT – Zahlen raten (MUSTERLÖSUNG)
# ============================================================
# Nur für den Betreuer – nicht an die Praktikantin weitergeben!
# ============================================================


import random


# ============================================================
# SCHRITT 1 – Eine zufällige Zahl erstellen
# ============================================================

geheimzahl = random.randint(1, 100)

print("Geheimzahl (nur zum Testen):", geheimzahl)
print()


# ============================================================
# SCHRITT 2 – Tipp des Spielers einlesen
# ============================================================

def tipp_einlesen():
    eingabe = input("Dein Tipp: ")
    return int(eingabe)

tipp = tipp_einlesen()
print("Dein Tipp:", tipp)
print("Typ:", type(tipp))
print()


# ============================================================
# SCHRITT 3 – Tipp überprüfen
# ============================================================

def tipp_pruefen(tipp, geheimzahl):
    if tipp > geheimzahl:
        return "zu hoch"
    elif tipp < geheimzahl:
        return "zu niedrig"
    else:
        return "richtig"

print(tipp_pruefen(80, 50))
print(tipp_pruefen(20, 50))
print(tipp_pruefen(50, 50))
print()


# ============================================================
# SCHRITT 4 – Versuche zählen
# ============================================================

versuche = 0

def versuch_hinzufuegen(versuche):
    return versuche + 1

versuche = versuch_hinzufuegen(versuche)
print(versuche)
versuche = versuch_hinzufuegen(versuche)
print(versuche)
versuche = versuch_hinzufuegen(versuche)
print(versuche)
print()

versuche = 0


# ============================================================
# SCHRITT 5 – Nachricht ausgeben
# ============================================================

def nachricht_ausgeben(ergebnis, versuche):
    if ergebnis == "zu hoch":
        print("Zu hoch! Versuch es nochmal.")
    elif ergebnis == "zu niedrig":
        print("Zu niedrig! Versuch es nochmal.")
    else:
        print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten!")

nachricht_ausgeben("zu hoch", 3)
nachricht_ausgeben("zu niedrig", 3)
nachricht_ausgeben("richtig", 3)
print()


# ============================================================
# SCHRITT 6 – Hauptschleife
# ============================================================

geheimzahl = random.randint(1, 100)
versuche = 0

print("Willkommen zu Zahlen raten!")
print("Ich habe mir eine Zahl zwischen 1 und 100 gedacht.")
print()

while True:
    tipp = tipp_einlesen()
    versuche = versuch_hinzufuegen(versuche)
    ergebnis = tipp_pruefen(tipp, geheimzahl)
    nachricht_ausgeben(ergebnis, versuche)
    print()

    if ergebnis == "richtig":
        break
