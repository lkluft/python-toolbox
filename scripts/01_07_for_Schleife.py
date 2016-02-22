# -*- coding: utf-8 -*-
"""Mehrmalige Codeausführung mittels for-Schleifen.

Schleifen stellen eine wichtige Funktion in der Datenverarbeitung dar.
Sie ermöglichen das wiederholte Ausführen von Anweisungsblöcken.

"""

import numpy as np


# Fibonacci-Folge mit for-Schleife

F = np.zeros(20, dtype='int')
F[1] = 1

# Die Schleife läuft von 2 bis 19 (!). Nach Berechnung der jeweiligen
# Fibonacci-Zahl wird diese ausgegeben.
for i in range(2, len(F)):
    F[i] = F[i-1] + F[i-2]
    print('F({0}) = {1}'.format(i, F[i]))

# Die Deklaration, über welchen Block die Schleife laufen soll, erfolgt wie bei
# der if-Abfrage (s. if_Abfrage.py) per Einrückung der betroffenen Zeilen.
