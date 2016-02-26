#Python Toolbox
Eine Sammlung von Skripten, die zur Einführung in die Datenverarbeitung mit
Python 3.5 dienen soll.

##Installation
Bei der Python Toolbox handelt es sich nicht um ein eigenständiges Paket sondern
lediglich um eine Sammlung von Skripten (s.
[Dokumentation](doc/toolbox-doc.pdf)).  Aus diesem Grund muss die Toolbox nicht
im klassischesn Sinne installiert werden. Es genügt das Github Repository zu
klonen. Um alle Skripte korrekt ausführen zu können, sind jedoch einige wenige
Abhängigkeiten zu erfüllen.

Nutzer von [Anaconda](https://www.continuum.io/downloads) können mit Hilfe der
beiliegenden `environment.yml` eine eigenständige Umgebung aufsetzen, die alle
nötigen Pakete beinhaltet. Hierzu reicht es im Hauptverzeichnis folgendes
Kommando auszuführen:

`conda env create`

Möchte man die Pakete mit `pip` installieren, kann die klassische
`requirements.txt` verwendet werden.


##Inhaltsverzeichnis
0. Einführung
  * [Aufbau eines Python-Skriptes](scripts/00_01_Aufbau_eines_Python_Skriptes.py)
1. Basics
  * [Grundrechenarten](scripts/01_01_Grundrechenarten.py)
  * [Arrays](scripts/01_02_Arrays.py)
  * [Matrixoperationen](scripts/01_03_Matrixoperationen.py)
  * [Strings](scripts/01_04_Strings.py)
  * [Textausgabe](scripts/01_05_Textausgabe.py)
  * [if-Abfrage](scripts/01_06_if_Abfrage.py)
  * [for-Schleife](scripts/01_07_for_Schleife.py)
  * [Aufruf externer Programme](scripts/01_08_Aufruf_externer_Programme.py)
2. Plotten
  * [Beispiel Plots](scripts/02_01_Beispiel_Plots.py)
  * [Beispiel Subplot](scripts/02_02_Beispiel_Subplot.py)
  * [Plotten mehrerer Linien](scripts/02_03_Plotten_mehrerer_Linien.py)
  * [Plotten mit logarithmischer Achse](scripts/02_04_Plotten_mit_logarithmischer_Achse.py)
  * [Plot mit Zeitachse](scripts/02_05_Plot_mit_Zeitachse.py)
  * [Achseneinstellungen](scripts/02_06_Achseneinstellungen.py)
  * [Speichern von Abbildungen](scripts/02_07_Speichern_von_Abbildungen.py)
3. Input & Output
  * [Einlesen einer Datei](scripts/03_01_Einlesen_einer_Datei.py)
  * [Einlesen mehrerer Dateien](scripts/03_02_Einlesen_mehrerer_Dateien.py)
  * [Speichern in einer Datei](scripts/03_03_Speichern_in_einer_Datei.py)
  * [Formatiertes Speichern in einer Datei](scripts/03_04_Formatiertes_Speichern_in_einer_Datei.py)
4. Datenverarbeitung
  * [Lineares Fitten](scripts/04_01_Lineares_Fitten.py)
  * [Exponential Fit](scripts/04_02_Exponential_Fit.py)
  * [Fehlwerte](scripts/04_03_Fehlwerte.py)
  * [Historgramme](scripts/04_04_Histogramme.py)
  * [Werte finden](scripts/04_05_Werte_finden.py)
  * [Autokorrelation](scripts/04_06_Autokorrelation.py)
  * [Fouriertransformation](scripts/04_07_Fouriertransformation.py)
