# -*- coding: utf-8 -*-
"""Definition eigener Funktionen.

Werden bestimmte Operationen häufiger angewandt, lohnt es sich meist,
diese in Funktionen zusammenzufassen.  Auf diese Weise kann im
folgenden Code einfach auf die Funktionalität zurückgegriffen werden.

"""

import numpy as np


# Funktionen werden mit Hilfe von def definiert. Zusätzlich zum Namen
# muss man die Parameter angeben, von denen die Funktion abhängt.  Es
# ist üblich, die Funktion in einem Docstring kurz zu beschreiben.  Das
# Ergebnis der Funktion wird mittels return zurückgegeben.
def f1(a, b):
    """Berechnet eine mathematische Funktion."""
    return a**2 + b


# Innerhalb des Funktionsblocks lassen sich auch komplexere Rechnungen
# ausführen.  Das return-Statement kann in diesem Fall genutzt werden,
# um Variablen gezielt zurückzugeben.
def f2(a, b):
    """Gibt einen Array der Länge a mit den Werten b wieder."""
    x = np.ones(a)
    y = b * x
    return y


# Eigene Funktionen lassen sich nach ihrer Definition genau so verwenden
# wie interne Pythonfunktionen. Rückgabewerte lassen sich in Variablen
# speichern, oder direkt verwenden.
x = f1(2, 1)
print(x)
print(f2(10, 3))
