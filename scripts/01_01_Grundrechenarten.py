# -*- coding: utf-8 -*-
"""Grundrechenarten mit Python und numpy.

Im folgenden Skript werden die Grundrechenarten in Python vorgestellt.
Die Ergebnisse werden direkt an stdout (i.A. das Terminal) ausgegeben.

"""

import numpy as np


# Grundrechenarten:
1 + 2  # Addition
3 - 4  # Subtraktion
5 * 6  # Multiplikation
7 / 8   # Ganzzahlige Division
7. / 8  # Gleitkomma Division
4**2  # Quadrat

# Komplexere Rechenoperationen:
# Funktionen aus einem Modul werden mittels Punktnotation aufgerufen:
# modul.funktion. Auch Konstanten können in Modulen enthalten sein.
np.sqrt(16)  # Wurzel
np.pi  # Pi
np.sin(np.pi/2)  # Sinus
