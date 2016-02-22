# -*- coding: utf-8 -*-
"""Einlesen mehrere Dateien mit Hilfe von glob und numpy.

In der Praxis sind die zu verarbeitenden Daten häufig auf verschiedene Dateien
aufgeteilt. In diesem Fall ist es notwendig, die Dateien einzeln einzulesen und
die darin eingelesenen Daten zu speichern.

"""

import glob

import numpy as np


# Das Modul glob bietet die Möglichkeit mit den normalen Shell-Wildcards zu
# arbeiten. So lassen sich zum Beispiel alle Dateien, deren Name  mit 'test'
# beginnt und die die Endung '.txt' haben, in der Liste files speichern.
files = glob.glob('data/test*.txt')

# Mit einer Schleife lässt sich im Anschluss auf die einzelnen Eintrage
# der Liste zugreifen.
for filepath in files:
    with open(filepath) as f:
        data = np.genfromtxt(f)
    print('Inhalt von Datei ' + filepath)
    print(data)

# Anstatt die einzelnen Arrays nur auszugeben, lassen sich diese auch in einer
# Liste abspeichern. Hierzu muss die Liste vorher deklariert werden. Im
# Anschluss kann der eingelesene Array mit der Funktion append an die Liste
# angehängt werden.
b = []
for filepath in files:
    with open(filepath) as f:
        b.append(np.genfromtxt(f))
