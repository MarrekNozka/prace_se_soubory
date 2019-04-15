#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:25:24 2019

@author: svo35103
"""
# importy
import random

# options
IGNORE_CHARS = (" ")
HLASKY = ["aeiyou","qwrtpsdfghjklzxcvbnm"]

# prevod na mala pismena, jako vstup string textu
def zmensi(text):
    return text.lower()

# vymena stringu co stringem cim
def nahrad(text, co, cim):
    return text.replace(co, cim)

# vrati slovnik a jako vstup bere string text
def statistika(text):
    statistika = {}
    for znak in text:
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
        typ = random.randint(0, 1) # 1 - samohhlaska, 2 - souhlaska
        delka_slova = random.randint(1, 8)
        for _ in range(delka_slova):
            hlaska = random.choice(HLASKY[typ])
            if not(text):
                hlaska = hlaska.upper()
            text += hlaska
            typ = not(typ)
        text += " "
    return text

# testy                
text = nahodny()
print("TESTY")
print(text)
print(statistika(text))
print(zmensi(text))
print(nahrad(text, "a", "/jahoda/"))

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
    vstup = input(">>> ", end="")
    if vstup == "1":
        nazev = input("Název souboru: ", end="" )
        with open(nazev, "r") as f:
            pass
        