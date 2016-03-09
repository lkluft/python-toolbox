# -*- coding: utf-8 -*-
"""Umgang mit Fehlwerten in Datensätzen.

In Zeitreihen kommt es immer wieder zu Fehlwerten. Diese werden häufig
durch einen besonderen Wert (z.B. -999) gekennzeichnet.  Um Ergebnisse so
nicht zu verfälschen, müssen sie in Python als NaN (not a number)
gekennzeichnet werden.

"""

import numpy as np


# Als Beispiel legen wir zunächst einen Vektor von Gleitkommazahlen
# (floats) an.  In diesem Vektor repräsentiert die -999 einen Fehlwert.
ts = np.array([14, 15, 15, -999, -999, 13, 14], dtype='float')

# Arrays lassen sich nicht nur mit expliziten Indizes, sondern auch mit
# logischen Ausdrücken aufrufen.  Die nächste Zeile ersetzt jeden Wert
# von ts, der -999 ist, mit dem Wert nan.
ts[ts == -999] = np.nan

# Einige Funktionen in Python (z.B. mean) geben bei Anwendung auf Arrays
# mit nan-Werten selbst auch nur nan als Rückgabewert aus.
print('mean mit nan: {0}'.format(np.mean(ts)))

# Um den Mittelwert der restlichen Zeitreihe zu berechnen, betrachtet
# man nur die Werte ungleich nan.  Hierzu stellt numpy die Funktion
# nanmean() bereit.  Diese Funktion ignoriert alle nan-Werte im
# Datensatz.
print('mean ohne nan: {0}'.format(np.nanmean(ts)))
