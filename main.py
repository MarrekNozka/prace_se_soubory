#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:25:24 2019

@author: svo35103
"""
# importy
import random
import os

# options
IGNORE_CHARS = (" ")
HLASKY = ["aeiyou","qwrtpsdfghjklzxcvbnm"]

# prevod na mala pismena, jako vstup string textu
def zmensi(text):
    return text.lower()

# vymena stringu co stringem cim
def nahrad(text, co, cim):
    return text.replace(co, cim)

# vrati slovnik a jako vstup bere string text a slovnik predchozi statistiky, popripade prazdny
def statistika(text, statistika={}):
    for znak in text:
        znak = znak.upper()
        if znak in IGNORE_CHARS:
            continue
        if znak in statistika:
            statistika[znak] += 1
        else:
            statistika[znak] = 1
    return statistika

# nahodny text, jako vstup pocet slov, pokud 0 tak nahodny pocet slov do 100
def nahodny(pocet=0):
    if pocet == 0:
        pocet = random.randint(1, 100)
    try:
        pocet = int(pocet)
    except ValueError:
        return ""
    text = ""
    for _ in range(pocet):
        typ = random.randint(0, 1) # 0 - samohhlaska, 1 - souhlaska
        delka_slova = random.randint(1, 8)
        for _ in range(delka_slova):
            hlaska = random.choice(HLASKY[typ])
            if not(text):
                hlaska = hlaska.upper()
            text += hlaska
            typ = not(typ)
        text += " "
    return text

# uloz list textu
def uloz(soubor, text):
    with open(soubor, "w") as f:
        for line in text:
            f.write(line)
            
# vypise slovnik jako tabulku
def vypis(slovnik):
    print("{:<8} {:<8}".format('Znak','Pocet'))
    for item in slovnik:
        print("{:<8} {:<8}".format(item,slovnik[item]))
        
# testy 
"""               
text = nahodny()
print("TESTY")
print(text)
print(statistika(text))
print(zmensi(text))
print(nahrad(text, "a", "/jahoda/"))
"""
# menu

print(
      """
    1) Převod na malá písmena
    2) Nahrazení znaků
    3) Statistika souboru 
    4) Generování náhodného textu
    5) Konec
      """)


while True:
    try:
        vstup = int(input(">>> "))
    except ValueError:
        print("Neplatna moznost! ")
        continue
    if vstup in range(1,3):
        try:
            nazev = input("Nazev souboru: ")
            if vstup == 2:
                co = input("Jake slovo: ")
                cim = input("Jakym slovem: ")
            novy_soubor = []
            with open(nazev, "r") as f:
                line = f.readline()
                while line:
                    if vstup == 1:
                        novy_soubor.append(zmensi(line))
                    elif vstup == 2:
                        novy_soubor.append(nahrad(line, co, cim))
                    line = f.readline()
                uloz(nazev, novy_soubor)
                print("Soubor {0} uspesne ulozen! ".format(nazev))
        except FileNotFoundError:
            print("Soubor nenalezen! ")
            continue
        
    elif vstup == 3:
        try:
            nazev = input("Nazev souboru: ")
            with open(nazev, "r") as f:
                stat = {}
                line = f.readline()
                while line:
                    stat = statistika(line, stat)
                    line = f.readline()
                vypis(stat)
        except FileNotFoundError:
            print("Soubor nenalezen! ")
            continue
        
    elif vstup == 4:
        nazev = input("Nazev souboru i s priponou: ")
        while True:
            try:
                pocet = int(input("Pocet nahodnych slov: "))
                break
            except ValueError:
                continue
        with open(nazev, "w") as f:
            f.write(nahodny(pocet))
        print("Soubor {0} uspesne ulozen! ".format(nazev))

    elif vstup == 5:
        exit(0)
        
    else: 
        print("Neplatna moznost! ")
        