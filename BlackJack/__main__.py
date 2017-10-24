# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:50:13 2017

@author: Isa
"""
import random
from PlayingCard import PlayingCard
from Table import Table 
from Player import Player
from Player import Dealer

def main(args=None):
    dealer = Dealer("hej")
    deck = dealer.loaddeck()
    dealer.printdeck(deck)
    
    for i in range(0,4):
        input("press enter for random hand:" )
        l=[]
        for j in range(0,5):
            l.append(randomcard(deck))
        printhand(l)
    input("press enter to continue")

if __name__ == "__main__":
    main()
    
    