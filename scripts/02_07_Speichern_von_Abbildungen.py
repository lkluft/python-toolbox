# -*- coding: utf-8 -*-
"""Speichern von Abbildungen.

Die Funktion savefig() bietet die Möglichkeit erstellte Grafiken direkt aus dem
Skript heraus abzuspeichern.

"""

import matplotlib.pyplot as plt
import numpy as np


# Erstellen einer Testdatenreihe
x = np.linspace(0, 10, 100)
y = x**2

# Erstellen eines einfachen Plots
fig, ax = plt.subplots()
ax.plot(x, y)

# Der Zugriff auf die figure erfolgt über die Variable fig. Das Dateiformat
# wird direkt durch die Dateiendung bestimmt.
fig.savefig('./python_testplot.pdf')
fig.savefig('./python_testplot.png')
