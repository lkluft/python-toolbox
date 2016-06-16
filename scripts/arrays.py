# -*- coding: utf-8 -*-
"""Einführung in Rechnugen mit numpy.ndarrays.

Arrays sind ein wichtiges Konstrukt zum Speichern zusammengehöriger
Daten.  Arrays können sowohl direkt per Hand als auch indirekt durch
Funktionen erzeugt werden.

"""

import numpy as np


# Definition per Hand
v1 = np.array([1, 5, 10], dtype='float')

# Ohne die direkte Angabe 'float' hätte Python v1 als Integer-Array
# interpretiert.  Das Hinzufügen eines Dezimalpunktes an einer der
# Zahlen hätte auch ausgereicht, um den Typ des Arrays als 'float' zu
# kennzeichnen:
# >>> np.array([1., 5, 10])

# Automatische Generierung eines Arrays mit drei Zahlen von 10 bis 30.
v2 = np.linspace(10, 30, 3)
# Automatisch genereiert Arrays haben (fast) immer den Typ 'float'.

# Manipulation von Arrays
v1 + 1.  # Erhöhen aller Elemente um 1
v1 * 2.  # Multiplizieren aller Element mit 2
v1 + v2  # Elementweise Summe zweier Arrays

# Inspektion von Arrays
v1.mean()  # Mittelwert alle Elemente
v1.min()  # Kleinstes Element


# Zugriff auf Spalten und Zeilen eines Arrays
# Bei indexbasiertem Zugriff auf Daten eines Arrays ist zu beachten,
# dass Python von 0 an indiziert!
A = np.arange(9).reshape(3, 3)  # Erstellen einer 3x3-Matrix
A[1, 2]  # Dritter Wert der zweiten Zeile von A
A[:, 1]  # Zweite Spalte von A
A[2, :]  # Dritte Zeile von A
