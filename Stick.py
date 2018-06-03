# -*- coding: utf-8 -*-
"""
@namespace Stick

    Stick manipulation


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
from Image import Image
#start these modules
pygame.init()

class Stick(Image):
	def __init__(self, fileName, name, x, y, polygon, game):
		"""
        Initialize a Stick

		    @param self -- the stick
		    @param fileName -- a string that contains the image name 
		    @param name -- a string that contains the label text
		    @param x -- a horizontal position of stick 
		    @param y -- a vertical position of stick 
		    @param polygon -- a list of (x,y) pairs
		    @param game -- the game 
	    
		"""
		
		self.image = pygame.image.load("image/stick/stick" + fileName + ".png")
		self.image.set_alpha(None) # disable alpha.
		self.image.convert()
		self.image.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.name = name
		self.fileName = fileName
		self.x = x
		self.y = y
		self.polygon = polygon
		self.game = game
		self.isHover = False
		self.isDown = False
		self.isVisible = True
		self.mouseInside = False

	def mouseHover(self):
		"""
        When the mouse is hover on the Stick

		    @param self -- the stick
	    
		"""
		
		self.isHover = True
		self.game.statusBar.setText(self.name)
		
	def mouseLeave(self):
		"""
        When the mouse leaves the stick

		    @param self -- the stick
	    
		"""
		
		self.isHover = False
		self.game.statusBar.setText("")
		
	def mouseDown(self):
		"""
        When the mouse is down the stick

		    @param self -- the stick
	    
		"""
		
		self.isDown = True
		self.game.selectChallenge(int(self.fileName))
		

	def draw(self, screen):
		"""
        Draw the Stick on the screen

		    @param self -- the stick
		    @param screen -- the screen where the images will be showed 
	    
		"""
		
		if self.isVisible:		
			screen.blit(self.image, (self.x, self.y))

