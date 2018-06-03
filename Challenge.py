# -*- coding: utf-8 -*-
"""
@namespace Challenge

        Challenge manipulation


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
import os.path
from Section import Section
from Sound import Sound
from Animation import Animation
from gettext import gettext as _
#start these modules
pygame.init()

class Challenge:
    def __init__(self, fileName, keys, stick, stones, helps, ball, bar, rightBall, level, game):
        """
        Initialize a challenge

	        @param self -- the challenge
            @param fileName -- a string that contains the sound name 
            @param keys -- the key vector
            @param stick -- the stick
            @param stones -- the stones
            @param helps -- the helps
            @param ball -- the left ball that it is used in the animation
            @param bar -- the grey bar that it is used in the animation
            @param rightBall -- the right ball that it is used in the animation
            @param level -- the challenge level
            @param game -- the game
	    
		"""
		
        self.fileName = fileName
        self.music = Sound()
        self.music.setFileName("sound/music/" + fileName)
        self.section = Section()
        self.section.setFileName("sound/section/" + fileName)
        self.section.setKeys(keys)
        self.stick = stick
        self.animation = Animation(stones, keys, helps, ball, rightBall, bar, game)
        self.ball = ball
        self.level = level
        self.attempts = 0
        self.game = game
    
    def start(self):
        """
        Start a challenge

    		@param self -- the challenge
	    
		"""
        
        if os.path.exists("sound/section/" + self.fileName + ".wav"):
            self.section.play()
            self.game.statusBar.setText(_("Discover the next musical note"))
            self.animation.playIntroduction()
            self.ball.setSound(self.fileName)
            
    def change(self):
        """
        Change a challenge

    		@param self -- the challenge
	    
		"""
        if os.path.exists("sound/section/" + self.fileName + ".wav"):
            self.section.play()
            self.game.statusBar.setText(_("Discover the next musical note"))
            self.animation.playIntroduction()
            self.ball.setSound(self.fileName)
			
    def finish(self):
        """
        Finish a challenge

    		@param self -- the challenge
	    
		"""
		
        if os.path.exists("sound/music/" + self.fileName + ".ogg"):
            self.music.play()
        self.game.currentChallenge = None
        self.game.statusBar.setText(_("Congratulations!!! You completed the challenge! Choose other to continue playing."))
        self.stick.setVisible(False)
        self.animation.playClosing()
        self.game.setPoints(self.level, self.attempts)
			
    def attempt(self, id):
        """
        Verify a attempt

    		@param self -- the challenge
            @param id -- the key index
	    
		"""
		
        if self.section.isCurrentKey(id):
        	self.game.setBufferPoints(self.level, self.attempts)
        	self.attempts = 0 
        	if self.section.isLastKey():
        		self.finish()
        	else:		
        		self.animation.lowStone(self.section.currentKey)
        		self.section.currentKey = self.section.currentKey + 1
        		self.game.statusBar.setText(_("Discover the next musical note"))
        else:
            self.attempts = self.attempts + 1
            if self.section.moreThan(id):
        	    self.game.statusBar.setText(_("Try a lower note"))
            else:
        	    self.game.statusBar.setText(_("Try a higher note"))
        	    
    def getBall(self):
        """
        Get the ball

    		@param self -- the challenge
	    
	    """
        return self.ball

