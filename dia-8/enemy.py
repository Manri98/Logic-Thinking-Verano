#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  enemy.py
#   
import random
import pygame


class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
       
def mueve_goomba(e, scroll_x):
	x = random.randint(0,1)
	if x > 0:
		inc = 2
		e.direction = True
	else:
		inc = -2
		e.direction = False
	e.x = scroll_x + 550 + inc

def colision_enemigo(a, b):
	if a.x - b.x < 32 and a.x-b.x > -32 and a.y-b.y < 32 and a.y-b.y > -32:
		print("muerte")
		return True
		


