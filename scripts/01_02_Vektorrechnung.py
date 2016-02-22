# -*- coding: utf-8 -*-
"""Einführung in Rechnugen mit numpy.ndarrays.

Arrays sind ein wichtiges Konstrukt zum Speichern zusammengehöriger Daten.
Arrays können sowohl direkt per Hand als auch indirekt durch Funktionen erzeugt
werden.  Es empfiehlt sich immer den Typ der gespeicherten Werte anzugeben
('long','float',...).

"""

import numpy as np


# Definition per Hand
v1 = np.array([1, 5, 10], dtype='float')
# Ohne die direkte Angabe 'float' hätte Python v1 als Integer-Array
# interpretiert.

# Automatische Generierung eines Arrays mit drei Zahlen von 10 bis 30.
v2 = np.linspace(10, 30, 3)

# Ausgabe der beiden Arrays
print(v1, v2)

# Vektoroperationen
print(v1 + 1) # Erhöhen aller Werte um 1
print(v2 * 2) # Multiplizieren aller Werte mit 2
print(v1 + v2) # Elementweise Summe zweier Vektoren
print(v1 * v2) # Elementweise Multiplikation zweier Vektoren
print(np.dot(v1, v2)) # Vektorprodukt
print(np.cross(v1, v2)) # Kreuzprodukt
