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

## Rechenarten
# Wenn die Dimensionen zweier Arrays übereinstimmt, lässt sich mit ihnen
# rechnen, wie mit jeder anderen Variablen auc.
print(A + B) # Addition
print(A - B) # Subraktion
print(A * B) # Multiplikation
print(np.dot(A, B)) # Matrixmultiplikation
print(A.T) # Transponieren einer Matrix


## Zugriff auf die Werte einer Matrix
# Zugriff auf Spalten und Zeilen einer Matrix
print(A[1, 2]) # Dritter Wert der zweiten Zeile von A
print(A[:, 1]) # Zweite Spalte von A
print(A[2, :]) # Dritte Zeile von A
