# -*- coding: utf-8 -*-
"""Einlesen einer netCDF-Datei.

Das netCDF-Dateiformat ist in den Klimawissenschaften weit verbreitet.
Mit Hilfe des Pythonmoduls `netCDF4` lassen sich netCDF-Daten bequem
einlesen und weiterverarbeiten.
"""
from netCDF4 import Dataset
import matplotlib.pyplot as plt


# Öffnen der netCDF-Datei als Dataset-Objekt.
nc = Dataset('data/test_data.nc')

# Die gespeicherten Daten lassen sich über das dict-like `nc.variables`
# ansprechen.  Das Attribut `keys` gibt eine Übersicht über die
# vorhandenen Daten.
print(nc.variables.keys())

# Auslesen der Daten in eine Variablen.
# (Erst durch die Indizierung hier werden die Daten wirklich gelesen!)
lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]
temp = nc.variables['temp'][:]

# Plot der eingelesenen Daten.
fig, ax = plt.subplots()
sm = ax.pcolormesh(lon, lat, temp, cmap='inferno')
fig.colorbar(sm, label='Temperatur [K]')
plt.show()
