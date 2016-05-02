# -*- coding: utf-8 -*-
"""Einlesen einer netCDF-Datei.

Das netCDF-Dateiformat ist in den Klimawissenschaften sehr stark
verbreitet.  Mit Hilfe des netCDF4-Moduls lassen sich Daten in diesem
Format bequem einlesen und weiterverarbeiten.  """

from netCDF4 import Dataset
import matplotlib.pyplot as plt


# Öffnen der netCDF-Datei als Dataset-Objekt.
nc = Dataset('data/test_data.nc')

# Die gespeicherten Daten lassen sich über das Dictionary nc.variables
# ansprechen.  Mit Hilfe der Keys lässt sich eine Übersicht über die
# vorhandenen Daten gewinnen.
print(nc.variables.keys())

# Speichern der Daten als Variablen.
# (Erst an dieser Stelle werden die Daten wirklich gelesen!)
lon = nc.variables['lon']
lat = nc.variables['lat']
temp = nc.variables['temp']

# Plot der eingelesenen Daten.
fig, ax = plt.subplots()
ax.pcolormesh(lon, lat, temp)
plt.show()
