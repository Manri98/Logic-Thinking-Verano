#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mario.py
# 

import pygame

scroll_x = 0
scroll_y = 0
MARIO_SPEED = 4

mario = pygame.image.load("sprites/mario.png").convert_alpha()
mario_walk1 = pygame.image.load("sprites/mario-walk1.gif").convert_alpha()
mario_walk2 = pygame.image.load("sprites/mario-walk2.gif").convert_alpha()
mario_walk3 = pygame.image.load("sprites/mario-walk3.gif").convert_alpha()
mario_jump = pygame.image.load("sprites/mario-jump.gif").convert_alpha()
mario_agachado = pygame.image.load("sprites/mario-duck.gif").convert_alpha()
mario_fiery = pygame.image.load("sprites/mario-fiery.gif").convert_alpha()
mario_fireball = pygame.image.load("sprites/mario-fireball.gif").convert_alpha()

class Mario:
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction
		
def MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left):
	global scroll_x
	global scroll_y
		
	if moving:
		if pressed_up:
			air = True
		if pressed_right:
			
			if not direccion:
				mario = pygame.transform.flip(mario, True, False)
				mario_walk1 = pygame.transform.flip(mario_walk1, True, False)
				mario_walk2 = pygame.transform.flip(mario_walk2, True, False)
				mario_walk3 = pygame.transform.flip(mario_walk3, True, False)
				mario_jump = pygame.transform.flip(mario_jump, True, False)
				mario_agachado = pygame.transform.flip(mario_agachado, True, False)
				mario_fiery = pygame.transform.flip(mario_fiery, True, False)
				mario_fireball = pygame.transform.flip(mario_fireball, True, False)
				direccion = True
			if not air:
				scroll_x -= MARIO_SPEED

		if pressed_left and scroll_x <= -1:
			if direccion:
				mario = pygame.transform.flip(mario, True, False)
				mario_walk1 = pygame.transform.flip(mario_walk1, True, False)
				mario_walk2 = pygame.transform.flip(mario_walk2, True, False)
				mario_walk3 = pygame.transform.flip(mario_walk3, True, False)
				mario_jump = pygame.transform.flip(mario_jump, True, False)
				mario_agachado = pygame.transform.flip(mario_agachado, True, False)
				mario_fiery = pygame.transform.flip(mario_fiery, True, False)
				mario_fireball = pygame.transform.flip(mario_fireball, True, False)
				direccion = False
				
			if not air:
				scroll_x += MARIO_SPEED

			
	if air:
			if direccion:
				scroll_x -= MARIO_SPEED
			else:
				scroll_x += MARIO_SPEED

		

