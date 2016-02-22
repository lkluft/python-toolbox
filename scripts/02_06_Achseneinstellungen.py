# -*- coding: utf-8 -*-
"""
Python bietet viele Möglichkeiten die Darstellung von Grafiken (figures) zu
editieren.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Erstellen eines Standardplots
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(-10, 10, 100)
plt.plot(x, x**2)

## Eigenschaften der Achsen editieren
# Wertebereich der Achsen
ax.set_xlim(-10, 10)
ax.set_ylim(0, 100)

# Explizite Angabe der angezeigten Werte auf der y-Achse:
ax.set_yticks([1, 7, 42, 99])

## Achsenbeschriftung

# Die Schriftgrösse (FontSize) auf 16 Pt verändern.
mpl.rc('font', size=16)

# Beschriftung der Achsen und erstellen einer Überschrift
ax.set_xlabel('x-Achse')
ax.set_ylabel('y-Achse')
ax.set_title('Beispielplot')

plt.show() # Anzeigen des Plots
