# -*- coding: utf-8 -*-
"""Steürung des Programmablaufes mittels if-Abfragen.

Ein elementares Werkzeug der Prozesssteürung in der Programmierung sind
bedingte Abfagen. In Python lassen sich diese in Form von if-Konstrukten
realisieren. Eine if-Abfrage steürt mit Hilfe einer Bedingung den Ablauf des
Skriptes.

"""

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

# Mehrfache Abfrage
if x == 3:
    print('Ich werde zwar nicht ausgeführt.')
elif x == 2:
    print('Ich aber.')
else:
    print('Ich würde ausgeführt werden, wenn nichts zutrifft.')

# Anders als in anderen Programmiersprachen werden Anweisungen nicht
# durch ein Keyword (z.B. endif, end, fi, ...) beendet oder eingeklammert.
# Der Block wird leidglich durch Einrückung deklariert!
