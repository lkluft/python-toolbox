# -*- coding: utf-8 -*-
"""Formatierte Daten in ASCII-files schreiben.
"""

import numpy as np


# Erstellen von drei Vektoren mit unterschiedichen Daten zum späteren
# Abspeichern. Dieser Schritt ist unnötig, wenn man beretis Daten hat.
dat1 = np.linspace(1, 100, 100)
dat2 = np.linspace(0, 10, 100)
dat3 = np.linspace(200, 1190, 100)

## Speichern in ASCII-File
# Erstellen einer Headerzeile
header = "Ich bin eine Headerzeile"

# Die Daten werden mit Hilfe der column_stack Funktion in einem array
# zusammengefasst. Die ursprünglichen Vektoren werden zu Spalten im Vektor.
stacked_data = np.column_stack((dat1, dat2, dat3))

# Speichern der Daten mit eigenen Format fmt. Zur Nutzung der Formate siehe
# Python-Dokumentation
np.savetxt('Testdatei_formatierte_Daten.txt',
           stacked_data,
           fmt='%5.0f;%7.2f %7.2f',
           header=header)

# Die Headerzeile ist per default ein Kommentar; ihr wird ein # vorangestellt.
# Möchte man dieses Verhalten umgehen, kann man dies mit dem Keyword
# comments=None ausschalten.
