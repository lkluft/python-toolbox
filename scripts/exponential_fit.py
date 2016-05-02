# -*- coding: utf-8 -*-
"""Anpassen einer e-Funktion an einen Datensatz.

Exponentielles Fitten ist ein häufiger Schritt bei der Auswertung von
Messreihen.  In Python bietet das Modul scipy.optimize eine curve_fit()
Funktion.  Diese ermöglicht das Fitten von Daten an eine beliebige
Funktion.

"""

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np


# Erstellen einer zufälligen Zeitreihe. (e-Funktion + Rauschen)
x = np.linspace(1, 5, 100)
y = 10 + np.exp(x) + 5*np.random.normal(size=np.size(x));

# Definition der Funktion func, an die gefittet werden soll.
def func(x, a, b, c):
    return a + b * np.exp(c * x)

# Exponentielles-Fitten: Der Funktion curve_fit werden die anzufittende
# Funktion, die x-Werte und die y-Werte mitgegeben.
popt, pcov = curve_fit(func, x, y)

# popt: Array, das die Werte für die Parameter a, b und c beinhaltet.
# pcov: Geschätzte Kovarianz von popt.

# Plot der Punktwolke und der gefitteten Funktion
fig, ax = plt.subplots()
ax.plot(x, y, marker='x', markersize=5, linestyle='none')
ax.plot(x, func(x, *popt), color='r')
ax.legend(['Data','Fit'],loc='upper left')

plt.show()  # Anzeigen des Plots
