# -*- coding: utf-8 -*-
"""Ausgabe von Text auf die Standardausgabe.

Ein wichtiger Bestandteil von Programmierung ist die Ausgabe von Text
auf das Terminal.  Es ermöglicht ein visuelles Feedback des
Programmablaues.  Auch Ergebnisse können direkt auf das Terminal
ausgegeben werden.

"""

# Mit Hilfe der print()-Funktion können Strings und Variablen direkt
# ausgegeben werden.
print('Diese Zeile wird im Terminal ausgegeben.')

# ... oder mit Variablen
var = 'Diese Variable wird gleich ausgegeben.'
print(var)

# Die Objektklasse String bietet eine format() Funktion an, mit der
# definierte Stellen im String mit Variablen ersetzt werden können.
print('{0} + {1} = {2}'.format(1, 2, 1 + 2))
