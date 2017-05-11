# Python Toolbox
Eine Sammlung von Skripten, die zur Einführung in die Datenverarbeitung mit
Python 3.5 dienen soll.

## Installation
Bei der Python Toolbox handelt es sich nicht um ein eigenständiges Paket
sondern lediglich um eine Sammlung von Skripten (s.
[Dokumentation](doc/toolbox-doc.pdf)).  Aus diesem Grund muss die Toolbox nicht
im klassischen Sinne installiert werden. Es genügt das Github Repository zu
klonen. Um alle Skripte korrekt ausführen zu können, sind jedoch einige wenige
Abhängigkeiten zu erfüllen.

Nutzer von [Anaconda](https://www.continuum.io/downloads) können mit Hilfe der
beiliegenden `environment.yml` eine eigenständige Umgebung aufsetzen, die alle
nötigen Pakete beinhaltet. Hierzu reicht es im Hauptverzeichnis folgendes
Kommando auszuführen:

```bash
conda env create
```

## Inhaltsverzeichnis
0. Einführung
  * [Aufbau eines Python-Skriptes](scripts/aufbau_eines_python_skriptes.py)
1. Basics
  * [Grundrechenarten](scripts/grundrechenarten.py)
  * [Variablen](scripts/variablen.py)
  * [Datentypen](scripts/datentypen.py)
  * [Arrays](scripts/arrays.py)
  * [Matrixoperationen](scripts/matrixoperationen.py)
  * [Strings](scripts/strings.py)
  * [Textausgabe](scripts/textausgabe.py)
  * [if-Abfrage](scripts/if_abfrage.py)
  * [for-Schleife](scripts/for_schleife.py)
  * [Aufruf externer Programme](scripts/aufruf_externer_programme.py)
  * [Funktionen](scripts/funktionen.py)
2. Plotten
  * [Beispiel Plots](scripts/beispiel_plots.py)
  * [Beispiel Subplot](scripts/beispiel_subplot.py)
  * [Plotten mehrerer Linien](scripts/plotten_mehrerer_linien.py)
  * [Plotten mit logarithmischer Achse](scripts/plotten_mit_logarithmischer_achse.py)
  * [Plot mit Zeitachse](scripts/plot_mit_zeitachse.py)
  * [Achseneinstellungen](scripts/achseneinstellungen.py)
  * [Style sheets](scripts/style_sheets.py)
  * [Speichern von Abbildungen](scripts/speichern_von_abbildungen.py)
3. Input & Output
  * [Einlesen einer Datei](scripts/einlesen_einer_datei.py)
  * [Einlesen mehrerer Dateien](scripts/einlesen_mehrerer_dateien.py)
  * [Speichern in einer Datei](scripts/speichern_in_einer_datei.py)
  * [Formatiertes Speichern in einer Datei](scripts/formatiertes_speichern_in_einer_datei.py)
  * [Einlesen einer netCDF-Datei](scripts/einlesen_einer_netcdf-datei.py)
4. Datenverarbeitung
  * [Lineares Fitten](scripts/lineares_fitten.py)
  * [Exponential Fit](scripts/exponential_fit.py)
  * [Fehlwerte](scripts/fehlwerte.py)
  * [Histogramme](scripts/histogramme.py)
  * [Werte finden](scripts/werte_finden.py)
  * [Autokorrelation](scripts/autokorrelation.py)
  * [Fouriertransformation](scripts/fouriertransformation.py)
