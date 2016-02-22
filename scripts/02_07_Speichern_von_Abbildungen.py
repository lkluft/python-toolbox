# -*- coding: utf-8 -*-
"""Speichern von Abbildungen.

Die Funktion savefig() bietet die Möglichkeit seine erstellen Grafiken direkt
aus dem Skript heraus abzuspeichern.

"""

import numpy as np
import matplotlib.pyplot as plt


# Erstellen einer Testdatenreihe
x = np.linspace(0, 10, 100)
y = x**2

# Erstellen eines einfachen Plots
fig1, ax = plt.subplots()
ax.plot(x, y)

# Der Zugriff auf die figure erfolgt über die figure handle. Das Dateiformat
# wird direkt im Dateinamen angegeben.
fig1.savefig('./python_testplot.pdf')
fig1.savefig('./python_testplot.png')

# Wenn man die Abmessungen seiner Abbildungen bestimmen möchte, können diese
# beim Aufruf der figure mitangegeben werden. Die Variable nimmt ein Tuple
# entgegen, das (Breite, Höhe) in Inch beinhaltet.
fig2, ax = plt.subplots(figsize=(15, 5))
ax.plot(x, y)

fig2.savefig('./python_testplot2.pdf')
