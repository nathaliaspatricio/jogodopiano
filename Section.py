# -*- coding: utf-8 -*-
"""
@namespace Section

    Section manipulation


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
from Sound import Sound
#start these modules
pygame.init()

class Section(Sound):
	def __init__(self):
		"""
        Initialize a Section

		    @param self -- the section
	    
		"""
		
		self.keys = []
		self.currentKey = None

	def setKeys(self, keys):
		"""
       Set the keys Section

		    @param self -- the section
            @param keys -- the related keys
	    
		"""
		
		self.keys = keys
		self.currentKey = 0
		
	def play(self):
		"""
        Play the section

		    @param self -- the section
	    
		"""
		
        #load sound(works with ogg e wav)
   		sound = pygame.mixer.Sound(self.fileName + ".wav")
	    #play sound
   		sound.play()

	def isCurrentKey(self, id):
		"""
        Verify if the key is the current key

		    @param self -- the section 
            @param id -- a key index
            
            @return boolean
	    
		"""
		
		if self.keys[self.currentKey] == id:
			return True
		else:
			return False

	def moreThan(self, id):
		"""
        Verify if the key is higher than current key

		    @param self -- the section
            @param id -- a key index
            
            @return boolean
	    
		"""
		
		if self.keys[self.currentKey] < id:
			return True
		else:
			return False
			
	def isLastKey(self): 
		"""
        Verify if the key is the last key

		    @param self -- the secton
	    
	        @return boolean
	    
		"""
		
		if self.currentKey == (len(self.keys) - 1):
			return True
		else:
			return False
	        
