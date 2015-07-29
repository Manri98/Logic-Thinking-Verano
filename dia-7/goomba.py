#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  goomba.py
#  

class goomba:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

def mueve_goomba(bola):
	if bola.direction:
		bola.x += 4
	else:
		bola.x -= 4
