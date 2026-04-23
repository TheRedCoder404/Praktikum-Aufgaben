# ============================================================
# PROJEKT – Hangman
# ============================================================
# Du baust jetzt Schritt für Schritt ein Hangman-Spiel.
# Lies jeden Schritt durch, fülle die TODOs aus und führe die
# Datei danach aus um zu sehen ob es funktioniert.
#
# Wenn du nicht weiterkommst, schau in deine alten Blöcke
# oder frag Google, eine KI oder mich.
# ============================================================
#
# So soll das Spiel am Ende aussehen:
#
#   Willkommen zu Hangman!
#   Das Wort hat 6 Buchstaben.
#
#   Wort:    _ _ _ _ _ _
#   Falsche Buchstaben: []
#   Versuche noch: 6
#
#   Dein Buchstabe: p
#   "p" ist im Wort!
#
#   Wort:    _ _ _ _ _ p
#   Falsche Buchstaben: []
#   Versuche noch: 6
#
#   Dein Buchstabe: x
#   "x" ist nicht im Wort!
#
#   Wort:    _ _ _ _ _ p
#   Falsche Buchstaben: ['x']
#   Versuche noch: 5
#
# ============================================================


import random


# ============================================================
# SCHRITT 1 – Ein zufälliges Wort auswählen
# ============================================================
# Wir haben eine Liste von Wörtern.
# Mit random.choice() wählen wir ein zufälliges Wort aus.
# ============================================================

woerter = ["python", "schleife", "variable", "funktion",
           "liste", "klasse", "methode", "tastatur"]

# TODO: Wähle ein zufälliges Wort aus der Liste "woerter".
#       Speichere es in der Variable "geheimwort".
#       Tipp: random.choice(liste) gibt ein zufälliges Element zurück.

geheimwort = None   # <- ersetze None durch den richtigen Aufruf

# Teste es – jedes Mal sollte ein anderes Wort ausgegeben werden.
print("Geheimwort (nur zum Testen):", geheimwort)
print()


# ============================================================
# SCHRITT 2 – Wort als Liste von Buchstaben anzeigen
# ============================================================
# Wir zeigen das Wort als Liste von "_" an.
# Für jeden bereits erratenen Buchstaben zeigen wir den Buchstaben.
#
# Beispiel: Wort "python", erratene Buchstaben ["p", "n"]
#           Ausgabe: p _ _ _ _ n
# ============================================================

# TODO: Schreibe eine Funktion "wort_anzeigen(wort, erratene_buchstaben)".
#       Sie bekommt das Geheimwort und eine Liste der erratenen Buchstaben.
#       Für jeden Buchstaben im Wort:
#           - Wenn er in erratene_buchstaben ist -> zeige den Buchstaben
#           - Sonst -> zeige "_"
#       Gib alle Zeichen mit Leerzeichen dazwischen aus.
#       Tipp: Benutze eine for-Schleife und eine Liste zum Sammeln.

def wort_anzeigen(wort, erratene_buchstaben):
    anzeige = []

    for buchstabe in wort:
        if None:   # <- ersetze None durch die richtige Bedingung
            anzeige.append(buchstabe)
        else:
            anzeige.append("_")

    print("Wort:   ", " ".join(anzeige))

# Teste es – führe die Datei aus.
# Erste Ausgabe:  _ _ _ _ _ _
# Zweite Ausgabe: p _ _ _ _ n
wort_anzeigen("python", [])
wort_anzeigen("python", ["p", "n"])
print()


# ============================================================
# SCHRITT 3 – Buchstabe einlesen
# ============================================================
# Der Spieler gibt einen Buchstaben ein.
# Wir lesen ihn mit input() ein und machen ihn klein mit .lower().
# ============================================================

# TODO: Schreibe eine Funktion "buchstabe_einlesen()".
#       Sie fragt den Spieler nach einem Buchstaben mit input().
#       Sie gibt den Buchstaben in Kleinbuchstaben zurück.
#       Tipp: .lower() macht einen String klein – das hast du in Block 4 gelernt!

def buchstabe_einlesen():
    eingabe = input(None)   # <- ersetze None durch den richtigen Text
    return None             # <- gib die Eingabe in Kleinbuchstaben zurück

# Teste es – führe die Datei aus und gib einen Buchstaben ein.
# Die Ausgabe sollte der Buchstabe in Kleinbuchstaben sein.
buchstabe = buchstabe_einlesen()
print("Dein Buchstabe:", buchstabe)
print()


