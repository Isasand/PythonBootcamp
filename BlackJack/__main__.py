# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:50:13 2017

@author: Isa
"""
from Table import Table 
from Player import Player
from Player import Dealer
import os
import time


clear = lambda: os.system('cls')

def welcome():
    print("Welcome to my black jack game!")
    
def menu():
    return "Start by choosing in the menu\n1. Show the rules\n2. Start the game\n3. Exit program\nInput choice:"

def print_rules():
        print("RULES:\n\nEach player starts by placing a bet in the boxes in front of them."
              "\nThe size of the bet is chosen by selecting a marker of the amount you want to bet."
              "\nThe minimum and maximum bet is shown on the table."
              "\n\nStart of round:\nEach player gets two open cards, at the same time the dealer recieves"
              " an open card \n(European) or two open cards (Atlantic City)."
              "\n\nEach turn: \nYou can ask for a card to increase the value of your hand."
              "\nAfter you've taken the required number of cards, the dealer will complete his hand."
              "\nThe goal is to get a better hand than the dealer, \nit should be higher without the total value exceeding 21."
              "\n\nYou can win if the dealer hand is bigger than 21, you'll be 'bust' if you get over 21 \n(being bust means losing your bet!)"
              "\n\nCards:\nA king, queen or jack is worth 10. \nAce is either one or eleven."
              "\nWhen an ace is valued at 11, the higher total is called a 'soft' total. \nPlayer with a"
              " 'soft' hand can either take a card or double without the risk of being bust."
              "\n\nBlack jack:\nBlack jack = one ace + one card worth ten (ten, jack, queen, king)."
              "\nBlack jack must be your first two cards and the hand is unbeatable, \nhowever"
              " it could end even if the dealer also gets black jack."
              "\n\nOptions available after drawn card:"
              "\nSplit, double, give up or stay."
              "\n\nIf you try to do any of the following, the program will issue a warning"
              "\nand ask you to double check if your action was aware:"
              "\n*Take card if total value of hand is 17 or higher" 
              "\n*Stay if total value of hand is 11 or below"
              "\n*Double if total value of hand is 12 or higher")
     
        
def playgame():
    dealer = Dealer()
    table = Table(1,400,dealer)
    deck = (table.get_dealer().loaddeck())
    
    n = int(input("How many players? (1-3):"))
    for i in range(0,n):
        table.add_players(Player())
        
    print(table.get_currently_playing())
    
    print("Min stake: {}\nMax stake: {}".format(table.get_min_stake(), table.get_max_stake()))
    
    
def main(args=None):
    gameon = True
    while gameon:
        clear()
        welcome()
        while True:
            try: 
                clear()
                choice = int(input(menu()))
            except:
                print("Try a valid choice")
                time.sleep(0.5)
                continue
            else:
                break
        
        if choice == 1:
            clear()
            print_rules()
            input("BACK<ENTER>")
        elif choice == 2:
            clear()
            playgame()
            input("BACK<ENTER>")
        elif choice == 3:
            clear()
            print("Closing program...")
            time.sleep(0.5)
            gameon = False
        else:
            print("input valid command")
    
    '''for i in range(0,4):
        input("press enter for random hand:" )
        l=[]
        for j in range(0,5):
            l.append(randomcard(deck))
        printhand(l)'''
    #input("press enter to continue")



    
if __name__ == "__main__":
    main()
    
    