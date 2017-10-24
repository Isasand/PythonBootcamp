# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:01:08 2017

@author: Isa
"""
from PlayingCard import PlayingCard

class Player(object):
    
    def __init__(self, money, hand =[]):
        self._money = money
        self._hand = hand
    
    def get_hand(self):
        return self._hand
    
    def add_card_to_hand(self, card):
        self._hand.append(card)
    
class Dealer(Player):
    
    def __init__(self, hand=[]):
        Player.__init__(self,money=0,hand=[])
        self._hand = hand
    
    def tell_rules(self):
        print("RULES:\n\nEach player starts by placing a bet in the boxes in front of them."
              " The size of the bet is chosen by selecting a marker of the amount you want to bet."
              " The minimum and maximum bet is shown on the table."
              "\n\nStart of round:\nEach player gets two open cards, at the same time the dealer recieves"
              " an open card (European) or two open cards (Atlantic City)."
              "\n\nEach turn: \nYou can ask for a card to increase the value of your hand."
              " After you've taken the required number of cards, the dealer will complete his hand."
              "\nThe goal is to get a better hand than the dealer, it should be higher without the total value exceeding 21."
              "\n\nYou can win if the dealer hand is bigger than 21, you'll be 'bust' if you get over 21 (being bust means losing your bet!)"
              "\n\nCards:\nA king, queen or jack is worth 10. Ace is either one or eleven."
              " When an ace is valued at 11, the higher total is called a 'soft' total. Player with a"
              " 'soft' hand can either take a card or double without the risk of being bust."
              "\n\nBlack jack:\nBlack jack = one ace + one card worth ten (ten, jack, queen, king)."
              "\nBlack jack must be your first two cards and the hand is unbeatable, however"
              " it could end even if the dealer also gets black jack."
              "\n\nOptions available after drawn card:"
              "\nSplit, double, give up or stay."
              "\n\nIf you try to do any of the following, the program will issue a warning"
              " and ask you to double check if your action was aware:"
              "\nTake card if total value of hand is 17 or higher" 
              "\nStay if total value of hand is 11 or below"
              "\nDouble if total value of hand is 12 or higher")
     
        

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
   

    def printhand(self, cards):
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

    def randomcard(self,deck):
        return random.choice(deck)    

    def deal_cards(self,players, deck):
        for player in players:
            randomcard(deck)
            player.add_card_to_hand()
            
            