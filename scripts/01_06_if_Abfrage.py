# -*- coding: utf-8 -*-
"""Steuerung des Programmablaufes mittels if-Abfragen.

Ein elementares Werkzeug der Prozesssteuerung in der Programmierung sind
bedingte Abfagen. In Python lassen sich diese in Form von if-Konstrukten
realisieren. Eine if-Abfrage steuert mit Hilfe einer Bedingung den Ablauf des
Skriptes.

"""

# Anders als in anderen Programmiersprachen werden Anweisungen nicht
# durch ein Keyword (z.B. endif, end, fi, ...) beendet oder eingeklammert.
# Der Block wird leidglich durch Einrückung deklariert!

x = 2

# Einfache Abfragen
if x == 2:
    print('Ich werde ausgeführt.')

if x < 2:
    print('Ich werde nicht ausgeführt.')

if ( x > 2 ) or ( x == 2 ):
    print('Ich werde ausgeführt.')

if ( x > 2 ) and (x == 2 ):
    print('Ich werde nicht ausgeführt.')

# Geschachtelte Abfrage
if x == 3:
    print('Ich werde zwar nicht ausgeführt.')
elif x == 2:
    print('Ich aber.')
else:
    print('Ich würde ausgeführt, wenn keine Bedingung erfüllt ist.')
