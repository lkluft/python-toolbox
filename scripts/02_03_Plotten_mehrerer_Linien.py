# -*- coding: utf-8 -*-
"""Plotten mehrere Linien in einem Plot.

Das Darstellen mehrerer Linien in einem Plot ist sehr einfach und
nützlich für das Vergleichen von Funktionen oder Messreihen.

"""

import numpy as np
import matplotlib.pyplot as plt


# Erstellen der nötigen x, y und z Vektoren
x = np.linspace(-5, 5, 100)
y = 0.5 * x
z = x - 1

# Wird keine neue figure geöffnet, werden alle weiteren Plotbefehle automatisch
# in der alten ausgeführt. Die Farbe wird dabei automatisch geändert, kann aber
# auch von Hand gesetzt werden (s. Beispiel_Plot.py)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, z)

# Anzeigen des Plots
plt.show()
