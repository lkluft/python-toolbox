# -*- coding: utf-8 -*-
"""Grundrechenarten mit Python und numpy.

Im folgenden Skript werden die Grundrechenarten in Python vorgestellt. Die
Ergebnisse werden direkt an stdout (i.A. das Terminal) ausgegeben.

"""

import numpy as np


# Grundrechenarten:
print('Grundrechenarten')
print(1 + 2) # Addition
print(3 - 4) # Subtraktion
print(5 * 6) # Multiplikation
print(7 / 8)  # Ganzzahlige Division
print(7. / 8) # Gleitkomma Division
print(4**2) # Quadrat

# Komplexere Rechenoperationen:
print('Komplexere Rechenoperationen')

# Funktionen aus einem Modul werden mittels Punktnotation aufgerufen:
# modul.funktion. Auch Konstanten können in Modulen enthalten sein.
print(np.sqrt(16)) # Wurzel
print(np.pi) # Pi
print(np.sin(np.pi/2)) # Sinus
