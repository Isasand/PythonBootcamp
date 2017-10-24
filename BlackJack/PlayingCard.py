# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:37:33 2017

@author: Isa
"""
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
        lines[1]=('│{}{}     │'.format(cardtype, space)) 
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
