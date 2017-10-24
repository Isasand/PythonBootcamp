# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:57:01 2017

@author: Isa
"""

class Table(object):
    
    def __init__(self,minstake,maxstake, dealer, players = []):
        self._maxstake = maxstake 
        self._minstake = minstake
        self._dealer = dealer
        self._currentlyplaying = players
    def get_max_stake(self):
        return (str(self._maxstake)) + "£"
    
    def get_min_stake(self):
        return (str(self._minstake)) +"£"
    
    def get_dealer(self):
        return self._dealer
    
    def add_players(self,player):
        self._currentlyplaying.append(player)
        
    def get_currently_playing(self):
        return self._currentlyplaying