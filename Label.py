# -*- coding: utf-8 -*-
"""
@namespace Label

    Label manipulation


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

class Label(Image):
	def __init__(self, x, y, polygon):
		"""
        Initialize a Image

		    @param self -- the label
            @param x -- a horizontal position of image 
            @param y -- a vertical position of image 
            @param polygon -- a list of (x,y) pairs
	    
		"""
		
		self.x = x
		self.y = y
		self.isHover = False
		self.isDown = False
		self.isVisible = True
		self.mouseInside = False
		self.polygon = polygon
		self.setText("")
	
	def setText(self, text):
		"""
        Set a Text on the label

		    @param self -- the label
            @param text -- a text that it will be showed in the label
	    
		"""
		
		self.text = text
		if (pygame.font):
	    		font = pygame.font.Font(None, 24)
	    		self.message = font.render(self.text, True, (0, 0, 0 ))
		
	def draw(self, screen):
		"""
       Draw a label on the screen

		    @param self -- the label
            @param screen -- the screen where the images will be showed
	    
		"""
		
		screen.blit(self.message, (self.x, self.y))
