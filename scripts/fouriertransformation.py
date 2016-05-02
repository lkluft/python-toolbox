# -*- coding: utf-8 -*-
"""Anwenden der FFT auf einen Datensatz.

Bei der Untersuchung von Zeitreihen kann mit Hilfe einer
Fouriertransformation bestimmt werden, ob dem Datensatz eine Periodiztät
zugrunde liegt.  Zur Veranschaulichung wird eine Datenreihe mit
Frequenzen bei 5 und 25 Hz erzeugt und verrauscht.

"""

import matplotlib.pyplot as plt
import numpy as np


# Abtastfrequenz des Messgerätes
Fs = 150  # Abtastfreuenz
Ts = 1.0 / Fs  # Abtastintervall

# Erstellen einer Zeitreihe (Sinus + Rauschen)
t = np.arange(0, 1, Ts)
y = (np.sin(2*np.pi*5*t) + 0.6*np.sin(2*np.pi*25*t)
     + 0.7*np.random.normal(size=t.size))

# Plot der Zeitreihe und Beschriftung der Achsen
fig, axes = plt.subplots(2, 1)
axes[0].plot(t, y)
axes[0].set_xlabel('Zeit')
axes[0].set_ylabel('Amplitude')

# Berechnung der Fouriertransformierten
n = len(y)  # Länge der Zeitreihe
k = np.arange(n)  # Werte von 0 bis Länge(y)-1
T = n / Fs  # Aufnahmelänge der Zeitreihe
freq = k / T  # Beidseitiger Frequenzbereich
Y = np.fft.fft(y) / n   # FFT Berechnung und Normierung

# Abschneiden der zweiten Vektorhälfte um einseitge FFT für Zeitreihen
# mit realen Werten zu erhalten
Y = 2 * Y[range(int(n / 2))]  # Amplitude der Fouriertransformierten
freq = freq[range(int(n / 2))]  # Einseitiger Frequenzbereich

# Plot der Fouriertransformation
axes[1].plot(freq, abs(Y), 'r')
axes[1].set_xlabel('Frequenz (Hz)')
axes[1].set_ylabel('Amplitude')

plt.show()  # Anzeigen des Plots
