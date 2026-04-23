# ============================================================
# PROJEKT – TicTacToe
# ============================================================
# Du baust jetzt Schritt für Schritt ein echtes TicTacToe-Spiel.
# Lies jeden Schritt durch, fülle die TODOs aus und führe die
# Datei danach aus um zu sehen ob es funktioniert.
#
# Wenn du nicht weiterkommst, schau in deine alten Blöcke
# oder frag Google, eine KI oder mich.
# ============================================================


# ============================================================
# SCHRITT 1 – Das Spielfeld erstellen
# ============================================================
# Das Spielfeld hat 9 Felder – wir speichern es als Liste.
# Jedes Feld ist am Anfang leer, also " " (Leerzeichen).
# Die Felder sind nummeriert von 1 bis 9 – so wählt der Spieler
# später seine Position.
#
# So soll das Spielfeld aussehen:
#
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9
#
# ============================================================

# TODO: Erstelle eine Liste mit 9 leeren Feldern (" ").
#       Nenne sie "spielfeld".
#       Tipp: Du hast das schon in Block 1 gemacht!

spielfeld = None   # <- ersetze None durch deine Liste

# ============================================================
# SCHRITT 2 – Das Spielfeld anzeigen
# ============================================================
# Wir brauchen eine Funktion die das Spielfeld ausgibt.
# So soll die Ausgabe aussehen:
#
#  X | O | X
# ---+---+---
#    | X | O
# ---+---+---
#  O |   | X
#
# ============================================================

# TODO: Schreibe eine Funktion "spielfeld_anzeigen(feld)".
#       Sie bekommt das Spielfeld als Parameter.
#       Sie gibt das Spielfeld in 3 Zeilen aus.
#       Tipp: Benutze print() und f-Strings.
#       Tipp: feld[0] ist das erste Feld, feld[1] das zweite usw.

def spielfeld_anzeigen(feld):
    print(f" {feld[0]} | {feld[1]} | {feld[2]} ")
    print("---+---+---")
    # TODO: Gib die zweite Zeile aus (feld[3], feld[4], feld[5])
    print(None)
    print("---+---+---")
    # TODO: Gib die dritte Zeile aus (feld[6], feld[7], feld[8])
    print(None)

# Teste es – führe die Datei aus. Du solltest ein leeres Spielfeld sehen.
spielfeld_anzeigen(spielfeld)
print()


# ============================================================
# SCHRITT 3 – Einen Zug machen
# ============================================================
# Der Spieler gibt eine Zahl zwischen 1 und 9 ein.
# Wir setzen dann sein Zeichen ("X" oder "O") auf das Feld.
#
# Wichtig: Der Spieler gibt 1-9 ein, aber Listen starten bei 0.
#           Position 1 ist also Index 0, Position 2 ist Index 1 usw.
#           Tipp: index = position - 1
#
# Außerdem: Wir dürfen nur auf ein freies Feld setzen!
# ============================================================

# TODO: Schreibe eine Funktion "zug_machen(feld, position, zeichen)".
#       Sie bekommt das Spielfeld, die gewählte Position (1-9)
#       und das Zeichen ("X" oder "O").
#       Wenn das Feld frei ist (" "), setze das Zeichen.
#       Wenn das Feld belegt ist, gib "Dieses Feld ist schon belegt!" aus.

def zug_machen(feld, position, zeichen):
    index = position - 1   # <- wandelt Position 1-9 in Index 0-8 um

    # TODO: Prüfe ob das Feld frei ist
    if None:                # <- ersetze None durch die richtige Bedingung
        feld[index] = None  # <- ersetze None durch das richtige Zeichen
    else:
        print("Dieses Feld ist schon belegt!")

# Teste es – führe die Datei aus.
# Das mittlere Feld (Position 5) sollte jetzt ein X haben.
zug_machen(spielfeld, 5, "X")
spielfeld_anzeigen(spielfeld)
print()


# ============================================================
# SCHRITT 4 – Spieler wechseln
# ============================================================
# Nach jedem Zug wechselt der aktive Spieler.
# Wenn "X" dran war, kommt "O" – und umgekehrt.
# ============================================================

# TODO: Schreibe eine Funktion "spieler_wechseln(aktueller_spieler)".
#       Wenn aktueller_spieler "X" ist, gib "O" zurück.
#       Wenn aktueller_spieler "O" ist, gib "X" zurück.
#       Tipp: Benutze if/else.

def spieler_wechseln(aktueller_spieler):
    if None:    # <- ersetze None durch die richtige Bedingung
        return None
    else:
        return None

# Teste es – führe die Datei aus.
# Die Ausgabe sollte "O" und dann "X" sein.
print(spieler_wechseln("X"))
print(spieler_wechseln("O"))
print()


