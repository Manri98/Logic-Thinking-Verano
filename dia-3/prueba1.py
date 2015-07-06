#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prueba1.py
#  
#  Copyright 2015 Carlos Manrique Enguita <cmanriqueenguita@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

###LIBRERÍAS
import pygame
from pygame.locals import *

###CONSTANTES
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Prueba de pygame")
	
	##Carga de imágenes
	fondo = pygame.image.load("fondo.jpg").convert()
	tux = pygame.image.load("tux.png").convert_alpha()
    
    ##Colocamos imagenes
	screen.blit(fondo, (0, 0))
	screen.blit(tux, (550, 200))
	
	##Aplicamos cambios
	pygame.display.flip()
	a = raw_input("")
	return 0

if __name__ == '__main__':
	main()

