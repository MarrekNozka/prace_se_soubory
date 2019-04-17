#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:25:24 2019

@author: svo35103
"""
# importy
import random

# options
IGNORE_CHARS = (" \n")
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
    for slovo in range(pocet):
        typ = random.randint(0, 1) # 0 - samohhlaska, 1 - souhlaska
        delka_slova = random.randint(1, 8)
        for _ in range(delka_slova):
            hlaska = random.choice(HLASKY[typ])
            if not(text):
                hlaska = hlaska.upper()
            text += hlaska
            typ = not(typ)
        if slovo % 10 == 0:
            text += "\n"
        else:
            text += " "

    return text

# uloz list textu
def uloz(soubor, text):
    with open(soubor, "w") as f:
        for line in text:
            f.write(line)

# vypise slovnik jako tabulku
def vypis(slovnik):
    mx = max(slovnik.values())
    koeficient = 20 / mx
    print("{:<8} {:<8}".format('Znak','Pocet'))
    for item in slovnik:
        mrizky = round(koeficient * slovnik[item]) * "#"
        print("{:<8} {:<8} {:<20}".format(item,slovnik[item], mrizky))

# programy
# 1 zmensi
def jedna():
    nazev = input("Nazev souboru: ")
    novy_soubor = []
    with open(nazev, "r") as f:
        line = f.readline()
        while line:
            novy_soubor.append(zmensi(line))
            line = f.readline()
        uloz(nazev, novy_soubor)
        print("Soubor {0} uspesne ulozen! ".format(nazev))

# 2 nahradi
def dva():
    nazev = input("Nazev souboru: ")
    co = input("Jake slovo: ")
    cim = input("Jakym slovem: ")
    novy_soubor = []
    with open(nazev, "r") as f:
        line = f.readline()
        while line:
            novy_soubor.append(nahrad(line, co, cim))
            line = f.readline()
        uloz(nazev, novy_soubor)
        print("Soubor {0} uspesne ulozen! ".format(nazev))

# 3 statistika
def tri():
    nazev = input("Nazev souboru: ")
    with open(nazev, "r") as f:
        stat = {}
        line = f.readline()
        while line:
            stat = statistika(line, stat)
            line = f.readline()
        vypis(stat)
# 4 nahodny text
def ctyri():
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
===============================================================================
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌            ▐░▌ ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌        ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░░░░░░░░░░░▌    ▐░▌         ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌        ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀
     ▐░▌     ▐░▌            ▐░▌ ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░▌     ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀
===============================================================================

    1) Převod na malá písmena
    2) Nahrazení znaků
    3) Statistika souboru
    4) Generování náhodného textu
    5) Konec
      """)

def main():
    while True:
        try:
            vstup = int(input(">>> "))
        except ValueError:
            print("Neplatna moznost! ")
            continue
        if vstup == 1 or vstup == 2:
            try:
                if vstup == 1:
                    jedna()
                else:
                    dva()
            except FileNotFoundError:
                print("Soubor nenalezen! ")
                continue
    
        elif vstup == 3:
            try:
                tri()
            except FileNotFoundError:
                print("Soubor nenalezen! ")
                continue
    
        elif vstup == 4:
            ctyri()
    
        elif vstup == 5:
            exit(0)
    
        else:
            print("Neplatna moznost! ")

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\rTahle teda ne! Pro vypnuti použijte pětku! :C ")
