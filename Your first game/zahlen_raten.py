# ============================================================
# PROJEKT – Zahlen raten
# ============================================================
# Du baust jetzt Schritt für Schritt ein Zahlen-Raten-Spiel.
# Lies jeden Schritt durch, fülle die TODOs aus und führe die
# Datei danach aus um zu sehen ob es funktioniert.
#
# Wenn du nicht weiterkommst, schau in deine alten Blöcke
# oder frag Google, eine KI oder mich.
# ============================================================
#
# So soll das Spiel am Ende aussehen:
#
#   Willkommen zu Zahlen raten!
#   Ich habe mir eine Zahl zwischen 1 und 100 gedacht.
#
#   Dein Tipp: 50
#   Zu hoch! Versuch es nochmal.
#
#   Dein Tipp: 25
#   Zu niedrig! Versuch es nochmal.
#
#   Dein Tipp: 37
#   Richtig! Du hast die Zahl in 3 Versuchen erraten!
#
# ============================================================


import random


# ============================================================
# SCHRITT 1 – Eine zufällige Zahl erstellen
# ============================================================
# Wir benutzen das "random" Modul um eine zufällige Zahl
# zwischen 1 und 100 zu erstellen.
# random.randint(1, 100) gibt eine zufällige Zahl zurück.
# ============================================================

# TODO: Erstelle eine zufällige Zahl zwischen 1 und 100.
#       Speichere sie in der Variable "geheimzahl".

geheimzahl = None   # <- ersetze None durch den richtigen Aufruf

# Teste es – führe die Datei aus.
# Jedes Mal sollte eine andere Zahl ausgegeben werden.
print("Geheimzahl (nur zum Testen):", geheimzahl)
print()


# ============================================================
# SCHRITT 2 – Tipp des Spielers einlesen
# ============================================================
# Der Spieler gibt eine Zahl ein.
# Wir lesen sie mit input() ein und wandeln sie in einen int um.
# ============================================================

# TODO: Schreibe eine Funktion "tipp_einlesen()".
#       Sie fragt den Spieler nach einem Tipp mit input().
#       Sie wandelt die Eingabe in einen int um und gibt ihn zurück.
#       Tipp: Das hast du in Block 4 gelernt!

def tipp_einlesen():
    eingabe = input(None)   # <- ersetze None durch den richtigen Text
    return None             # <- wandle eingabe in einen int um und gib ihn zurück

# Teste es – führe die Datei aus und gib eine Zahl ein.
# Die Ausgabe sollte deine Zahl als int sein.
tipp = tipp_einlesen()
print("Dein Tipp:", tipp)
print("Typ:", type(tipp))
print()


# ============================================================
# SCHRITT 3 – Tipp überprüfen
# ============================================================
# Wir vergleichen den Tipp des Spielers mit der Geheimzahl.
# Es gibt drei Möglichkeiten:
#   - Tipp ist zu hoch   -> "Zu hoch! Versuch es nochmal."
#   - Tipp ist zu niedrig -> "Zu niedrig! Versuch es nochmal."
#   - Tipp ist richtig   -> "Richtig!"
# ============================================================

# TODO: Schreibe eine Funktion "tipp_pruefen(tipp, geheimzahl)".
#       Sie bekommt den Tipp und die Geheimzahl als Parameter.
#       Sie gibt "zu hoch", "zu niedrig" oder "richtig" zurück.
#       Tipp: Benutze if/elif/else – das hast du in Block 3 gelernt!

def tipp_pruefen(tipp, geheimzahl):
    if None:        # <- zu hoch
        return "zu hoch"
    elif None:      # <- zu niedrig
        return "zu niedrig"
    else:
        return "richtig"

# Teste es – führe die Datei aus.
# Die Ausgaben sollten "zu hoch", "zu niedrig" und "richtig" sein.
print(tipp_pruefen(80, 50))
print(tipp_pruefen(20, 50))
print(tipp_pruefen(50, 50))
print()


# ============================================================
# SCHRITT 4 – Versuche zählen
# ============================================================
# Wir zählen wie viele Versuche der Spieler gebraucht hat.
# Nach jedem Tipp erhöhen wir den Zähler um 1.
# ============================================================

# TODO: Erstelle eine Variable "versuche" und setze sie auf 0.
#       Schreibe dann eine Funktion "versuch_hinzufuegen(versuche)"
#       die versuche um 1 erhöht und zurückgibt.

versuche = None   # <- setze versuche auf 0

def versuch_hinzufuegen(versuche):
    return None   # <- erhöhe versuche um 1 und gib den neuen Wert zurück

# Teste es – führe die Datei aus.
# Die Ausgaben sollten 1, 2 und 3 sein.
versuche = versuch_hinzufuegen(versuche)
print(versuche)
versuche = versuch_hinzufuegen(versuche)
print(versuche)
versuche = versuch_hinzufuegen(versuche)
print(versuche)
print()

# Versuche zurücksetzen für den nächsten Schritt
versuche = 0


# ============================================================
# SCHRITT 5 – Nachricht ausgeben
# ============================================================
# Nach jedem Tipp geben wir eine passende Nachricht aus.
# Am Ende sagen wir dem Spieler wie viele Versuche er gebraucht hat.
# ============================================================

# TODO: Schreibe eine Funktion "nachricht_ausgeben(ergebnis, versuche)".
#       Sie bekommt das Ergebnis ("zu hoch", "zu niedrig", "richtig")
#       und die Anzahl der Versuche.
#       Wenn ergebnis "zu hoch" ist    -> "Zu hoch! Versuch es nochmal."
#       Wenn ergebnis "zu niedrig" ist -> "Zu niedrig! Versuch es nochmal."
#       Wenn ergebnis "richtig" ist    -> "Richtig! Du hast die Zahl in
#                                         [versuche] Versuchen erraten!"
#       Tipp: Benutze if/elif/else und f-Strings.

def nachricht_ausgeben(ergebnis, versuche):
    if None:        # <- zu hoch
        print(None)
    elif None:      # <- zu niedrig
        print(None)
    else:
        print(None)

# Teste es – führe die Datei aus.
# Die Ausgaben sollten die richtigen Nachrichten sein.
nachricht_ausgeben("zu hoch", 3)
nachricht_ausgeben("zu niedrig", 3)
nachricht_ausgeben("richtig", 3)
print()


# ============================================================
# SCHRITT 6 – Hauptschleife
# ============================================================
# Jetzt bauen wir alles zusammen!
# Die Hauptschleife läuft solange bis der Spieler die Zahl erraten hat.
# ============================================================

# TODO: Fülle die Lücken in der Hauptschleife aus.

geheimzahl = random.randint(1, 100)
versuche = 0

print("Willkommen zu Zahlen raten!")
print("Ich habe mir eine Zahl zwischen 1 und 100 gedacht.")
print()

while True:
    # TODO: Tipp einlesen
    tipp = None   # <- ersetze None durch den richtigen Funktionsaufruf

    # TODO: Versuche erhöhen
    versuche = None   # <- ersetze None durch den richtigen Funktionsaufruf

    # TODO: Tipp prüfen
    ergebnis = None   # <- ersetze None durch den richtigen Funktionsaufruf

    # TODO: Nachricht ausgeben
    None   # <- ersetze None durch den richtigen Funktionsaufruf
    print()

    # TODO: Prüfe ob der Spieler gewonnen hat und beende die Schleife
    if None:   # <- ersetze None durch die richtige Bedingung
        break
