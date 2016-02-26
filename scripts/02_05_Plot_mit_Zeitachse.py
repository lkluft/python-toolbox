# -*- coding: utf-8 -*-
"""Plotten von Zeitreihen mit Zeitangabe auf der x-Achse.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Zuerst wird eine Testdatei aus dem Windkanal eingelesen.  Für ein genaueres
# Verständnis der Einleseroutine sei auf das Skript
# Einlesen_einer_ASCII_Datei.csv verwiesen.
with open('data/Windkanal_Testdaten.csv', 'rb') as file:
    file = (line.decode().replace(',','.').encode() for line in file)
    data = np.genfromtxt(file,
                         dtype=None,
                         names=True,
                         delimiter=';',
                        )

# Im nächsten Schritt wird die eingelesene Zeit in einen Zahlenwert umgewandelt.
# Somit lässt sich die Variable time als x-Wert für einen Plot nutzen.
time = mpl.dates.datestr2num(data['TIME'])

# Die Funktion plot_date ermöglicht es, den Zeitplot zu erstellen.
# Eingangsvariablen sind die erzeugte time Variable und die y-Werte.  Zusätzlich
# wird angegeben, welche Variablen ein Datumsformat sind.  Der Parameter
# definiert den Plot (hier blaue Punkte)
fig, ax = plt.subplots()
ax.plot_date(time, data['M40V02'], xdate=True, ydate=False, fmt='bo')
ax.set_ylabel('Windgeschwindigkeit')
ax.set_xlabel('Uhrzeit')

# Mit dem DateFormatter lässt sich das auf der Achse angezeigte Datumsformat
# editieren.
formatter = mpl.dates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(formatter)
#plt.xticks(rotation=45) # Auskommentieren um die x-Ticks zu drehen

plt.show()
