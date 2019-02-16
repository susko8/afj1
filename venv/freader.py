#!/usr/bin/env python

import sys


def readFile():
    if len(sys.argv) == 2:
        print('Argument ok,\nKompilujem subor:', str(sys.argv[1]), '\nVystup:\n')
    else:
        print('Chyba nespravne spustenie skriptu: zadajte interpreter "meno suboru"')
        sys.exit()
    filename = str(sys.argv[1])
    file = open(filename, 'r')
    filecontent = file.read().splitlines()
    file.close()
    return filecontent
