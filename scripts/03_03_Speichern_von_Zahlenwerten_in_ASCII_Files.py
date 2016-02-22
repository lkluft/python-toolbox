# -*- coding: utf-8 -*-
"""Zahlenwerte in eine ASCII-Datei schreiben.

Beim Datenaustausch ist es notwendig, seine Ergebnisse in einem für alle
Anwender verwertbaren Format zu speichern. Hierbei bietet sich z.B. das
Speichern der Daten in einer einfachen ASCII-Datei an.

"""

import numpy as np


# Erstellen einer 5x5-Zufallsmatrix
M = np.random.normal(size=(5, 5))

# Speichern der Matrix M mit Semikolon als Trennungzeichen (Delimiter).
np.savetxt('Testdatei_Semikolon.txt', M, delimiter=';')

# Um einen anderen Delimiter zu verwenden, wird das ; einfach durch das
# gewünschte Zeichen ersetzt. Neben dem Semikolon sind Komma (','), Tab ('\t')
# und Leerzeichen (' ') gängige Delimiter.

# Es ist sinnvoll seinem Datensatz eine Kopfzeile (header) hinzuzufügen, in der
# der Inhalt der Datei beschrieben wird.
# Die Headerzeile ist per default ein Kommentar; ihr wird ein # vorangestellt.
# Möchte man dieses Verhalten umgehen, kann man dies mit dem Keyword
# comments=None ausschalten.
header = 'A,B,C,D,E'
np.savetxt('Testdatei_Header.txt', M, delimiter=',', header=header)
