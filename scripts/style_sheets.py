# -*- coding: utf-8 -*-
"""Anpassung des Plotstyles mittels style sheets.

Matplotlib bietet mit den sogenannten style sheets [0] einen
komfortablen Weg an, das Aussehen von Plots zu manipulieren.  Diese
ermöglichen es die Parameter zur Darstellung seiner Abbildungen zentral
zu definieren und in seinen Skripten zu laden.  Auf diese Weise ist es
sehr einfach Abbildungen den gewünschten Look zu verleihen oder diesen
zu ändern.

[0] http://matplotlib.org/users/style_sheets.html
"""

import numpy as np
import matplotlib.pyplot as plt


# Liste der verfügbaren styles.
print(plt.style.available)

# Setzen eines matplotlib styles.
plt.style.use('bmh')

x = np.linspace(0, 2*np.pi, 50)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label='Sinus')
ax.plot(x, np.cos(x), label='Kosinus')
ax.legend()

plt.show()
