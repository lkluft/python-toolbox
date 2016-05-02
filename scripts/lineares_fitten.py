# -*- coding: utf-8 -*-
"""Anpassen einer Geraden an einen Datensatz.

Zum Ermitteln von Trends in Datenreihen, kann eine lineare Regression
durchgeführt werden.  Diese lässt sich mit der numpy Funktion polyfit
durchführen.

"""

import matplotlib.pyplot as plt
import numpy as np


# Erstellen einer Zufallsreihe mit zufälligem Rauschen
x = np.linspace(1, 10, 100)
y = 0.5*x + np.random.uniform(-1, 1, size=100)

# Ausgleichsgerade 1. Ordnung erstellen [ f(x) = a(1) * x + a(2) ]
a = np.polyfit(x, y, 1)

# Plotten der Ausgleichsgeraden durch die Punktwolke
fig, ax = plt.subplots()
ax.plot(x, y, marker='x', linestyle='none')  # Plot der Zahlenreihe
ax.plot(x, np.polyval(a, x), 'r')  # Plot des Fits

plt.show()  # Anzeigen des Plots
