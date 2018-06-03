# -*- coding: utf-8 -*-
"""
@namespace Stone

    Stone manipulation


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
from Image import Image
from Sound import Sound
#start these modules
pygame.init()

class Stone(Image):
	def __init__(self, fileName, x, y, polygon, game):
		"""
        Initialize a Stone

		    @param self -- the stone
		    @param fileName -- a string that contains the image name 
		    @param x -- a horizontal position of stone 
		    @param y -- a vertical position of stone 
		    @param polygon -- a list of (x,y) pairs
		    @param game -- the game
	    
		"""
		
		self.image = pygame.image.load("image/" + fileName + ".png")
		self.image.set_alpha(None) # disable alpha.
		self.image.convert()
		self.image.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.fileName = fileName
		self.x = x
		self.y = y
		self.polygon = polygon
		self.game = game
		self.isHover = False
		self.isDown = False
		self.isVisible = False
		self.mouseInside = False
		
	def setSound(self, id):
		"""
        Set a stone sound

		    @param self -- the stone
		    @param id -- a number that represents the ball note
	    
		"""
		
		self.id = id
		self.sound = Sound()
		self.sound.setFileName("sound/notes/T" +str(self.id + 3))

	def mouseHover(self):
		"""
        When the mouse is hover on the stone

		    @param self -- the stone
	    
		"""
		
		self.isHover = True
		self.game.setEarCursorVisible(True)
		self.game.setHelp()
		if self.game.lampIsSelected():
		    self.game.setLampCursorVisible(False)
		    self.button.mouseHover()
		    self.help.setVisible(True)
		else:
		    if os.path.exists("sound/notes/T" +str(self.id + 3) + ".ogg"):
		    	self.sound.play()
		
	def mouseLeave(self):
		"""
        When the mouse leaves the stone

		    @param self -- the stone
	    
		"""
		
		self.isHover = False
		self.game.setEarCursorVisible(False)
		if self.game.lampIsSelected():
		    self.game.setLampCursorVisible(True)
		    self.button.mouseLeave()
		    self.help.setVisible(False)
	
	def draw(self, screen):
		"""
        Draw the stone on the screen

		    @param self -- the stone
		    @param screen -- the screen where the images will be showed
	    
		"""
		
		if self.isVisible:		
			screen.blit(self.image, (self.x, self.y))

	def setButton(self, button):
		"""
        Set a related button

		    @param self -- the stone
		    @param button -- it relates a button with the stone 
	    
		"""
		
		self.button = button
		
	def setHelp(self, help):
		"""
        Set a related help

		    @param self -- the stone
		    @param help -- it relates a help with the stone 
	    
		"""
		
		self.help = help
						
