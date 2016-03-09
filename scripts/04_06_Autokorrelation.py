# -*- coding: utf-8 -*-
"""Berechnen der Autokorrelationsfunktion einer Datenreihe.  """

import matplotlib.pyplot as plt
import numpy as np

# Erstellen eines Cosinus mit Rauschen
x = np.linspace(0, 25, 200)
y = 2*np.cos(2*x) + np.random.normal(size=x.size)

# Die Autkorrelation wird mit Hilfe der Funktion correlate() gebildet.
# Das Ergebnis wird direkt skaliert.
ac = np.correlate(y, y, mode='full') / np.sum(y**2)

# Durch den Parameter mode='full' wird die Korrelationsfunktion
# beidseitig bestimmt.  Im folgenden Schritt wird die erste Hälfte des
# Vektors abgeschnitten.  (Sprich: "Von der Hälfte der Länge des Vektors
# bis zu seinem Ende")
ac = ac[ac.size/2:]

# Plotten der Zeitreihe und der Autkokorrelation
fig, ax = plt.subplots()
ax.plot(x, y, 'r', x, ac, 'b')
ax.legend(['Messreihe', 'Autokorrelation'])

plt.show()  # Anzeigen des Plots
