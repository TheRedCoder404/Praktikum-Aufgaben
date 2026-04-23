# ============================================================
# PROJEKT – TicTacToe (MUSTERLÖSUNG)
# ============================================================
# Nur für den Betreuer – nicht an die Praktikantin weitergeben!
# ============================================================


# ============================================================
# SCHRITT 1 – Das Spielfeld erstellen
# ============================================================

spielfeld = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]


# ============================================================
# SCHRITT 2 – Das Spielfeld anzeigen
# ============================================================

def spielfeld_anzeigen(feld):
    print(f" {feld[0]} | {feld[1]} | {feld[2]} ")
    print("---+---+---")
    print(f" {feld[3]} | {feld[4]} | {feld[5]} ")
    print("---+---+---")
    print(f" {feld[6]} | {feld[7]} | {feld[8]} ")

spielfeld_anzeigen(spielfeld)
print()


# ============================================================
# SCHRITT 3 – Einen Zug machen
# ============================================================

def zug_machen(feld, position, zeichen):
    index = position - 1

    if feld[index] == " ":
        feld[index] = zeichen
    else:
        print("Dieses Feld ist schon belegt!")

zug_machen(spielfeld, 5, "X")
spielfeld_anzeigen(spielfeld)
print()


# ============================================================
# SCHRITT 4 – Spieler wechseln
# ============================================================

def spieler_wechseln(aktueller_spieler):
    if aktueller_spieler == "X":
        return "O"
    else:
        return "X"

print(spieler_wechseln("X"))
print(spieler_wechseln("O"))
print()


# ============================================================
# SCHRITT 5 – Gewinner prüfen
# ============================================================

def hat_gewonnen(feld, zeichen):
    kombinationen = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for kombi in kombinationen:
        if feld[kombi[0]] == zeichen and feld[kombi[1]] == zeichen and feld[kombi[2]] == zeichen:
            return True

    return False

print(hat_gewonnen(spielfeld, "X"))

zug_machen(spielfeld, 4, "X")
zug_machen(spielfeld, 6, "X")
spielfeld_anzeigen(spielfeld)

print(hat_gewonnen(spielfeld, "X"))
print()

spielfeld = [" "] * 9


# ============================================================
# SCHRITT 6 – Unentschieden prüfen
# ============================================================

def ist_unentschieden(feld):
    for einzelfeld in feld:
        if einzelfeld == " ":
            return False
    return True

print(ist_unentschieden(spielfeld))

spielfeld = ["X", "O", "X",
             "O", "X", "O",
             "O", "X", "O"]

print(ist_unentschieden(spielfeld))
print()

spielfeld = [" "] * 9


# ============================================================
# SCHRITT 7 – Hauptschleife
# ============================================================

aktueller_spieler = "X"

print("Willkommen zu TicTacToe!")
print("Spieler X beginnt.")
print()

while True:
    spielfeld_anzeigen(spielfeld)
    print()

    eingabe = input(f"Spieler {aktueller_spieler}, wähle eine Position (1-9): ")
    position = int(eingabe)

    zug_machen(spielfeld, position, aktueller_spieler)

    if hat_gewonnen(spielfeld, aktueller_spieler):
        spielfeld_anzeigen(spielfeld)
        print(f"Spieler {aktueller_spieler} hat gewonnen!")
        break

    if ist_unentschieden(spielfeld):
        spielfeld_anzeigen(spielfeld)
        print("Unentschieden!")
        break

    aktueller_spieler = spieler_wechseln(aktueller_spieler)
