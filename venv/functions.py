#!/usr/bin/env python

#datova struktura kt. obsahuje definovane premenne
varDict={}

def getVariable(key):
    if not (key in varDict):
        return 'problem'
    return varDict[key]

def read(instruction):
    print("Zadaj hodnotu premennej", instruction[1])
    try:
        varDict[instruction[1]] = int(input())
    except ValueError:
        print("Chyba treba zadat celociselnu konstantu")
        return False
    return True

def write(instruction):
    if instruction[1] in varDict:
        print('Vypis premennej:',instruction[1],'=',varDict[instruction[1]])
        return True
    else:
        print('Chyba vypisu premenna',instruction[1],'nebola deklarovana')
        return False

def represents_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def number_validation(instruction):
    if (not instruction[1] in varDict) and (not represents_integer(instruction[1])) or (
            not instruction[2] in varDict) and (not represents_integer(instruction[2])):
        print('Chyba pri matematickej operacii, jedna z premennych nebola deklarovana')
        return True
    return False

def addition(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) + int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) + int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) + int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) + int(varDict[instruction[2]])
        return True

def subtraction(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) - int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) - int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) - int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) - int(varDict[instruction[2]])
        return True

def multiplication(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) * int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) * int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) * int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) * int(varDict[instruction[2]])
        return True

def smaller_than(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) < int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) < int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) < int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) < int(varDict[instruction[2]])
        return True

def greater_than(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) > int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) > int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) > int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) > int(varDict[instruction[2]])
        return True

def greater_or_equal_than(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) >= int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) >= varDict[instruction[1]]
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) >= int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) >= int(varDict[instruction[2]])
        return True

def smaller_or_equal_than(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) <= int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) <= int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) <= int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) <= int(varDict[instruction[2]])
        return True

def equal_to(instruction):
    if number_validation(instruction):
        return False
    else:
        if represents_integer(instruction[1]) and represents_integer(instruction[2]):
            varDict[instruction[3]] = int(instruction[1]) == int(instruction[2])
        elif represents_integer(instruction[1]):
            varDict[instruction[3]] = int(instruction[1]) == int(varDict[instruction[1]])
        elif represents_integer(instruction[2]):
            varDict[instruction[3]] = int(varDict[instruction[1]]) == int(instruction[2])
        else:
            varDict[instruction[3]] = int(varDict[instruction[1]]) == varDict[instruction[2]]
        return True

def assign(instruction):
    if not represents_integer(instruction[2]) and not instruction[2] in varDict:
        print('Chyba ! Premenna',instruction[2],'nebola deklarovana alebo nie je prirodzenym cislo')
        return False
    if represents_integer(instruction[2]):
        varDict[instruction[1]] = int(instruction[2])
    else:
        varDict[instruction[1]] = int(varDict[instruction[2]])
    return True