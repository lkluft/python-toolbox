# -*- coding: utf-8 -*-
"""Einlesen einer ASCII-Datei mit numpy.

Das Einlesen von Daten aus Dateien ist meist der erste Schritt der
Datenverarbeitung.  In diesem Skript wird eine einfache Testdatei
eingelesen.  Die verwendeten Funktionen lassen sich bei Bedarf auf
andere Dateien anpassen.  Für weitere Informationen sei auf die
Dokumentation von np.genfromtxt() [0] verwiesen.

[0] http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html

"""

import numpy as np


# Python bietet für das Einlesen von Dateien den with-Block an.  Dieser
# sorgt dafür, dass die Datei nach erfolgreichem Einlesen wieder
# geschlossen wird.

# Die Datei 'Testdatei.csv' aus dem data/ Verzeichnis wird geöffnet und
# ist im Folgenden über die Variable f ansprechbar.

with open('data/Testdatei.csv', 'rb') as f:

    # Mit Hilfe der replace Funktion lassen sich einzelne Zeichen oder
    # Strings in der Datei ersetzen.  Der folgende Befehl ersetzt in
    # jeder Zeile der Datei Kommas durch Punkte (Python erwartet Punkte
    # als Dezimalpunkte).  Seit Python 3 werden files a Byte-Objekte
    # gehandhabt.  Um die String-Operation replace trotzdem ausführen zu
    # können, muss jeder Zeile zunächste dekodiert und anschließend
    # wieder kodiert werden.
    f = [line.decode().replace(',', '.').encode() for line in f]

    # Die NumPy Funktion genfromtxt() liest die Datei in ein Array ein.
    # Die Angabe der Parameter dtype, comments, skip_header und usecols
    # ist in diesem Fall eigentlich nicht nötig, da nur die
    # default-Werte übergeben werden.  Sie dienen lediglich als
    # Beispiel, was unter anderem eingestellt werden kann.
    data = np.genfromtxt(
        f,  # Einzulesende Datei
        dtype=['f8', 'f8'],  # Dateityp der Spalten
        delimiter=';',  # Trennzeichen
        comments='#',  # Kommentarerkennung
        skip_header=0,  # Reihen am Beginn auslassen
        usecols=None  # Ggf. nur einzelne Spalte lesen
        )

print(data)  # Ausgabe der eingelesenen Werte
