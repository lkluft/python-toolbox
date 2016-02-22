# -*- coding: utf-8 -*-
"""Einlesen einer ASCII-Datei mit numpy.

Das Einlesen von Daten aus Dateien ist meist der erste Schritt der
Datenverarbeitung. In diesem Skript wird eine einfacheTestdatei eingelesen. Die
verwendeten Funktionen lassen sich bei Bedarf an anderen Dateien anpassen. Für
weitere Informationen lohnt ein Blick in die Dokumentation von genfromtxt [0].

[0] http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.genfromtxt.html

"""

import numpy as np


# Python bietet für das Einlesen von Dateien den with Block an.  Dieser sorgt
# dafür, dass die Datei nach erfolgreichem Einlesen geschlossen wird.

# Die Datei 'Testdatei.csv' wird geöffnet und ist im Folgenden über die Variable
# f ansprechbar.

with open('data/Testdatei.csv') as f:
    # Mit Hilfe der replace Funktion lassen sich einzelne Zeichen oder Strings
    # in der Datei ersetzen. Der folgende Befehl ersetzt in jeder Zeile der
    # Datei Kommas durch Punkte.
    f = [line.replace(',','.') for line in f]

    # Die NumPy Funktion genfromtxt() liest die Datei in einen array ein.
    data = np.genfromtxt(f, # Einzulesende Datei
                         dtype=['f8','f8'], # Angabe des Dateitypen der Spalte
                         delimiter=';', # Trennzeichen zwischen den Werten
                         comments='#', # Einleitendes Zeichen für Kommentare
                         skip_header=0, # Reihen am Dateibeginn auslassen
                         usecols=None # Ggf. nur einzelne Spalte lesen
                        )

# Ausgabe der eingelesenen Werte auf das Terminal
print(data)
