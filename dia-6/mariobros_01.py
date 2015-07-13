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
#  
import pygame
import sys
import threading

#######################################################################
# VARIABLES GLOBALES
#######################################################################



#######################################################################
#CONSTANTES
#######################################################################
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 480
GRAVEDAD = 10
TIMER_MARIO = 70
SUELO = 380

#######################################################################
# FUNCIONES
#######################################################################

"""" False izquierda
     True derecha
     si comprobarMovimiento coincide con ultimoMovimiento --> MovimientoNormal()
     si no --> MovimientoConGiro()
"""
comprobarMovimiento = True
ultimoMovimiento = True

def DireccionMario():
	if event.key == pygame.K_RIGHT:
		comprobarMovimiento = True
	if event.key == pygame.K_RIGHT:
		comprobarMovimiento = False
		
	return comprobarMovimiento


def Gravedad(y, i): 
		y += i
		return y
		
		

	



def main():
	pygame.init()
	
	# CREAMOS LA VENTANA DEL JUEGO Y LE PONEMOS TÍTULO
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Mario Bros by Elías")
	
	fondo_01 = pygame.image.load("sprites/fondo_01.jpg") 
	mario = pygame.image.load("sprites/mario.gif").convert_alpha()
	mario_walk1 = pygame.image.load("sprites/mario-walk1.gif").convert_alpha()
	mario_walk2 = pygame.image.load("sprites/mario-walk2.gif").convert_alpha()
	mario_walk3 = pygame.image.load("sprites/mario-walk3.gif").convert_alpha()
	mario_jump1 = pygame.image.load("sprites/mario-jump1.gif").convert_alpha()
	
	pressed_up = False
	pressed_down = False
	pressed_right = False
	pressed_left = False

	mario_speed = 6
	mario_pos_x = 100
	mario_pos_y = 200
	
	screen.fill((255,255,255)) 
	#	screen.blit(fondo_01, (0, 0))
	screen.blit(mario,(mario_pos_x, mario_pos_y))
	pygame.display.flip()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					pressed_up = True

					
				if event.key == pygame.K_RIGHT:
					pressed_right = True
					
				if event.key == pygame.K_DOWN:
					pressed_down = True
					
				if event.key == pygame.K_LEFT:
					screen.fill((255,255,255)) 
					screen.blit(mario_walk1,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER_MARIO)
					screen.fill((255,255,255)) 
					screen.blit(mario_walk2,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER_MARIO)
					screen.fill((255,255,255)) 
					screen.blit(mario_walk3,(mario_pos_x, mario_pos_y))
					pygame.display.update()
					pygame.time.wait(TIMER_MARIO)
					pressed_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					pressed_up = False
				if event.key == pygame.K_RIGHT:
					pressed_right = False
				if event.key == pygame.K_DOWN:
					pressed_down = False
				if event.key == pygame.K_LEFT:
					pressed_left = False

		# EJERCICIO 1: HAZ QUE MARIO SE MUEVA, SEGÚN SI LAS FLECHAS ESTÁN
		# PULSADAS (pressed_up, pressed_right...)
		if pressed_up:
			a = -15
			b = 15 
			for i in range(a, b):
				mario_pos_y += i
				screen.fill((255,255,255)) 
				screen.blit(mario_jump1,(mario_pos_x, mario_pos_y))
				pygame.display.update()
				pygame.time.wait(TIMER_MARIO)
		if pressed_down:
			mario_pos_y += mario_speed	
		if pressed_left:
			mario_pos_x -= mario_speed
			screen.fill((255,255,255)) 
			screen.blit(mario_walk1,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			pygame.time.wait(TIMER_MARIO)
			mario_pos_x -= mario_speed
			screen.fill((255,255,255)) 
			screen.blit(mario_walk2,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			mario_pos_x -= mario_speed
			pygame.time.wait(TIMER_MARIO)
			screen.fill((255,255,255)) 
			screen.blit(mario_walk3,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			mario_pos_x -= mario_speed
			pygame.time.wait(TIMER_MARIO)
		if pressed_right:
			mario_pos_x += mario_speed		
			screen.fill((255,255,255)) 
			screen.blit(mario_walk1,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			pygame.time.wait(TIMER_MARIO)
			mario_pos_x += mario_speed
			screen.fill((255,255,255)) 
			screen.blit(mario_walk2,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			mario_pos_x += mario_speed
			pygame.time.wait(TIMER_MARIO)
			screen.fill((255,255,255)) 
			screen.blit(mario_walk3,(mario_pos_x, mario_pos_y))
			pygame.display.update()
			mario_pos_x += mario_speed
			pygame.time.wait(TIMER_MARIO)
		
		
		
		#EJERCICIO 2: PROGRAMA LA GRAVEDAD PARA QUE MARIO CAIGA HASTA y=380
		while mario_pos_y >= SUELO:
			mario_pos_y = mario_pos_y - GRAVEDAD
			
			
			
			
		screen.fill((255,255,255)) 	
		screen.blit(mario,(mario_pos_x, mario_pos_y))		
		pygame.display.flip()
				
	
	return 0

if __name__ == '__main__':
	main()

