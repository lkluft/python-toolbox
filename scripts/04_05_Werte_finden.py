# -*- coding: utf-8 -*-
"""Auffinden von Indizes bestimmter Werte.

Bei der Arbeit mit Arrays ist es häufig nötig bestimmte Werte in einem Datensatz
zu finden. Hierbei kann es nötig sein, die Indizes der betreffenden Werte in
Erfahrung zu bringe.

"""

import numpy as np


# Erstellen eines Datenvektors
a = np.array([1, 2, 1, 3, 4, 1], dtype='float')
print('Array: {0}'.format(a))

# Gibt die Position (den Index) der Werte größer 2 an
print(np.where(a>2))

# Die ermittelten Indizes lassen sich wiederum als Input in den Array geben.
# Somit lässt sich ein Array erzeugen, der alle Werte >2 aus dem Urpsrungsarray
# enthält.
b = a[np.where(a>2)]
print('Werte >2: {0}'.format(b))

# Ist man nicht an den Indizes interessiert, lässt sich dieser Array auch direkt
# über eine logische Bedingung erzeugen.
c = a[a>2]
print('Werte >2: {0}'.format(c))
