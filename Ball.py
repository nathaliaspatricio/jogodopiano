# -*- coding: utf-8 -*-
"""
@namespace Ball

        Ball class


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

#import the pygame modules package
import pygame
from pygame.locals import *
import os.path
from Image import Image
from Section import Section
#start these modules
pygame.init()

class Ball(Image):
	def __init__(self, fileName, x, y, polygon, game):
		"""
        Initialize a ball

            @param self -- the ball
            @param fileName -- a string that contains the image name 
            @param x -- a horizontal position of ball
            @param y -- a vertical position of ball
            @param polygon -- a list of (x,y) pairs	
            @param game -- the game
	    
		"""
		
		self.image = pygame.image.load("image/animation/" + fileName + ".png")
		self.image.set_alpha(None) # disable alpha.
		self.image.convert()
		self.image.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.x = x
		self.y = y
		self.polygon = polygon
		self.isHover = False
		self.isDown = False
		self.isVisible = False
		self.mouseInside = False
		self.currentBall = None
		self.game = game
		
	def setSound(self, sectionFileName):
		"""
        Set a sound ball

    		@param self -- the ball
            @param sectionFileName -- a related section filename  
	    
		"""
		self.sectionFileName = sectionFileName
		self.section = Section()
		self.section.setFileName("sound/section/" + sectionFileName)

	def mouseHover(self):
		"""
        When the mouse is hover on the ball

            @param self -- the ball

        """

		self.isHover = True
		self.game.setEarCursorVisible(True)
		if self.game.lampIsSelected():
		    self.game.setLampCursorVisible(False)
		if os.path.exists("sound/section/" + self.sectionFileName + ".wav"):
		    self.section.play()

	def mouseLeave(self):
		"""
		When the mouse leaves the ball

            @param self -- the ball 

		"""
		
		self.isHover = False
		self.game.setEarCursorVisible(False)
		if self.game.lampIsSelected():
		    self.game.setLampCursorVisible(True)
		
	def draw(self, screen):
		"""
		Draw the ball

            @param self -- the ball
            @param screen -- the screen where the images will be showed
	    
		"""
		
		if self.isVisible:		
		 	screen.blit(self.image, (self.x, self.y))
			
