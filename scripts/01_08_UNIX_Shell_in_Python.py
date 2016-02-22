# -*- coding: utf-8 -*-
"""Aufruf von externen Programmen aus einem Pythonskript.

Aus einem Pythonskript lassen sich auch externe Programme starten. Dies kann
bei der Vor- und Nachverarbeitung von Daten hilfreich sein.

"""

import subprocess


# Mit Hilfe des Shell-Kommandos 'who' anzeigen lassen, wer noch auf dem System
# eingeloggt ist.
subprocess.call(['who'])
