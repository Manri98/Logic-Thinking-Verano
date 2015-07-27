#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fireball.py

fireball_speed = 2

class Fireball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def Moverse(lista):
	lista = lista
	for i in range (0, len(lista)):
		lista[i].x += fireball_speed
		lista[i].y	+= fireball_speed
def Dibujar(lista):
	lista = lista
	for i in range (0, len(lista)):	
		screen.blit(fireball,(lista[i].x, lista[i].y))


