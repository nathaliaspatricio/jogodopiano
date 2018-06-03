# -*- coding: utf-8 -*-
"""
@namespace Image

    Image class


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
#start these modules
pygame.init()

class Image:
	def __init__(self, fileName, x, y, polygon):
		"""
        Initialize a Image

		    @param self -- the image 
            @param fileName -- a string that contains the image name 
            @param x -- a horizontal position of image 
            @param y -- a vertical position of image 
            @param polygon -- a list of (x,y) pairs
	    
		"""
		
		self.image = pygame.image.load(fileName + ".png")
		image.set_alpha(None) # disable alpha.
		self.imageHover = pygame.image.load(fileName + "Hover.png")
		imageHover.set_alpha(None) # disable alpha.
		self.imageDown = pygame.image.load(fileName + "Down.png")
		self.imageDown.set_alpha(None) # disable alpha.
		self.x = x
		self.y = y
		self.polygon = polygon
		self.isHover = False
		self.isDown = False
		self.isVisible = True
		self.mouseInside = False

	def mouseHover(self):
		"""
        When the mouse is hover on the image

		    @param self -- the image
	    
		"""
		
		self.isHover = True

	def mouseLeave(self):
		"""
        When the mouse leaves the Image

		    @param self -- the image
	    
		"""
		
		self.isHover = False
	
	def mouseDown(self):
		"""
        When the mouse is down the Image

		    @param self -- the image
	    
		"""
		
		self.isDown = True

	def mouseUp(self):
		"""
        When the mouse is up the Image

		    @param self -- the image
	    
		"""
		
		self.isDown = False
		
	def mouseMove(self, event):
		"""
        When the mouse moves in the Image

		    @param self -- the image
            @param event -- a mouse event
            
            @return None
	    
		"""
		
		return

	def isMouseInside(self, position):
		"""
        Determine if a point is inside a given polygon or not

		    @param self -- the image
            @param position -- a list of (x,y) pair
            
            @return inside
	    
		"""
		
		x = position[0]
		y = position[1]
		
		n = len(self.polygon)
		inside = False

		p1x,p1y = self.polygon[0]
		for i in range(n+1):
			p2x,p2y = self.polygon[i % n]
			if y > min(p1y,p2y):
				if y <= max(p1y,p2y):
					if x <= max(p1x,p2x):
						if p1y != p2y:
							xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
						if p1x == p2x or x <= xinters:
							inside = not inside
			p1x,p1y = p2x,p2y

		return inside


	def isMouseInsideChanged(self, position):
		"""
        When the inside changed

		    @param self -- the image
            @param position -- a list of (x,y) pair
            
            @return boolean
	    
		"""
		
		isMouseInsideTemp = self.isMouseInside(position)
		
		if self.mouseInside != isMouseInsideTemp:
			self.mouseInside = isMouseInsideTemp	
			return True
		else:
			return False


	def parseEvent(self, event):
		"""
        Treat the mouse event

		    @param self -- the image
            @param event -- a mouse event
	    
		"""
		
		if self.isVisible:
			if event.type == MOUSEMOTION:
				if self.isMouseInsideChanged(event.pos):
					if self.mouseInside:
						self.mouseHover()
					else:
						self.mouseLeave()
				self.mouseMove(event)
			elif (event.type == MOUSEBUTTONDOWN) and (self.mouseInside):
					self.mouseDown()
			elif (event.type == MOUSEBUTTONUP) and (self.isDown):
					self.mouseUp()
			
	
	def draw(self, screen):
		"""
        Draw a Image on the screen

		    @param self -- the image
            @param screen -- the screen where the images will be showed
	    
		"""
		
		if self.isVisible:		
			if self.isDown:
			 	screen.blit(self.imageDown, (self.x, self.y))
			elif self.isHover:
			 	screen.blit(self.imageHover, (self.x, self.y))
			#else:
				#screen.blit(self.image, (self.x, self.y))

	def setVisible(self, isVisible):
		"""
        Set the Image visibility

		    @param self -- the image
            @param isVisible -- a boolean that it indicates that the image is visible
	    
		"""
		
		self.isVisible = isVisible
		
