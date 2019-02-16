#!/usr/bin/env python

#datova struktura kt. obsahuje definovane premenne
varDict={}

def read(instruction):
    print("Zadaj hodnotu premennej", instruction[1])
    varDict[instruction[1]] = input()
    print(varDict)
    return varDict[instruction[1]]
