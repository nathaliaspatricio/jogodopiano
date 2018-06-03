# -*- coding: utf-8 -*-
"""
@namespace Game

        Game manipulation


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
import sys, pygame
#start these modules
pygame.init()

class Game:      
    def __init__(self):
        """
        Initialize the game

		    @param self -- the game
	    
		"""
		
        self.challenges = []
        self.helps = []
        self.currentChallenge = None
        self.points = 0
        self.bufferPoints = 0
        self.help = 0
		
    def addChallenge(self, challenge):
        """
        Add a challenge

		    @param self -- the game
            @param challenge -- a challenge
	    
		"""
		
        self.challenges += [challenge]
	
    def selectChallenge(self, id):
        """
        Select a challenge

		    @param self -- the game
            @param id -- a challenge index
	    
		"""
		
        if self.currentChallenge == None:
            self.currentChallenge = self.challenges[id - 1]
            self.currentChallenge.start()
        else:
            lastBall = self.currentChallenge.getBall()
            lastBall.setVisible(False)
            self.currentChallenge = self.challenges[id - 1]
            self.currentChallenge.change()
		
    def attempt(self, id):
        """
        Write a message

		    @param self -- the game 
            @param id -- a key index
	    
		"""
		
        if self.currentChallenge != None:
            message = self.currentChallenge.attempt(id)
	
    def lampIsSelected(self):
        """
        Return if the lamp is selected

		    @param self -- the game

            @return self.lamp.getIsSelected()
	    
		"""
		
        return self.lamp.getIsSelected()
		
    def setLampCursorVisible(self, isVisible):
        """
        Set the lamp cursor visibility

    		@param self -- the game 
            @param isVisible -- a boolean that represents the lamp cursor visibility
	    
		"""
		
        self.lamp.setLampCursorVisible(isVisible)
    
    def setEarCursorVisible(self, isVisible):
        """
        Set the ear cursor visibility

    		@param self -- the game
            @param isVisible -- a boolean that represents the ear cursor visibility
	    
		"""
		
        self.earCursor.setVisible(isVisible)

    def setButtons(self, buttons, helps):
        """
        Set the buttons

    		@param self -- the game
            @param buttons -- the buttons
            @param helps -- the helps
	    
		"""
		
        self.buttons = buttons
        self.earCursor = buttons[54]
        self.lamp = buttons[55]
        self.statusBar = buttons[56]
        self.statusBarRight = buttons[57]
        self.helps = helps
		
    def setHelp(self):

        """
        Set the help

    		@param self -- the game 
	    
		"""
        self.help = True
	
    def setPoints(self, level, attempts):
        """
        Set Points

    		@param self -- the game
            @param level -- the challenge level
            @param attempts -- the number of attempts
	    
		"""
		
        if level == "easy":
            self.points = self.points + self.bufferPoints + 20
            self.bufferPoints = 0
        elif level == "difficult":
            self.points = self.points + self.bufferPoints + 40
            self.bufferPoints = 0
        self.statusBarRight.setText("Points: " + str(self.points))
	    
    def setBufferPoints(self, level, attempts): 
        """
        Set the buffer points

    		@param self -- the game
            @param level -- the challenge level
            @param attempts -- the number of attempts
	    
		"""
		
        if level == "easy":
            if self.lampIsSelected() and self.help:
                if attempts == 0:
                    self.bufferPoints = self.bufferPoints + 5
                elif attempts == 1:
                    self.bufferPoints = self.bufferPoints + 4
                elif attempts == 2:
                    self.bufferPoints = self.bufferPoints + 3
                elif attempts == 3:
                    self.bufferPoints = self.bufferPoints + 2
                elif attempts >= 4:
                    self.bufferPoints = self.bufferPoints + 1
            else:
                if attempts == 0:
                    self.bufferPoints = self.bufferPoints + 10
                elif attempts == 1:
                    self.bufferPoints = self.bufferPoints + 8
                elif attempts == 2:
                    self.bufferPoints = self.bufferPoints + 6
                elif attempts == 3:
                    self.bufferPoints = self.bufferPoints + 4
                elif attempts >= 4:
                    self.bufferPoints = self.bufferPoints + 2

        elif level == "difficult":
            if self.lampIsSelected() and self.help:
                if attempts == 0:
                    self.bufferPoints = self.bufferPoints + 10
                elif attempts == 1:
                    self.bufferPoints = self.bufferPoints + 8
                elif attempts == 2:
                    self.bufferPoints = self.bufferPoints + 6
                elif attempts == 3:
                    self.bufferPoints = self.bufferPoints + 4
                elif attempts >= 4:
                    self.bufferPoints = self.bufferPoints + 2
            else:
                if attempts == 0:
                    self.bufferPoints = self.bufferPoints + 20
                elif attempts == 1:
                    self.bufferPoints = self.bufferPoints + 16
                elif attempts == 2:
                    self.bufferPoints = self.bufferPoints + 12
                elif attempts == 3:
                    self.bufferPoints = self.bufferPoints + 8
                elif attempts >= 4:
                    self.bufferPoints = self.bufferPoints + 4
            
