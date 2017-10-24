# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:57:01 2017

@author: Isa
"""

class Table(object):
    
    def __init__(self,maxstake,minstake, dealer):
        self._maxstake = maxstake 
        self._minstake = minstake
        self._dealer = dealer
        
    def get_max_stake(self):
        return self._maxstake
    
    def get_min_stake(self):
        return self._minstake
    
    