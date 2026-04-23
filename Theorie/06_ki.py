# ============================================================
# BLOCK 6 – Künstliche Intelligenz (KI)
# ============================================================
# Lies jede Frage durch und schreib deine Antwort hinter # ANTWORT:
# In diesem Block wirst du eine KI auch selbst ausprobieren.
# Benutze z.B. ChatGPT oder Claude: https://claude.ai
#
# Wenn du fertig bist: Datei einmal komplett ausführen (Run).
# Du siehst dann ob du alle Felder ausgefüllt hast.
# ============================================================


# ------------------------------------------------------------
# 6.1 – Was ist KI?
# ------------------------------------------------------------

# FRAGE: Was ist Künstliche Intelligenz?
#         Erkläre es so, als würdest du es einem 10-Jährigen erklären.
# ANTWORT: ...

# FRAGE: Wo begegnest du KI in deinem Alltag?
#         Nenne mindestens 3 Beispiele – trag sie hier als Variablen ein:

ki_beispiel_1 = "..."
ki_beispiel_2 = "..."
ki_beispiel_3 = "..."

# --- TEST 6.1 ---
assert ki_beispiel_1 != "...", "ki_beispiel_1 ist noch leer – trag ein Beispiel ein"
assert ki_beispiel_2 != "...", "ki_beispiel_2 ist noch leer – trag ein Beispiel ein"
assert ki_beispiel_3 != "...", "ki_beispiel_3 ist noch leer – trag ein Beispiel ein"
assert len(ki_beispiel_1) > 0, "ki_beispiel_1 ist noch leer – schau nochmal in die Aufgabe"
assert len(ki_beispiel_2) > 0, "ki_beispiel_2 ist noch leer – schau nochmal in die Aufgabe"
assert len(ki_beispiel_3) > 0, "ki_beispiel_3 ist noch leer – schau nochmal in die Aufgabe"
print("Test 6.1 bestanden: KI-Beispiele aus dem Alltag:")
print(" -", ki_beispiel_1)
print(" -", ki_beispiel_2)
print(" -", ki_beispiel_3)
print()


# ------------------------------------------------------------
# 6.2 – KI & Programmieren
# ------------------------------------------------------------

# AUFGABE: Öffne eine KI (z.B. https://claude.ai)
#           Stelle ihr diese Frage:
#           "Erkläre mir, was eine for-Schleife in Python ist.
#            Ich bin Anfängerin und 15 Jahre alt."

# FRAGE: War die Erklärung verständlich? Was war gut, was war unklar?
# ANTWORT: ...

# AUFGABE: Stelle der KI jetzt diese Frage:
#           "Schreib mir eine Python-Funktion die zwei Zahlen addiert"
#
#           Kopiere den Code den die KI dir gibt hier rein
#           und ersetze das "pass" – dann wird er automatisch getestet.

# Code von der KI: (hier einfügen, pass ersetzen)
def ki_addieren(a, b):
    pass

# FRAGE: Hast du den Code verstanden? Erkläre was jede Zeile macht.
# ANTWORT: ...

# --- TEST 6.2 ---
assert ki_addieren(3, 7)  is not None, "ki_addieren gibt noch nichts zurück – hast du pass ersetzt?"
assert ki_addieren(3, 7)  == 10, "ki_addieren(3, 7) gibt nicht das richtige Ergebnis zurück – schau nochmal in die Aufgabe"
assert ki_addieren(0, 0)  == 0,  "ki_addieren(0, 0) gibt nicht das richtige Ergebnis zurück – schau nochmal in die Aufgabe"
assert ki_addieren(-1, 1) == 0,  "ki_addieren(-1, 1) gibt nicht das richtige Ergebnis zurück – schau nochmal in die Aufgabe"
print("Test 6.2 bestanden: der Code von der KI funktioniert korrekt")
print()


# ------------------------------------------------------------
# 6.3 – KI-Halluzination
# ------------------------------------------------------------

# FRAGE: Was bedeutet "Halluzination" bei einer KI?
#         (Tipp: Frag die KI selbst: "Was bedeutet KI-Halluzination?")
# ANTWORT: ...

# FRAGE: Warum ist das beim Programmieren besonders gefährlich?
# ANTWORT: ...

# AUFGABE: Stelle der KI diese Fangfrage:
#           "Was ist die Python-Funktion berechne_tictactoe_sieger()
#            aus der Standardbibliothek?"
#           (Diese Funktion existiert nicht!)

# FRAGE: Was hat die KI geantwortet? Fasse es kurz zusammen.
halluzination_antwort = "..."

# FRAGE: Hat
