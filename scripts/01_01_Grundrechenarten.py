# -*- coding: utf-8 -*-
"""Grundrechenarten mit Python und numpy.

Im folgendenen Skript werden die Grundrechenarten in Python vorgestellt. Die
Ergebnisse werden direkt an stdout (i.A. das Terminal) ausgegeben.

"""

import numpy as np


# Grundrechenarten:
print('Grundrechenarten')
print(1+2)
print(3-4)
print(5*6)
print(7/8)  # Ganzzahlige Division
print(7./8) # Gleitkomma Division
print(4**2)

# Komplexere Rechenoperationen:
print('Komplexere Rechenoperationen')

# Funktionen aus einem Modul werden mittels Punktnotation aufgerufen:
# modul.funktion

print(np.sqrt(16))
print(np.sin(np.pi/2))  # Auch Konstanten können in Modulen enthalten sein.
print(np.cos(np.pi))
