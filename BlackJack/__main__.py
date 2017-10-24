# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:50:13 2017

@author: Isa
"""
from Table import Table 
from Player import Player
from Player import Dealer
import time

import os

clear = lambda: os.system('cls')

def welcome():
    print("Welcome to my black jack game!")
    
def menu():
    return "Start by choosing in the menu\n1. Show the rules\n2. Start the game\n3. Exit program\nInput choice:"

def print_rules():
    f = open('rules.txt', 'r')
    content = f.read()
    print(content)
    input("OK<ENTER")
    f.close()

def choose_number_of_players(table):
    n = int(input("How many players? (1-3):"))
    for i in range(0,n):
        table.add_players(Player())
        name = input("Name of player {}:".format(i+1))
        table.get_player_nr(i).set_name(name)

def playgame():
    dealer = Dealer()
    table = Table(1,400,dealer)
    deck = (table.get_dealer().loaddeck())
    
    choose_number_of_players(table)
    input("START GAME (enter)")
    count = 0
    
    for player in table.get_currently_playing():
        for i in range(0,2):
            clear()
            table.print_properties()
            if count >= 1:
                print("Player {} cards:".format(count))
                table.get_player_nr(count-1).printhand()
            print("Player {} cards:".format(count+1))
            dealer.deal_card(table.get_player_nr(count), deck, table, i)
            player.printhand()
            time.sleep(1)
        count+=1
        
def main(args=None):
    programon = True
    while programon:
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
        elif choice == 2:
            clear()
            playgame()
            input("BACK<ENTER>")
        elif choice == 3:
            clear()
            print("Closing program...")
            time.sleep(0.5)
            programon = False
        else:
            print("Try a valid choice")
            time.sleep(0.5)
    
    '''for i in range(0,4):
        input("press enter for random hand:" )
        l=[]
        for j in range(0,5):
            l.append(randomcard(deck))
        printhand(l)'''
    #input("press enter to continue")

if __name__ == "__main__":
    main()
    
    