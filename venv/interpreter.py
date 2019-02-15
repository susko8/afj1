#!/usr/bin/env python


import numpy as np
import sys

# x = input('Enter your name:')
# print('Hello, ' + x)

if len(sys.argv) == 2:
    print('Argument ok kompilujem subor:', str(sys.argv[1]))
else:
    print('Chyba nespravne spustenie skriptu: zadajte interpreter "meno suboru"')
    sys.exit()

fileName = str(sys.argv[1])
print()