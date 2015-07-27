#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fireball.py
#  

class Fireball:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

def mueve_fireball(bola):
	if bola.direction:
		bola.x += 4
	else:
		bola.x -= 4

