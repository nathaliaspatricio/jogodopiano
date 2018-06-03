# -*- coding: utf-8 -*-
"""
@namespace Sound

    Sound manipulation


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
#start these modules
pygame.init()

class Sound:	
	def setFileName(self, fileName):
		"""
        Initialize a Sound

		    @param self -- the sound
		    @param fileName -- a string that contains the sound name 
	    
		"""
		
		self.fileName = fileName

	def getFileName(self):
		"""
        Get the sound filename

		    @param self -- the sound
		    
		    @return fileName
	    
		"""
		
		return self.fileName

	def play(self):
		"""
        Play the sound

		    @param self -- the sound 
	    
		"""
		
    		#load sound(works with ogg e wav)
    		sound = pygame.mixer.Sound(self.fileName + ".ogg")
			#toca som
    		sound.play()


