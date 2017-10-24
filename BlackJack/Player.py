# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:01:08 2017

@author: Isa
"""
from PlayingCard import PlayingCard
import random
import time
import os

clear = lambda: os.system('cls')

class Player(object):
    
    def __init__(self, name = " ", money = 0):
        self._name = name
        self._money = money
        self._hand = []
        self._visualhand = [" "]*9
    
    def set_name(self,name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def get_hand(self):
        return self._hand
    
    def add_card_to_hand(self, card):
        self._hand.append(card)
        
    def printhand(self):
        lns =[]
        lns.clear()
        self._visualhand.clear()
        self._visualhand = [" "]*9
        for card in self._hand:
            lns.append(card.create_visual_card())
        
        count = 0
        for line in lns:
            if count < 4:  
                self._visualhand[0]+=line[0]
                self._visualhand[1]+=line[1]
                self._visualhand[2]+=line[2]
                self._visualhand[3]+=line[3]
                self._visualhand[4]+=line[4]
                self._visualhand[5]+=line[5]
                self._visualhand[6]+=line[6]
                self._visualhand[7]+=line[7]
                self._visualhand[8]+=line[8]
                count+=1
    
        #print("Printing card(s):")
        for card in self._visualhand:
            print(card)
    
    #TODO#sum all values, try for ace and sum both with 1/11, check both for !>21 and return the biggest if both are under
    '''def get_total_value(self):
        if not len(self._hand) == 0:
            for card in hand:
                if card.get_cardtype() == 'ace':
                    
         '''           
                
        
        
class Dealer(Player):
    #def __init__(self, hand=[]):
     #   Player.__init__(self,money=0,hand=[])
        
        
    def loaddeck(self):
        deck = [PlayingCard('ace', 'club', '1/11'), PlayingCard('ace', 'diamond', '1/11'), 
                PlayingCard('ace', 'heart', '1/11'), PlayingCard('ace', 'spade', '1/11'),
                PlayingCard('two', 'club', 2), PlayingCard('two', 'diamond', 2),
                PlayingCard('two', 'heart', 2), PlayingCard('two', 'spade', 2),
                PlayingCard('three', 'club', 3), PlayingCard('hree', 'diamond',3),
                PlayingCard('three', 'heart', 3), PlayingCard('three', 'spade', 3),
                PlayingCard('four', 'club', 4), PlayingCard('four', 'diamond', 4),
                PlayingCard('four', 'heart', 4), PlayingCard('two', 'spade', 4),
                PlayingCard('five', 'club', 5), PlayingCard('five', 'diamond', 5),
                PlayingCard('five', 'heart', 5), PlayingCard('five', 'spade', 5),
                PlayingCard('six', 'club', 6), PlayingCard('six', 'diamond', 6), 
                PlayingCard('six', 'heart', 6), PlayingCard('six', 'spade', 6), 
                PlayingCard('seven', 'club', 7), PlayingCard('seven', 'diamond', 7), 
                PlayingCard('seven', 'heart', 7), PlayingCard('seven', 'spade', 2), 
                PlayingCard('eight', 'club', 8), PlayingCard('eight', 'diamond', 8), 
                PlayingCard('eight', 'heart', 8), PlayingCard('eight', 'spade', 8),
                PlayingCard('nine', 'club', 9), PlayingCard('nine', 'diamond', 9),
                PlayingCard('nine', 'heart', 9), PlayingCard('nine', 'spade', 9),
                PlayingCard('ten', 'club', 10), PlayingCard('ten', 'diamond', 10), 
                PlayingCard('ten', 'heart', 10), PlayingCard('ten', 'spade', 10), 
                PlayingCard('jack', 'club', 10), PlayingCard('jack', 'diamond', 10),
                PlayingCard('jack', 'heart', 10), PlayingCard('jack', 'spade', 10), 
                PlayingCard('queen', 'club', 10), PlayingCard('queen', 'diamond', 10), 
                PlayingCard('queen', 'heart', 10), PlayingCard('queen', 'spade', 10), 
                PlayingCard('king', 'club', 10), PlayingCard('king', 'diamond', 10),
                PlayingCard('king', 'heart', 10), PlayingCard('king', 'spade', 10)]
        return deck

    def printdeck(self,deck):
        print("Card in deck (type, suit, value):")
        for card in deck:
            card.print_card()

    def randomcard(self,deck):
        return random.choice(deck)    

    def deal_card(self,player, deck, table, n):
        while True:
            card = self.randomcard(deck)
            if card not in (table.get_cards_on_table()):
                player.add_card_to_hand(card)
                table.add_card_to_table(card)
                print("Dealing card number {}...".format(n+1))
                break
            else:
                continue