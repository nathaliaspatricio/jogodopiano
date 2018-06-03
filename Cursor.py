# -*- coding: utf-8 -*-
"""
@namespace Cursor

        Cursor manipulation


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

class Cursor(Image):
    def __init__(self, fileName, x, y, polygon):
		"""
		Initialize a cursor

		    @param self -- the cursor
		    @param fileName -- a string that contains the cursor image name
		    @param x -- a initial horizontal position of cursor image 
		    @param y -- a initial vertical position of cursor image
		    @param polygon -- a list of (x,y) pairs
	    
		"""
		
		self.imageCursor = pygame.image.load("image/" + fileName + "Cursor.png")
		self.imageCursor.set_alpha(None) # disable alpha.
		self.imageCursor.convert()
		self.imageCursor.set_colorkey( ( 255, 0, 255 ) ) # magenta
		self.x = x
		self.y = y
		self.polygon = polygon
		self.isHover = False
		self.isDown = False
		self.isVisible = False
		self.mouseInside = False

    def mouseMove(self, event):
        """
        When mouse moves on the screen

            @param self -- the cursor
            @param event -- a mouse event

        """
		
        self.x = event.pos[0] + 5
        self.y = event.pos[1] + 5
		
    def draw(self, screen):
        """
        Draw a cursor on the screen

    		@param self -- the cursor
            @param screen -- the screen where the images will be showed
	    
		"""
		
        if self.isVisible:		
            screen.blit(self.imageCursor, (self.x, self.y))


