#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
import sys
import random
import re


try:
    palabra = sys.argv[1].lower().split()
    caracter = ['>', '!', '#', '$', '%', '&', '<', '/', '@', '(', ')', '=', '{', '?', '|', '*', '+', '^', '[', ']', ':', '~', '.', '}', '-', '_',';']
    letras = ['a', 'b' , 'c' , 'd' , 'e' , 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for validate in palabra:
        if not re.match("^[a-z-ñ]*$", validate):
            print("[Error!] Solo puede ingresar las letras del alfabeto en español!")
            sys.exit()

    for letra in letras:
        numCaracteres = len(caracter)
        numRandom = random.randrange(numCaracteres)
        caracterRandom = caracter[numRandom].encode('utf-8')
        #print(f'LETRA: {letra} | CARACTER: {caracterRandom.decode("utf-8")} | NCAR: {len(caracter)}')
        palabra = [sub.replace(letra, caracterRandom.decode("utf-8")) for sub in palabra ]
        caracter.pop(numRandom)
    print('  '.join(palabra))
except IndexError:
    print('Al ejecutar el programa debe acompañarlo con la palabra que desee cifrar y si es una frase coloquela entre comillas dobles (") ')

#Contact: snd.pedraza93@gmail.com