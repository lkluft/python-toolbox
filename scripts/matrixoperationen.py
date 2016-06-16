# -*- coding: utf-8 -*-
"""Umgang mit mehrdimensionalen Arrays.

Im Folgenden wird der Umgang mit mehrdimensionalen Arrays
veranschaulicht.  Die Beispiele zeigen zweidimensionale Arrays
(Matrizen), das Verhalten lässt sich jedoch auf Arrays höherer
Dimensionen übertragen.

"""

import numpy as np


# Definition zufälliger Matrizen
A = np.random.random_integers(0, 10, (3, 3))
B = np.random.random_integers(0, 10, (3, 3))

# Rechenarten
A + B  # Addition
A - B  # Subraktion
A * B  # Multiplikation
A @ B  # Matrixmultiplikation
np.cross(A, B)  # Kreuzprodukt
A.T  # Transponieren einer Matrix
