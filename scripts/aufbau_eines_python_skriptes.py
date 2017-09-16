# -*- coding: utf-8 -*-
"""Aufbau eines Pythonskriptes.

In der ersten Zeile wird das Encoding des Files angegeben.  UTF-8
ermöglicht die Nutzung von Umlauten.

Im Anschluss an das Encoding sollte immer ein Docstring folgen.  Dieser ist
durch dreifache Anführungszeichen gekennzeichnet.  Die erste Zeile sollte in
einem Satz die Funktion des Skriptes beschreiben.  In den folgenden Zeilen kann
dann weiter ins Detail gegangen werden.

"""

# Kommentare innerhalb des Codes werden mit einer Raute eingeleitet.

# Zu Beginn eines Python Skriptes werden benötigte Module geladen.
# Diese enthalten Funktionen und Konstanten auf die im späteren Verlauf
# mittels Punktnotation (modul.funktion) zugegriffen werden kann.  Zur
# leichteren Anwendung können diesen Kürzel zugeordnet werden.  Um in
# der Vielfalt der Pythonmodule nicht die Uebersicht zu verlieren,
# beschränkt sich dieser Werkzeugkasten auf folgende Module:

import glob  # noqa
import os  # noqa
import subprocess  # noqa

from netCDF4 import Dataset  # noqa
import matplotlib as mpl  # noqa
import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa
import scipy as sp  # noqa

# Um Details über die verschiedenen Module zu erhalten, kann die interne
# help-Funktion von Python genutzt werden.  Mit Hilf von help(modul)
# gelangt man zu einer Übersichtsseite von modul:
# >>> import os
# >>> help(os)

# Sollte beim Ausführen dieses Skriptes ein Fehler auftreten, sind
# einige Module nicht installiert, oder es wird eine falsche
# Python-Version verwendet.  In diesem Fall sei auf den Unterpunkt
# Installation in der README.md verwiesen.
