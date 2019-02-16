#!/usr/bin/env python


from freader import readFile
import functions as fns

# pole riadkov suboru
fileContent = readFile()

#pridanie dummy prvku na prve miesto pre implicitne cislovanie
#t.j. pre pristup k riadku indexujem od 1
a='program'
fileContent = [a] + fileContent

i=1
while i < fileContent.__len__():
    codeline = fileContent[i].split(',')
    i += 1
    if codeline[0] == 'READ':
        print('read')
        continue
    elif codeline[0] == 'WRITE':
        print('write')
        continue
    elif codeline[0] == '+':
        print('sucet')
        continue
    elif codeline[0] == '-':
        print('rozdiel')
        continue
    elif codeline[0] == '*':
        print('nasobenie')
        continue
    elif codeline[0] == '<':
        print('smallerThan')
        continue
    elif codeline[0] == '>':
        print('greaterThan')
        continue
    elif codeline[0] == '>==':
        print('greaterThanOrEqual')
        continue
    elif codeline[0] == '<==':
        print('smallerThanOrEqual')
        continue
    elif codeline[0] == '==':
        print('Equal')
        continue
    elif codeline[0] == '=':
        print('Assign')
        continue
    elif codeline[0] == 'JUMP':
        print('jmp')
        continue
    elif codeline[0] == 'JUMPT':
        print('jmpto')
        continue
    elif codeline[0] == 'JUMPF':
        print('jmpif')
        continue
    elif codeline[0] == 'NOP':
        print('nop')
        continue
    else:
        print('neznama instrukcia')