# ============================================================
# SCHRITT 5 – Gewinner prüfen
# ============================================================
# Nach jedem Zug prüfen wir ob jemand gewonnen hat.
# Es gibt 8 mögliche Gewinnkombinationen:
#   - 3 Zeilen:    [0,1,2], [3,4,5], [6,7,8]
#   - 3 Spalten:   [0,3,6], [1,4,7], [2,5,8]
#   - 2 Diagonalen:[0,4,8], [2,4,6]
#
# Ein Spieler hat gewonnen wenn alle 3 Felder einer Kombination
# sein Zeichen enthalten.
# ============================================================

# TODO: Schreibe eine Funktion "hat_gewonnen(feld, zeichen)".
#       Sie bekommt das Spielfeld und ein Zeichen ("X" oder "O").
#       Prüfe alle 8 Kombinationen.
#       Gib True zurück wenn der Spieler gewonnen hat, sonst False.

def hat_gewonnen(feld, zeichen):
    kombinationen = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for kombi in kombinationen:
        # TODO: Prüfe ob alle 3 Felder der Kombination das Zeichen enthalten.
        #       Tipp: feld[kombi[0]], feld[kombi[1]], feld[kombi[2]]
        if None:   # <- ersetze None durch die richtige Bedingung
            return True

    return False

# Teste es – führe die Datei aus.
# Die erste Ausgabe sollte False sein (noch kein Gewinner).
print(hat_gewonnen(spielfeld, "X"))

# Setze noch zwei X um eine Reihe zu vervollständigen
zug_machen(spielfeld, 4, "X")
zug_machen(spielfeld, 6, "X")
spielfeld_anzeigen(spielfeld)

# Jetzt sollte True ausgegeben werden
print(hat_gewonnen(spielfeld, "X"))
print()

# Spielfeld zurücksetzen für den nächsten Schritt
spielfeld = [" "] * 9


# ============================================================
# SCHRITT 6 – Unentschieden prüfen
# ============================================================
# Wenn alle 9 Felder belegt sind und niemand gewonnen hat,
# ist es Unentschieden.
# ============================================================

# TODO: Schreibe eine Funktion "ist_unentschieden(feld)".
#       Sie gibt True zurück wenn kein Feld mehr leer ist (" ").
#       Tipp: Benutze eine for-Schleife und prüfe jedes Feld.

def ist_unentschieden(feld):
    for einzelfeld in feld:
        # TODO: Wenn noch ein Feld leer ist, gib False zurück
        if None:   # <- ersetze None durch die richtige Bedingung
            return False
    return True

# Teste es – führe die Datei aus.
# Die erste Ausgabe sollte False sein (Spielfeld ist leer).
print(ist_unentschieden(spielfeld))

# Fülle alle Felder – kein Gewinner
spielfeld = ["X", "O", "X",
             "O", "X", "O",
             "O", "X", "O"]

# Jetzt sollte True ausgegeben werden
print(ist_unentschieden(spielfeld))
print()

# Spielfeld zurücksetzen
spielfeld = [" "] * 9


# ============================================================
# SCHRITT 7 – Hauptschleife
# ============================================================
# Jetzt bauen wir alles zusammen!
# Die Hauptschleife läuft solange bis jemand gewonnen hat
# oder es Unentschieden ist.
# ============================================================

# TODO: Fülle die Lücken in der Hauptschleife aus.

aktueller_spieler = "X"

print("Willkommen zu TicTacToe!")
print("Spieler X beginnt.")
print()

while True:
    # Spielfeld anzeigen
    spielfeld_anzeigen(spielfeld)
    print()

    # TODO: Frage den aktuellen Spieler nach seiner Position.
    #       Tipp: Benutze input() und int() – das hast du in Block 4 gelernt!
    eingabe = input(None)   # <- ersetze None durch den richtigen Text
    position = None         # <- wandle eingabe in einen int um

    # TODO: Zug machen
    zug_machen(None, None, None)   # <- fülle die richtigen Parameter ein

    # TODO: Prüfe ob der aktuelle Spieler gewonnen hat
    if None:   # <- ersetze None durch den richtigen Funktionsaufruf
        spielfeld_anzeigen(spielfeld)
        print(f"Spieler {aktueller_spieler} hat gewonnen!")
        break

    # TODO: Prüfe ob es Unentschieden ist
    if None:   # <- ersetze None durch den richtigen Funktionsaufruf
        spielfeld_anzeigen(spielfeld)
        print("Unentschieden!")
        break

    # TODO: Spieler wechseln
    aktueller_spieler = None   # <- ersetze None durch den richtigen Funktionsaufruf
