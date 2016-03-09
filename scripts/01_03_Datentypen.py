# -*- coding: utf-8 -*-
"""Eingebaute Datentypen.

Python bietet von sich aus einige grundlegende eingebaut Datentypen an
(built-in datatypes).  Dieses Skript stellt eine Auswahl dieser
Datentypen vor, welche im Alltag der Datenverarbeitung häufig genutzt
werden.  Eine vollstädnige Liste findet sich in der Python Dokumentation
[0].

[0] https://docs.python.org/2/library/stdtypes.html

"""

# Basistypen

i = 1 # Integer (Ganzzahlen)
f = 1.0 # Float (Gleitkommazahl)
s = 'eins' # String (Zeichenkette)
b = True # Boolean (Boolscher Wahrheitswert)


# Erweiterte Datentypen

# Listen dienen zum Zusammenfassen mehrerer Variablen.  Die Einträge
# einer Liste haben eine feste Reihenfolge.  Listen lassen sich
# erweitern und sortieren.
l = [2, 1, 3]
l.append(4)  # l = [2, 1, 3, 4]
l.sort()  # l = [1, 2, 3, 4]

# Dictionaries bieten die Möglichkeit Daten unter einem bestimmten 'key'
# abzuspeichern.  Der Zugriff auf den gespeicherten Wert erfolgt dann
# über den jeweiligen key.
d = {'key': 1}
var = d['key'] # var = 1
