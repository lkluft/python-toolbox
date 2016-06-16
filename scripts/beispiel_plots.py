# -*- coding: utf-8 -*-
"""Erstellen einfacher Plots mit matplotlib.

Das grafische Darstellen von Daten ist einer der wichtigsten
Aufgabenbereiche der Datenverarbeitung. Wir verwenden zu diesem Zweck
matplotlib [0], eine plotting library, die sich als de facto Standard
für Visualisierungen aller Art etabliert hat.

[0] http://matplotlib.org/

"""

import matplotlib.pyplot as plt
import numpy as np


# Erstellen einer Datenreihe (Nebenrechnung)
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)

# Plot der Daten als Linie
fig, ax = plt.subplots()
ax.plot(x, y, color='r', linewidth=2)
ax.legend('Beispiel', loc='upper left')


# Plot der einzelnen Datenpunkte
fig, ax = plt.subplots()
ax.plot(x, y, linestyle='none', marker='x', markersize=10)

# Plots werden in Python im Hintergrund geöffnet und müssen aktiv in den
# Vordergrund geholt werden, wenn man sie betrachten möchte.
plt.show()
