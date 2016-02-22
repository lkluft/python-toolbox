# -*- coding: utf-8 -*-
"""Plotten von Zeitreihen mit Zeitangabe auf der x-Achse.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Zuerst wird eine Testdatei aus dem Windkanal eingelesen.  Für ein genaueres
# Verständnis der Einleseroutine sei auf das Skript
# Einlesen_einer_ASCII_Datei.csv verwiesen.
with open('data/Windkanal_Testdaten.csv') as file:
    file = (line.replace(',','.') for line in file)
    data = np.genfromtxt(file,
                  dtype=[('index', 'i1'),
                         ('date', 'S10'),
                         ('time', 'S8'),
                         ('speed', 'f8')],
                  delimiter=';',
                  skip_header=1)

# Im nächsten Schritt wird die eingelesene Zeit in einen Zahlenwert umgewandelt.
# Somit lässt sich die Variable time als x-Wert für einen Plot nutzen.
time = mpl.dates.datestr2num(data['time'])

# Die Funktion plot_date ermöglicht es, den Zeitplot zu erstellen.
# Eingangsvariablen sind die erzeugte time Variable und die y-Werte.  Zusätzlich
# wird angegeben, welche Variablen ein Datumsformat sind.  Der Parameter
# definiert den Plot (hier blaü x)
plt.plot_date(time, data['speed'], xdate=True, ydate=False, fmt='bx')
plt.ylabel('Windgeschwindigkeit')
plt.xlabel('Uhrzeit')

# Mit dem DateFormatter lässt sich das auf der Achse angezeigte Datumsformat
# editieren.
formatter = mpl.dates.DateFormatter('%H:%M:%S')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
#plt.xticks(rotation=45) # Auskommentieren um die x-Ticks zu drehen

plt.show()