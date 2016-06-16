# -*- coding: utf-8 -*-
"""Umgange mit Zeichenketten.

Der Umgang mit Zeichenketten (Strings) hat viele praktische Anwendungen:
Sei es das Einlesen von Dateien oder die Kommentierung von Plots und
Ausgabedateien.  Im Folgenden werden einige grundlegende Funktionen zur
Stringbearbeitung erläutert.

"""

# Erstellen eines Strings:
# Um einen String einer Variablen zu zuordnen, wird dieser in
# 'Apostrophe' oder "Anführungszeichen" gesetzt.
s1 = 'Teststring 1'
s2 = "Teststring 2"

# Sämtliche Zeichen (character) innerhalb der Markierungen werden dem
# String zugeordnet.
s3 = 'Alles.was_hier steht,ist;ein:String'

# Häufig kommt es vor, dass man ein Ergebnis in einen String umwandeln
# möchte (z.B. dynamische Abbildungstitel).  Die Umwandlung von Zahlen in
# Strings erfolgt z.B. über die Funktion str()
x = 1 + 2  # enthält die Zahl 3
s4 = str(x)  # enthält das Zeichen '3' als Character/String

# Möchte man mehrere Strings zusammensetzen, kann man diese mit Hilfe
# des + Operators verknüpfen.
s5 = 'Eins plus zwei ist ' + s4

# Strings lassen sich mit den Funktion print() ausgeben.
for s in [s1, s2, s3, s4, s5]:
    print(s)
