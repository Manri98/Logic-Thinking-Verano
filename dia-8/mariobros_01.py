#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mariobros_01.py
#  
#  Copyright 2015 Elías <Ozi@FDZ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
########################################################################
# LIBRERÍAS
######################################################################## 
import pygame
import sys
import time
import threading
from fireball import *
from enemy import *
from mario import *

########################################################################
# CONSTANTES
########################################################################
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MARIO_SPEED = 4
TIMER = 10


########################################################################
# FUNCIONES
########################################################################

global scroll_x = 0
global scroll_y = 0


########################################################################
# FUNCIÓN PRINCIPAL DEL JUEGO
########################################################################
def main():
	pygame.init()
	
	# CREAR LA VENTANA DEL JUEGO CON LAS MEDIDAS SCREEN_WIDTH Y 
	# SCREEN_HEIGHT
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# LE PONEMOS TÍTULO A LA VENTANA DEL JUEGO
	pygame.display.set_caption("Mario Bros by Elías")
	
	# CARGA DE IMÁGENES
	fondo = pygame.image.load("fondos/fondo_02.png").convert_alpha()
	mario = pygame.image.load("sprites/mario.png").convert_alpha()
	mario_walk1 = pygame.image.load("sprites/mario-walk1.gif").convert_alpha()
	mario_walk2 = pygame.image.load("sprites/mario-walk2.gif").convert_alpha()
	mario_walk3 = pygame.image.load("sprites/mario-walk3.gif").convert_alpha()
	mario_jump = pygame.image.load("sprites/mario-jump.gif").convert_alpha()
	mario_agachado = pygame.image.load("sprites/mario-duck.gif").convert_alpha()
	mario_fiery = pygame.image.load("sprites/mario-fiery.gif").convert_alpha()
	mario_fireball = pygame.image.load("sprites/mario-fireball.gif").convert_alpha()
	fireball= pygame.image.load("sprites/fireball.gif").convert_alpha()
	goomba= pygame.image.load("sprites/goomba.gif").convert_alpha()

	
	# VARIABLES
	mario_pos_x = 200
	mario_pos_y = 255
	pressed_up = False
	pressed_right = False
	pressed_down = False
	pressed_left = False
	salto = -15
	air = False
	moving = False
	direccion = True
	disparo = False
	fireball_x = mario_pos_x
	fireball_y = mario_pos_y
	L_fireball = []
	enemigo = False
	muertes = 0	

	
	# DIBUJAR EN PANTALLA LAS IMÁGENES INICIALES
	screen.blit(fondo,(scroll_x, 0)) 
	screen.blit(mario,(mario_pos_x, mario_pos_y))
	# ACTUALIZAR TODAS LAS IMÁGENES
	pygame.display.flip()
	

	# BUCLE PRINCIPAL DEL JUEGO
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				moving = True
				if event.key == pygame.K_UP:
					pressed_up = True	
				elif event.key == pygame.K_RIGHT:
					pressed_right = True
				elif event.key == pygame.K_DOWN:
					pressed_down = True	
				elif event.key == pygame.K_LEFT:
					pressed_left = True
				elif event.key == pygame.K_SPACE:
					disparo = True
					fireball_y = mario_pos_y
					fire = Fireball(fireball_x, fireball_y+40, direccion)
					L_fireball.append(fire)
			elif event.type == pygame.KEYUP:
				moving = False
				if event.key == pygame.K_UP:
					pressed_up = False	
				elif event.key == pygame.K_RIGHT:
					pressed_right = False
				elif event.key == pygame.K_DOWN:
					pressed_down = False	
				elif event.key == pygame.K_LEFT:
					pressed_left = False
		
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
					screen.blit(fondo,(scroll_x, 0)) 
					screen.blit(mario_walk1,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER)
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
					screen.blit(fondo,(scroll_x, 0)) 
					screen.blit(mario_walk2,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER)
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
					screen.blit(fondo,(scroll_x, 0)) 
					screen.blit(mario_walk3,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER)
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
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
					screen.blit(fondo,(scroll_x, 0))  
					screen.blit(mario_walk1,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER)
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
					screen.blit(fondo,(scroll_x, 0)) 
					screen.blit(mario_walk2,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER)
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
					screen.blit(fondo,(scroll_x, 0))  
					screen.blit(mario_walk3,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER)
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
			if pressed_down:
				screen.blit(fondo,(scroll_x, 0))  
				screen.blit(mario_agachado,(mario_pos_x, mario_pos_y))
				pygame.display.update()
				pygame.time.wait(TIMER)
			
		
		
		if air:
			if salto <= 15:
				if direccion:
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
				else:
					MueveMario(direccion, air, moving, pressed_up, pressed_right, pressed_down, pressed_left)
				mario_pos_y += salto
				salto += 1
				screen.blit(fondo,(scroll_x, 0))  
				screen.blit(mario_jump,(mario_pos_x, mario_pos_y))
				pygame.display.update()
				
			else:
				salto = -15
				air = False
		
		if disparo:
			if L_fireball:
				for bola in L_fireball:					
					mueve_fireball(bola)
					screen.blit(fondo,(scroll_x, 0)) 
					screen.blit(mario,(mario_pos_x, mario_pos_y))
					screen.blit(fireball,(bola.x, bola.y))
					pygame.display.update()
					if bola.x > SCREEN_WIDTH or bola.x < 0:
						L_fireball.remove(bola)

			else: 
				disparo = False
					
		else:
			screen.blit(fondo,(scroll_x, 0)) 
			screen.blit(mario,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			
		if scroll_x == -300:
			e = Enemy(300,285,False)
			enemigo = True
		
		if enemigo:
			mueve_goomba(e, scroll_x)
			screen.blit(goomba,(e.x, e.y))
			pygame.display.update()
			for bola in L_fireball:
				if colision_enemigo(bola, e):
					enemigo = False
					muertes += 1
					
				
		pygame.font.init()
		fuente = pygame.font.Font(None, 30)
		texto = fuente.render('MUERTES = ' + str(muertes), 1, (255, 0, 0))
		screen.blit(texto, (0, 50))
		pygame.display.flip()
		pygame.time.wait(TIMER)
		
				
	
	return 0


if __name__ == '__main__':
	main()

