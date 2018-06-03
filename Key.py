# -*- coding: utf-8 -*-
"""
@namespace Key

    Key manipulation


Copyright 2007, NATE-LSI-EPUSP

Piano Game is developed in Brazil at Escola Politécnica of 
Universidade de São Paulo. NATE is part of LSI (Integrable
Systems Laboratory) and stands for Learning, Work and Entertainment
Research Group. Visit our web page: 
www.lsi.usp.br/nate
Suggestions, bugs and doubts, please email sautchuk@lsi.usp.br

Piano Game is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation version 2 of 
the License.

Piano Game is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with Oficina; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, 
Boston, MA  02110-1301  USA.
The copy of the GNU General Public License is found in the 
COPYING file included in the source distribution.


Author:
Nathalia Sautchuk Patrício          (nathalia.sautchuk@gmail.com)

Group Manager:
Irene Karaguilla Ficheman           (irene@lsi.usp.br)

Cientific Coordinator:
Roseli de Deus Lopes                (roseli@lsi.usp.br)

"""

#import the pygame modules package and Piano Game archives
import sys, pygame
import os.path
from Sound import Sound
from Image import Image
#start these modules
pygame.init()

class Key(Image):
	def __init__(self, fileName, x, y, polygon, game):
		"""
        Initialize a Key

		    @param self -- the key 
            @param fileName -- a string that contains the image name 
            @param x -- a horizontal position of key 
            @param y -- a vertical position of key 
            @param polygon -- a list of (x,y) pairs
            @param game -- the game
	    
		"""
		
		self.image = pygame.image.load("image/key/" + fileName + ".png")
		self.image.set_alpha(None) # disable alpha.
		self.image.convert()
		self.image.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.imageHover = pygame.image.load("image/keyHover/" + fileName + ".png")
		self.imageHover.set_alpha(None) # disable alpha.
		self.imageHover.convert()
		self.imageHover.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.imageDown = pygame.image.load("image/keyDown/" + fileName + ".png")
		self.imageDown.set_alpha(None) # disable alpha.
		self.imageDown.convert()
		self.imageDown.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.id = int(fileName)
		self.fileName = fileName
		self.sound = Sound()
		self.sound.setFileName("sound/notes/T" +str(int(fileName) + 3))
		self.x = x
		self.y = y
		self.polygon = polygon
		self.isHover = False
		self.isDown = False
		self.isVisible = True
		self.mouseInside = False
		self.game = game

	def mouseHover(self):
		"""
        When the mouse is hover on the Key

		    @param self -- the key
	    
		"""
		
		self.isHover = True
		if os.path.exists("sound/notes/T" +str(self.id + 3) + ".ogg"):
		    self.sound.play()
		
	def mouseDown(self):
		"""
        When the mouse is down the Key

		    @param self -- the key
	    
		"""
		
		self.isDown = True
		if os.path.exists("sound/notes/T" +str(self.id + 3) + ".ogg"):
		    self.sound.play()
		    self.game.attempt(self.id)
		    		
