# -*- coding: utf-8 -*-
"""Erstellen einfacher Histogramme mit numpy und matplotlib.

Histogramme lassen sich in Python mit der Funktion hist()
erstellen. Als Parameter werden der Funktion der zu analysierende
array und die bin-Grösse mitgegeben.

"""

import matplotlib.pyplot as plt
import numpy as np


# Erstellen von normalverteilten Daten
x=np.random.normal(size=100)

# n: Anzahl der Werte im bin
# bins: Grenzen der bins

## Histogramm mit 5 bin-Klassen
fig, axes = plt.subplots(1, 2)
n, bins, _ = axes[0].hist(x, bins=5)

## Histogramm mit vorgegebenen Grenzen
n, bins, _ = axes[1].hist(x, range=[-3, 3])

plt.show()
