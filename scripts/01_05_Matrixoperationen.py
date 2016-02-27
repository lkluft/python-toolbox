# -*- coding: utf-8 -*-
"""Umgang mit mehrdimensionalen Arrays.

Im Folgenden wird der Umgang mit mehrdimensionalen Arrays veranschaulicht. Die
Beispiele zeigen zweidimensionale Arrays (Matrizen), das Verhalten lässt sich
jedoch auf Arrays höherer Dimensionen übertragen.

"""

import numpy as np


# Definition zufälliger Matrizen
A = np.random.random_integers(0, 10, (3,3))
print(A)
B = np.random.random_integers(0, 10, (3,3))
print(B)

# Rechenarten
print(A + B) # Addition
print(A - B) # Subraktion
print(A * B) # Multiplikation
print(A @ B) # Matrixmultiplikation
print(np.cross(A, B)) # Kreuzprodukt
print(A.T) # Transponieren einer Matrix
