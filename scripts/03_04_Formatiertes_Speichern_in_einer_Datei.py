# -*- coding: utf-8 -*-
"""Daten in bestimmtem Format in eine ASCII-Datei schreiben.

In einigen Fällen kann es erforderlich sein, ein spezielles Datenformat
einzuhalten (Anzahl der Nachkommastellen, etc.).  Hierzu kann beim
Speichern das gewünscht Format explizit angegeben werden.

"""

import numpy as np


# Erstellen von drei Vektoren mit unterschiedichen Daten zum späteren
# Abspeichern.  Dieser Schritt ist unnötig, wenn man beretis Daten hat.
dat1 = np.arange(100)
dat2 = np.linspace(0, 1, 100)
dat3 = np.linspace(200, 1190, 100)

# Die Daten werden mit Hilfe der column_stack Funktion in einem array
# zusammengefasst.  Die ursprünglichen Vektoren werden zu Spalten im
# Vektor.
stacked_data = np.column_stack((dat1, dat2, dat3))

# Speichern der Daten mit eigenen Format fmt. Zur Nutzung der Formate
# siehe Python-Dokumentation.
np.savetxt('Testdatei_formatierte_Daten.txt',
           stacked_data,
           fmt='%3d;%7.5f %7.2f'
          )
