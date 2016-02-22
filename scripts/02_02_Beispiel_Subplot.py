# -*- coding: utf-8 -*-
"""Erstellen von Subplots mit matplotlib.

Um mehrere Plots in einer figure zu plotten, gibt es den Befehl subplot(). Seine
Anwendung soll hier an einem einfachen Beispiel gezeigt werden.

"""

import matplotlib.pyplot as plt
import numpy as np


# Erstellen eines x-Vektors (Nebenrechnung)
x = np.linspace(0, 10, 100)

# Erstellen einer figure mit zwei Plots nebeneinander.
# plt.sublots(Reihen, Spalten)
fig, axes = plt.subplots(1, 2)

# Die Variable axes ist ein Array, mit dessen Einträgen auf die einzelnen
# Subplots zugegriffen werden kann.
axes[0].plot(x, np.sin(x))
axes[0].set_title('Sinus')
axes[1].plot(x, np.cos(x))
axes[1].set_title('Cosinus')

plt.show() # Anzeigen des Plots
