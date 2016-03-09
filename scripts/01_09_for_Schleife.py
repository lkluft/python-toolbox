# -*- coding: utf-8 -*-
"""Mehrmalige Codeausführung mittels for-Schleifen.

Schleifen stellen eine wichtige Funktion in der Datenverarbeitung dar.
Sie ermöglichen das wiederholte Ausführen von Anweisungsblöcken.

In diesem Skript wird eine for-Schleife verwendet, um die ersten 20
Fibonacci-Zahlen zu berechnen.

"""

import numpy as np


# Initialisierung eines Arrays mit 20 Nullen.
F = np.zeros(20, dtype='int')

# F[0]=0, F[1]=1
F[1] = 1

# Die Schleife läuft von 2 an über alle Einträge im Array.  Nach
# Berechnung der jeweiligen Fibonacci-Zahl wird diese ausgegeben.
for i in np.arange(2, len(F)):
    F[i] = F[i-1] + F[i-2]
    print('F({0}) = {1}'.format(i, F[i]))

# Die Deklaration, über welchen Block die Schleife laufen soll, erfolgt
# wie bei der if-Abfrage (s. 01_06_if_Abfrage.py) per Einrückung der
# jeweiligen Zeilen.
