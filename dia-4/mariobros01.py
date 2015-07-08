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

########################################################################
# CONSTANTES
########################################################################
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MARIO_SPEED = 5
TIMER_MARIO = 200



########################################################################
# FUNCIONES
########################################################################




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
	screen.fill((255,255,255)) 
	mario = pygame.image.load("sprites/mario.gif").convert_alpha()
	mario_walk1 = pygame.image.load("sprites/mario-walk1.gif").convert_alpha()
	mario_walk2 = pygame.image.load("sprites/mario-walk2.gif").convert_alpha()
	mario_walk3 = pygame.image.load("sprites/mario-walk3.gif").convert_alpha()


	
	# VARIABLES
	mario_pos_x = 100
	mario_pos_y = 200
	
	# DIBUJAR EN PANTALLA LAS IMÁGENES INICIALES
	screen.blit(mario,(mario_pos_x, mario_pos_y))

	# ACTUALIZAR TODAS LAS IMÁGENES
	pygame.display.flip()
	
	
	# BUCLE PRINCIPAL DEL JUEGO
	while True:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					mario_pos_y -= MARIO_SPEED	
					screen.blit(mario,(mario_pos_x, mario_pos_y))
									
				elif event.key == pygame.K_DOWN:
					mario_pos_y+= MARIO_SPEED	
					screen.blit(mario,(mario_pos_x, mario_pos_y))	
					
				elif event.key == pygame.K_LEFT:
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
					
				elif event.key == pygame.K_RIGHT:
					screen.fill((255,255,255)) 
					screen.blit(mario_walk1,(mario_pos_x, mario_pos_y))
					mario_walk1 = pygame.transform.flip(mario_walk1, True, False)
					pygame.display.update()
					pygame.time.wait(TIMER_MARIO)
					screen.fill((255,255,255)) 
					screen.blit(mario_walk2,(mario_pos_x, mario_pos_y))
					mario_walk2 = pygame.transform.flip(mario_walk2, True, False)
					pygame.display.update()
					pygame.time.wait(TIMER_MARIO)
					screen.fill((255,255,255)) 
					screen.blit(mario_walk3,(mario_pos_x, mario_pos_y))
					mario_walk3 = pygame.transform.flip(mario_walk3, True, False)
					pygame.display.update()
					pygame.time.wait(TIMER_MARIO)
					
		
		screen.fill((255,255,255)) 
		screen.blit(mario,(mario_pos_x, mario_pos_y))	
		pygame.display.update()
		
	
	return 0

if __name__ == '__main__':
	main()
