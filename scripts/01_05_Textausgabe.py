# -*- coding: utf-8 -*-
"""
Ein wichtiger Bestandteil von Programmierung ist die Ausgabe von Text auf das
Terminal. Es ermöglicht ein visülles Feedback an welcher Stelle der
Codeausführung das Skript momentan steht. Auch Ergebnisse können direkt auf das
Terminal ausgegeben werden.

"""

# Python bietet hierzu die print() Funktion an. Dies kann direkt mit
# Strings aufgerufen werden
print('Diese Zeile wird auf dem Terminal ausgegeben.')

# ... oder mit Variablen
var = 'Diese Variable wird gleich ausgegeben.'
print(var)

# Die Objektklasse String bietet eine format() Funktion an, mit der
# definierte Stellen im String mit Variablen ersetzt werden können.
print('{0} + {1} = {2}'.format(1, 2, 1+2))
