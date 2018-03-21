# -*- coding: utf-8 -*-
"""Eingebaute Datentypen.

Python bietet von sich aus einige grundlegende eingebaut Datentypen an
(built-in datatypes).  Dieses Skript stellt eine Auswahl dieser
Datentypen vor, welche im Alltag der Datenverarbeitung häufig genutzt
werden.  Eine vollstädnige Liste findet sich in der Python Dokumentation:

    https://docs.python.org/2/library/stdtypes.html

"""

# Basistypen

print('integer:', 1)  # Ganzzahlen
print('float:', 1.0)  # Gleitkommazahl
print('string:', 'eins')  # Zeichenkette
print('boolean:', True)  # Boolscher Wahrheitswert

# Erweiterte Datentypen

# Listen dienen zum Zusammenfassen mehrerer Variablen.
# Die Einträge einer Liste haben eine feste Reihenfolge.
int_list = [2, 1, 3]

# Listen lassen sich erweitern...
int_list.append(4)  # int_list = [2, 1, 3, 4]

# und sortieren.
int_list.sort()  # int_list = [1, 2, 3, 4]

# Dictionaries bieten die Möglichkeit Daten unter einem bestimmten `key`
# abzuspeichern.  Der Zugriff auf den gespeicherten Wert erfolgt dann
# über den jeweiligen key.
dictionary = {'key': 1}
var = dictionary['key']  # var = 1
