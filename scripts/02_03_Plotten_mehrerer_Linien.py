# -*- coding: utf-8 -*-
"""Plotten mehrere Linien in einem Plot.

Das Darstellen mehrerer Linien in einem Plot ist sehr einfach und
nützlich für das Vergleichen von Funktionen oder Messreihen.

"""

import matplotlib.pyplot as plt
import numpy as np


# Erstellen der nötigen x, y und z Vektoren
x = np.linspace(-5, 5, 100)
y1 = 0.5 * x
y2 = x - 1

# Wird keine neue figure geöffnet, werden alle weiteren Plotbefehle
# automatisch in der aktuellen ausgeführt.  Die Linienfarbe wird dabei
# automatisch geändert, kann aber auch von Hand gesetzt werden (s.
# 02_01_Beispiel_Plot.py)
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)

plt.show()  # Anzeigen des Plots
