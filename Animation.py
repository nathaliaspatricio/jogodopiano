# -*- coding: utf-8 -*-
"""
@namespace Animation

        Stones Animation


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
import time
#start these modules
pygame.init()

class Animation():
    def __init__(self, stones, keys, helps, ball, rightBall, bar, game):
		"""
        Initialize the animation

    		@param self -- the animation
            @param stones -- the stones
            @param keys -- the related keys
            @param helps -- the related helps
            @param ball -- the left ball
            @param rightBall -- the right ball
            @param bar -- the grey bar
            @param game -- the game
	    
		"""
		
		self.stones = stones
		self.keys = keys
		self.helps = helps
		self.ball = ball
		self.rightBall = rightBall
		self.bar = bar
		self.game = game
    
    def playIntroduction(self):
		"""
        Play the animation introduction

            @param self -- the animation

		"""
		
		i = 0
		while i != 15:
		    if i < len(self.keys):
			    self.stones[i].setVisible(True)
			    self.stones[i].setSound(self.keys[i])
			    self.stones[i].setButton(self.game.buttons[(self.keys[i] - 1)])
			    self.stones[i].setHelp(self.game.helps[(self.helps[i])])
		    else:
			    self.stones[i].setVisible(False)
		    i = i + 1
		self.ball.setVisible(True)
		self.bar.setVisible(True)
		self.rightBall.setVisible(True)
    
    def lowStone(self, id):
		"""
        Low a determined stone

    		@param self -- the animation
            @param id -- a stone index

		"""
		
		self.stones[id].setVisible(False)
    
    def playClosing(self):
		"""
        Play the animation closing

	        @param self -- the animation

		"""
		
		self.stones[len(self.keys) - 1].setVisible(False)
		self.ball.setVisible(False)
		self.bar.setVisible(False)
		self.rightBall.setVisible(False)	
