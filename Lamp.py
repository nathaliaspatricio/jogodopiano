# -*- coding: utf-8 -*-
"""
@namespace Lamp

    Lamp manipulation


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
from pygame.locals import *
from Image import Image
#start these modules
pygame.init()

class Lamp(Image):
    def __init__(self, fileName, x, y, polygon, lampCursor):
		"""
        Initialize a Image

		    @param self -- the lamp
            @param fileName -- a string that contains the image name 
            @param x -- a horizontal position of lamp
            @param y -- a vertical position of lamp
            @param polygon -- a list of (x,y) pairs
            @param lampCursor -- the lamp cursor
	    
		"""
		
		self.imageSelected = pygame.image.load("image/" + fileName + "Selected.png")
		self.imageSelected.set_alpha(None) # disable alpha.
		self.imageSelected.convert()
		self.imageSelected.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.x = x
		self.y = y
		self.polygon = polygon
		self.isHover = False
		self.isDown = False
		self.isVisible = True
		self.isSelected = False
		self.mouseInside = False
		self.lampCursor = lampCursor
			
    def mouseDown(self):
		"""
        When the mouse is down the Lamp

		    @param self -- the lamp
	    
		"""
		
		self.isDown = True
		self.isSelected = not self.isSelected
		self.lampCursor.setVisible(self.isSelected)

    def draw(self, screen):
		"""
        Draw the Lamp

		    @param self -- the lamp
            @param screen -- the screen where the images will be showed
	    
		"""
		
		if self.isVisible:		
			if self.isSelected:
			    screen.blit(self.imageSelected, (self.x, self.y))
			 
    def getIsSelected(self):
		"""
        Get isSelected

		    @param self -- the lamp

            @return isSelected
	    
		"""
		
		return self.isSelected

    def setLampCursorVisible(self, isVisible):
		"""
        Set the lamp cursor visibility

		    @param self -- the lamp
            @param isVisible -- a boolean that represents the lamp cursor visibility
	    
		"""
		
		self.lampCursor.setVisible(isVisible)
			    
