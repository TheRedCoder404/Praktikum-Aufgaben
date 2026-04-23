# ============================================================
# BLOCK 2 – Schleifen, IDE, Terminal & Shell
# ============================================================
# Lies jede Frage durch und schreib deine Antwort hinter # ANTWORT:
# Danach kommt direkt eine kleine Code-Aufgabe zum Ausprobieren.
# Wenn du nicht weiterkommst, frag Google oder mich.
#
# Wenn du fertig bist: Datei einmal komplett ausführen (Run).
# Du siehst dann für jede Aufgabe, ob sie korrekt ist.
# ============================================================


# ------------------------------------------------------------
# 2.1 – Was ist eine Schleife?
# ------------------------------------------------------------

# FRAGE: Was ist eine Schleife? Wann benutzt man sie?
#         Erkläre in deinen eigenen Worten.
# ANTWORT: ...

# FRAGE: Was ist der Unterschied zwischen "for" und "while"?
# ANTWORT: ...

# CODE-AUFGABE A: Was gibt diese Schleife aus?
#                 Schreib die Antwort als Kommentar BEVOR du sie ausführst.

for i in range(5):
    print(i)

# Ich erwarte: ...

# --- TEST 2.1 A ---
ausgabe_a = list(range(5))
assert len(ausgabe_a) == 5,      "Die Schleife hat nicht die richtige Anzahl an Schritten"
assert ausgabe_a[0] == 0,        "Der erste Wert ist nicht korrekt – bei welcher Zahl fängt range() an?"
assert ausgabe_a[-1] == 4,       "Der letzte Wert ist nicht korrekt – schau nochmal in die Aufgabe"
print("Test 2.1 A bestanden: range(5) korrekt")
print()


# CODE-AUFGABE B: Ergänze die Schleife so, dass sie
#                 alle Elemente des Spielfelds ausgibt.

spielfeld = ["X", "O", "X",
             " ", "X", "O",
             "O", " ", "X"]

gesammelte_elemente = []

for element in spielfeld:
    print(element)
    gesammelte_elemente.append(element)

# --- TEST 2.1 B ---
assert len(gesammelte_elemente) == len(spielfeld), "Nicht alle Elemente wurden durchlaufen"
assert gesammelte_elemente == spielfeld,           "Die Elemente stimmen nicht mit dem Spielfeld überein"
print("Test 2.1 B bestanden: alle", len(gesammelte_elemente), "Elemente korrekt durchlaufen")
print()


# CODE-AUFGABE C: Schreibe eine while-Schleife die von 3 bis 1
#                 rückwärts zählt und dann "Los!" ausgibt.

zaehler = 3
zaehler_verlauf = []

while zaehler > 0:       # <- Bedingung hier anpassen falls nötig
    zaehler_verlauf.append(zaehler)
    print(zaehler)
    zaehler -= 1         # <- Zähler hier anpassen, falls nötig
print("Los!")

# --- TEST 2.1 C ---
assert len(zaehler_verlauf) == 3,  "Die Schleife hat nicht die richtige Anzahl an Schritten"
assert zaehler_verlauf[0] == 3,    "Der Countdown fängt nicht mit dem richtigen Wert an"
assert zaehler_verlauf[-1] == 1,   "Der Countdown endet nicht mit dem richtigen Wert"
assert zaehler == 0,               "Der Zähler hat nach der Schleife nicht den richtigen Wert"
print("Test 2.1 C bestanden: Countdown korrekt")
print()


# CODE-AUFGABE D: TicTacToe hat maximal 9 Runden.
#                 Schreibe eine for-Schleife, die die Runden 1-9 ausgibt.
#                 Ausgabe soll sein: "Runde 1", "Runde 2" usw.

runden_ausgabe = []

for runde in range(1, 10):   # <- range anpassen falls nötig
    print("Runde " + str(runde))
    runden_ausgabe.append("Runde " + str(runde))

# --- TEST 2.1 D ---
assert len(runden_ausgabe) == 9,         "Die Anzahl der Runden stimmt nicht"
assert runden_ausgabe[0] == "Runde 1",   "Die erste Runde hat nicht den richtigen Wert"
assert runden_ausgabe[-1] == "Runde 9",  "Die letzte Runde hat nicht den richtigen Wert"
print("Test 2.1 D bestanden: Runden korrekt ausgegeben")
print()


# ------------------------------------------------------------
# 2.2 – Was ist eine IDE?
# ------------------------------------------------------------

# FRAGE: Was bedeutet IDE? Schreib die ausgeschriebene Bedeutung hin.
# ANTWORT: ...

# FRAGE: Was kann eine IDE, was ein normaler Texteditor (z.B. Notepad) nicht kann?
#         Nenne mindestens 3 Dinge.
# ANTWORT:
#   1. ...
#   2. ...
#   3. ...

# FRAGE: Welche IDE benutzt du gerade?
# ANTWORT: ...

# FRAGE: Nenne eine andere IDE die du kennst oder gegoogelt hast.
# ANTWORT: ...


# ------------------------------------------------------------
# 2.3 – Terminal & Shell
# ------------------------------------------------------------

# FRAGE: Was ist ein Terminal? Erkläre in deinen eigenen Worten.
# ANTWORT: ...

# FRAGE: Was ist der Unterschied zwischen Terminal und Shell?
# ANTWORT: ...

# AUFGABE – Benutze das Terminal in PyCharm:
#   (unten in PyCharm auf "Terminal" klicken)
#
#   Führe diese Befehle nacheinander aus und schreib auf was passiert:
#
#   1. python --version
#      Ausgabe: ...
#
#   2. cd ..
#      Was macht das? ...
#
#   3. ls   (Mac/Linux)  ODER  dir  (Windows)
#      Was siehst du? ...
#
#   4. python 02_schleifen_ide.py
#      Was passiert? ...


# ------------------------------------------------------------
# Alle Tests bestanden!
# ------------------------------------------------------------
print("============================================")
print("Alle Tests in Block 2 bestanden.")
print("Du kannst mit Block 3 weitermachen.")
print("============================================")