# ============================================================
# SCHRITT 4 – Buchstaben prüfen
# ============================================================
# Wir prüfen ob der eingegebene Buchstabe im Geheimwort vorkommt.
# ============================================================

# TODO: Schreibe eine Funktion "buchstabe_pruefen(buchstabe, wort)".
#       Sie bekommt den eingegebenen Buchstaben und das Geheimwort.
#       Wenn der Buchstabe im Wort ist -> gib True zurück.
#       Wenn der Buchstabe nicht im Wort ist -> gib False zurück.
#       Tipp: Benutze "in" um zu prüfen ob ein Buchstabe in einem String ist.
#             Beispiel: "p" in "python" -> True

def buchstabe_pruefen(buchstabe, wort):
    return None   # <- ersetze None durch die richtige Bedingung

# Teste es – führe die Datei aus.
# Erste Ausgabe:  True
# Zweite Ausgabe: False
print(buchstabe_pruefen("p", "python"))
print(buchstabe_pruefen("x", "python"))
print()


# ============================================================
# SCHRITT 5 – Spielstatus prüfen
# ============================================================
# Nach jedem Zug prüfen wir ob der Spieler gewonnen oder verloren hat.
#
# Gewonnen: Alle Buchstaben des Wortes wurden erraten.
# Verloren: Der Spieler hat keine Versuche mehr (versuche == 0).
# ============================================================

# TODO: Schreibe eine Funktion "hat_gewonnen(wort, erratene_buchstaben)".
#       Sie gibt True zurück wenn alle Buchstaben des Wortes
#       in erratene_buchstaben sind.
#       Tipp: Benutze eine for-Schleife und prüfe jeden Buchstaben.

def hat_gewonnen(wort, erratene_buchstaben):
    for buchstabe in wort:
        if None:   # <- ersetze None durch die richtige Bedingung
            return False
    return True

# Teste es – führe die Datei aus.
# Erste Ausgabe:  False
# Zweite Ausgabe: True
print(hat_gewonnen("python", ["p", "y", "t", "h", "o"]))
print(hat_gewonnen("python", ["p", "y", "t", "h", "o", "n"]))
print()


# ============================================================
# SCHRITT 6 – Hauptschleife
# ============================================================
# Jetzt bauen wir alles zusammen!
# Die Hauptschleife läuft solange bis der Spieler gewonnen
# oder alle Versuche aufgebraucht hat.
# ============================================================

geheimwort       = random.choice(woerter)
erratene_buchstaben  = []
falsche_buchstaben   = []
versuche         = 6

print("Willkommen zu Hangman!")
print(f"Das Wort hat {len(geheimwort)} Buchstaben.")
print()

while True:
    # Spielstand anzeigen
    # TODO: Zeige das Wort an
    None   # <- ersetze None durch den richtigen Funktionsaufruf

    print("Falsche Buchstaben:", falsche_buchstaben)
    print("Versuche noch:", versuche)
    print()

    # Buchstabe einlesen
    # TODO: Lies einen Buchstaben ein
    buchstabe = None   # <- ersetze None durch den richtigen Funktionsaufruf

    # Buchstabe prüfen
    # TODO: Prüfe ob der Buchstabe im Wort ist
    if None:   # <- ersetze None durch den richtigen Funktionsaufruf
        print(f'"{buchstabe}" ist im Wort!')
        # TODO: Füge den Buchstaben zu erratene_buchstaben hinzu
        None   # <- ersetze None durch den richtigen Aufruf
    else:
        print(f'"{buchstabe}" ist nicht im Wort!')
        # TODO: Füge den Buchstaben zu falsche_buchstaben hinzu
        None   # <- ersetze None durch den richtigen Aufruf
        # TODO: Verringere versuche um 1
        versuche = None   # <- ersetze None durch die richtige Berechnung
    print()

    # Gewonnen?
    # TODO: Prüfe ob der Spieler gewonnen hat
    if None:   # <- ersetze None durch den richtigen Funktionsaufruf
        wort_anzeigen(geheimwort, erratene_buchstaben)
        print("Glückwunsch! Du hast das Wort erraten!")
        break

    # Verloren?
    # TODO: Prüfe ob der Spieler keine Versuche mehr hat
    if None:   # <- ersetze None durch die richtige Bedingung
        print(f"Leider verloren! Das Wort war: {geheimwort}")
        break
