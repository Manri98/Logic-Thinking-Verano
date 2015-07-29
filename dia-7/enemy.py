#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  enemy.py
#  
#  Copyright 2015 Ozi <Ozi@FDZ>
#  
import random

class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
       
def mueve_goomba(e, scroll_x):
	x = random.randint(0,200)
	if x == 0:
		#e.x = scroll_x + 550
		e.direction = True
		print("derecha")
	else:
		#e.x = scroll_x + 550
		e.direction = False
		print("izquierda")
	if e.direction:
		inc = 2
	else:
		inc= -2

	e.x = scroll_x + 500 + inc
	print(e.x)


