# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:50:13 2017

@author: Isa
"""
import random


class PlayingCard(object):

    def __init__(self,cardtype,suit,value):
        self._suit = suit
        self._value = value
        self._cardtype = cardtype
        
    def get_suit(self):
        return self._suit
    
    def get_value(self):
        return self._value
    
    def get_cardtype(self):
        return self._cardtype
    
    def print_card(self):
        print(self._cardtype, ",", self._suit, ",", self._value)
    
    
    def format_suit_for_visual_output(self):
        if self._suit == 'club':
            return '♣'
        elif self._suit == 'spade':
            return '♠'
        elif self._suit == 'heart':
            return '♥'
        elif self._suit == 'diamond':
            return '♦'
    
    def format_type_for_visual_output(self):
        if self._cardtype == 'ace':
            return 'A'
        elif self._cardtype == 'jack':
            return 'J'
        elif self._cardtype == 'queen':
            return 'Q'
        elif self._cardtype == 'king':
            return 'K'
        else:
            return self._value
        
    def create_visual_card(self):
        suit = self.format_suit_for_visual_output()
        cardtype = self.format_type_for_visual_output()
        if not self._cardtype == 'ten':
            space = '   '
        else:
            space = '  '
            
        lines =[" "]*9
        lines[0]=('┌─────────┐')
        lines[1]=('│{}{}     │'.format(cardtype, space)) # use two {} one for char, one for space or char
        lines[2]=('│         │')
        lines[3]=('│         │')
        lines[4]=('│    {}    │'.format(suit))
        lines[5]=('│         │')
        lines[6]=('│         │')
        lines[7]=('│     {}{}│'.format(space, cardtype))
        lines[8]=('└─────────┘')
       # for line in lines:
        #    print(line)
        return lines


def printdeck(deck):
    print("Card in deck (type, suit, value):")
    for card in deck:
        card.print_card()
   

def printhand(cards):
    
    lns =[]
    for card in cards:
        lns.append(card.create_visual_card())
        
    hand = [" "]*9
    count = 0
    for line in lns:
        if count < 4:  
            hand[0]+=line[0]
            hand[1]+=line[1]
            hand[2]+=line[2]
            hand[3]+=line[3]
            hand[4]+=line[4]
            hand[5]+=line[5]
            hand[6]+=line[6]
            hand[7]+=line[7]
            hand[8]+=line[8]
            count+=1
    
    print("Printing card(s):")
    for card in hand:
        print(card)

def randomcard(deck):
    return random.choice(deck)    
    
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

count = 0

printdeck(deck)
while count < 5:
    input("press enter for random hand:" )
    l=[]
    for i in range(0,5):
        l.append(randomcard(deck))
    printhand(l)
    count += 1
input("press enter to continue")