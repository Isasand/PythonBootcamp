# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:57:01 2017

@author: Isa
"""

class Table(object):
    
    def __init__(self,minstake,maxstake, dealer, players = [], cards = []):
        self._maxstake = maxstake 
        self._minstake = minstake
        self._dealer = dealer
        self._currentlyplaying = players
        self._cardsontable = cards 
        
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

    def get_player_nr(self, n):
        return self._currentlyplaying[n]
    
    def print_properties(self):
        print("Min stake: {} Max stake: {}".format(self.get_min_stake(), self.get_max_stake()))
        print("Players at table:")
        for player in self._currentlyplaying:
            print(player.get_name())
        print("\n")
            
    def get_cards_on_table(self):
        return self._cardsontable
        
    def add_card_to_table(self, card):
        self._cardsontable.append(card)
        