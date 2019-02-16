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
        if not fns.read(codeline):
            print('Chyba funkcie nacitania premennej na riadku', i - 1, 'program nemoze pokracovat')
            break
        continue
    elif codeline[0] == 'WRITE':
        if not fns.write(codeline):
            print('Chyba funkcie vypisu premennej na riadku',i-1,'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '+':
        if not fns.addition(codeline):
            print('Chyba funkcie suctu na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '-':
        if not fns.subtraction(codeline):
            print('Chyba funkcie rozdielu na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '*':
        if not fns.multiplication(codeline):
            print('Chyba funkcie sucinu na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '<':
        if not fns.smaller_than(codeline):
            print('Chyba funkcie porovnavanie "<" na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '>':
        if not fns.greater_than(codeline):
            print('Chyba funkcie porovnavanie ">" na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '>=':
        if not fns.greater_or_equal_than(codeline):
            print('Chyba funkcie porovnavanie ">=" na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '<=':
        if not fns.smaller_or_equal_than(codeline):
            print('Chyba funkcie porovnavanie ">=" na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '==':
        if not fns.equal_to(codeline):
            print('Chyba funkcie porovnavanie ">=" na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == '=':
        if not fns.assign(codeline):
            print('Chyba funkcie priradenia premennej "=" na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == 'JUMP':
        if fns.getVariable(codeline[1]) == 'problem' and not fns.represents_integer(codeline[1]):
            print('Chyba premenna',codeline[1],'pri JUMP nebola deklarovana')
            break
        if int(fileContent.__len__()) - 1 >= int(codeline[1]) > 0:
            i=int(codeline[1])
        else:
            print('JUMP riadok nenajdeny')
            print('Chyba funkcie JUMP na riadku', i - 1, 'program nebol skompilovany')
            break
        continue
    elif codeline[0] == 'JUMPT':
        if fns.getVariable(codeline[1]) == 'problem' and not fns.represents_integer(codeline[1]):
            print('Chyba premenna',codeline[1],'pri JUMPT nebola deklarovana')
            break
        if fns.getVariable(codeline[1]):
            if int(fileContent.__len__()) - 1 >= int(codeline[2]) > 0:
                i = int(codeline[2])
            else:
                print('JUMPT riadok nenajdeny')
                print('Chyba funkcie JUMPT na riadku', i - 1, 'program nebol skompilovany')
                break
        continue
    elif codeline[0] == 'JUMPF':
        if fns.getVariable(codeline[1]) == 'problem' and not fns.represents_integer(codeline[1]):
            print('Chyba premenna',codeline[1],'pri JUMPF nebola deklarovana')
            break
        if not fns.getVariable(codeline[1]):
            if int(fileContent.__len__()) - 1 >= int(codeline[2]) > 0:
                i = int(codeline[2])
            else:
                print('JUMPF riadok nenajdeny')
                print('Chyba funkcie JUMPF na riadku', i - 1, 'program nebol skompilovany')
                break
    elif codeline[0] == 'NOP':
        print('')
        continue
    else:
        print('neznama instrukcia na riadku',i-1,'chyba program nebol skompilovany')
        break






