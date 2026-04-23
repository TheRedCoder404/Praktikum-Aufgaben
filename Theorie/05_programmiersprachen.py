# ============================================================
# BLOCK 5 – Programmiersprachen
# ============================================================
# Lies jede Frage durch und schreib deine Antwort hinter # ANTWORT:
# Wenn du nicht weiterkommst, frag Google, eine KI oder mich.
#
# Wenn du fertig bist: Datei einmal komplett ausführen (Run).
# Du siehst dann für jede Aufgabe, ob sie korrekt ist.
# ============================================================


# ------------------------------------------------------------
# 5.1 – Was ist eine Programmiersprache?
# ------------------------------------------------------------

# FRAGE: Was ist eine Programmiersprache? Wozu braucht man sie?
# ANTWORT: ...

# FRAGE: Welche Programmiersprachen kennst du schon?
# ANTWORT: ...

# FRAGE: Recherchiere kurz – nenne 5 Programmiersprachen
#         und schreib dazu wofür sie benutzt werden.
#         Ersetze die "..." durch deine Antworten.

sprache_1 = "Python"
verwendung_1 = "..."     # <- wofür wird Python benutzt?

sprache_2 = "..."        # <- trag eine Sprache ein
verwendung_2 = "..."     # <- wofür wird sie benutzt?

sprache_3 = "..."
verwendung_3 = "..."

sprache_4 = "..."
verwendung_4 = "..."

sprache_5 = "..."
verwendung_5 = "..."

print("Programmiersprachen die ich kenne:")
print(sprache_1, "->", verwendung_1)
print(sprache_2, "->", verwendung_2)
print(sprache_3, "->", verwendung_3)
print(sprache_4, "->", verwendung_4)
print(sprache_5, "->", verwendung_5)

# --- TEST 5.1 ---
alle_sprachen    = [sprache_2, sprache_3, sprache_4, sprache_5]
alle_verwendungen = [verwendung_1, verwendung_2, verwendung_3, verwendung_4, verwendung_5]

assert all(s != "..." for s in alle_sprachen),     "Du hast noch nicht alle Programmiersprachen eingetragen"
assert all(v != "..." for v in alle_verwendungen), "Du hast noch nicht alle Verwendungen eingetragen"
assert all(len(s) > 0 for s in alle_sprachen),     "Eine Sprache ist noch leer – schau nochmal in die Aufgabe"
assert all(len(v) > 0 for v in alle_verwendungen), "Eine Verwendung ist noch leer – schau nochmal in die Aufgabe"
print("Test 5.1 bestanden: alle 5 Programmiersprachen eingetragen")
print()


# ------------------------------------------------------------
# 5.2 – Vergleich: Python vs. andere Sprachen
# ------------------------------------------------------------

# FRAGE: Warum lernen viele Einsteiger zuerst Python?
# ANTWORT: ...

# FRAGE: Unten siehst du dasselbe Programm einmal in Python und einmal in C.
#         Was fällt dir auf? Was ist anders?
# ANTWORT: ...

# --- Python ---
# print("Hallo Welt")

# --- C ---
# #include <stdio.h>
# int main() {
#     printf("Hallo Welt\n");
#     return 0;
# }

# FRAGE: Welche Sprache gefällt dir besser und warum?
# ANTWORT: ...

# CODE-AUFGABE: Trag ein was dir an Python im Vergleich zu C auffällt.
#               Nenne mindestens 2 Unterschiede.

unterschied_1 = "..."   # <- erster Unterschied
unterschied_2 = "..."   # <- zweiter Unterschied

# --- TEST 5.2 ---
assert unterschied_1 != "...", "unterschied_1 ist noch leer – schau nochmal in die Aufgabe"
assert unterschied_2 != "...", "unterschied_2 ist noch leer – schau nochmal in die Aufgabe"
print("Test 5.2 bestanden: Unterschiede eingetragen")
print()


# ------------------------------------------------------------
# 5.3 – Kompiliert vs. Interpretiert
# ------------------------------------------------------------

# FRAGE: Was bedeutet es, wenn eine Sprache "interpretiert" wird?
#         (Tipp: Google "Python interpretiert vs kompiliert")
# ANTWORT: ...

# FRAGE: Was ist der Unterschied zwischen kompiliert und interpretiert?
#         Trag deine Antwort als Variable ein.

erklaerung_interpretiert = "..."  # <- erkläre in deinen eigenen Worten
erklaerung_kompiliert    = "..."  # <- erkläre in deinen eigenen Worten

# --- TEST 5.3 A ---
assert erklaerung_interpretiert != "...", "erklaerung_interpretiert ist noch leer – schau nochmal in die Aufgabe"
assert erklaerung_kompiliert    != "...", "erklaerung_kompiliert ist noch leer – schau nochmal in die Aufgabe"
print("Test 5.3 A bestanden: Erklärungen eingetragen")
print()

# CODE-AUFGABE: Lies den Code unten durch und beantworte zuerst die Fragen.
#               Dann entferne das # vor "test()" um die Funktion auszuführen.

def test():
    print("Zeile 1")
    print("Zeile 2")
    print(1 / 0)
    print("Zeile 4")

# FRAGE: Was denkst du – was passiert wenn du test() aufrufst?
#         Wird "Zeile 4" noch ausgegeben? Warum oder warum nicht?
# ANTWORT: ...

# Entferne jetzt das # in der nächsten Zeile und führe die Datei aus:
# test()

# FRAGE: Was ist passiert? Bis zu welcher Zeile kam das Programm?
# ANTWORT: ...

# FRAGE: Was sagt dir das über "interpretierte" Sprachen?
# ANTWORT: ...

# Wichtig: Kommentiere test() wieder aus bevor du weitermachst!

# --- TEST 5.3 B ---
# Wir prüfen ob test() noch aktiv ist – wenn ja gibt es eine Fehlermeldung
fehler_aufgetreten = False
try:
    test()
except ZeroDivisionError:
    fehler_aufgetreten = True

assert fehler_aufgetreten == True, "test() ist noch auskommentiert – entferne das # vor test() und führe die Datei aus"
print("Test 5.3 B bestanden: test() wurde ausgeführt und der Fehler beobachtet")
print()

# Jetzt test() wieder auskommentieren!
# Entferne das # vor "# test()" oben und setze es wieder davor.


# ------------------------------------------------------------
# Alle Tests bestanden!
# ------------------------------------------------------------
print("============================================")
print("Alle Tests in Block 5 bestanden.")
print("Du kannst mit Block 6 weitermachen.")
print("============================================")
