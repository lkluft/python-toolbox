# -*- coding: utf-8 -*-
"""Plotten mit logarithmischer y-Achse.

Bei der Visualisierung von Daten mit einem sehr großen Wertebereich kann eine
halblogarithmische Darstellung hilfreich sein. Hierbei werden die Daten auf der
y-Achse logarithmisch dargestellt.

"""

import matplotlib.pyplot as plt
import numpy as np

# Erstellen der Datenreihe
x = np.linspace(0, 10, 100)
y = np.exp(x)

fig, axes = plt.subplots(1, 2)
axes[0].semilogy(x, y) # logarithmische y-Achse
axes[1].plot(x, y) # lineare y-Achse

plt.show() # Anzeigens des Plots
