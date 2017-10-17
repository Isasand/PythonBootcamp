# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

# In[1]:
import os

# global variables
board = [" "] * 10
game_state = True
position = 0
player = {"Player one": [True, "X"], "Player two": [False, "O"]}
number_of_tries = 0
invalid_input = True
not_empty_position = True


# In[2]:


def clear_game():
    global board, game_state, position, number_of_tries, invalid_input
    board = [" "] * 10
    game_state = True
    position = 0
    number_of_tries = 0
    invalid_input = True


# In[3]:
def print_board():
    global board
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

# In[]
def print_currently_playing():
    global player
    for key in player.items():
        if key[1][0]:
            print("Playing right now: ", key[0])

# In[]
def check_input():
    global position, invalid_input
    if position > 10 or position < 0:
        print("Invalid position, input number between 1-9")
        invalid_input = True
    else:
        if check_if_position_is_empty():
            print("Position is not empty, try again:")
            invalid_input = True
        else:
            invalid_input = False
    return invalid_input

# In[25]:

def take_input():
    global position, invalid_input, number_of_tries, player
    invalid_input = True
    while (invalid_input):
        print_currently_playing()
        position = int(input("Input player position: "))
        check_input()

# In[9]:


def place_player():
    global board, position, player
    if player["Player one"][0]:
        board[position - 1] = player["Player one"][1]
    elif player["Player two"][0]:
        board[position - 1] = player["Player two"][1]


# In[10]:


def switch_player():
    global player
    if player["Player one"][0]:
        player["Player one"][0] = False
        player["Player two"][0] = True
    else:
        player["Player one"][0] = True
        player["Player two"][0] = False


# In[11]:


def ask_to_play_again():
    global game_state
    ans = input("Want to play again (y/n)? ")
    if ans == "Y" or ans == "y":
        game_state = True
        clear_game()
    else:
        game_state = False
    return game_state


# In[12]:


def check_if_position_is_empty():
    global board, position, not_empty_position
    not_empty_position = True
    if board[position - 1] == " ":
        not_empty_position = False
    else:
        not_empty_position = True
    return not_empty_position


# In[16]:


def check_if_winner():
    global board, player
    for key in player.items():
        if (board[0] == key[1][1] and board[1] == key[1][1] and board[2] == key[1][1]) or (
                    board[3] == key[1][1] and board[4] == key[1][1] and board[5] == key[1][1]) or (
                    board[6] == key[1][1] and board[7] == key[1][1] and board[8] == key[1][1]) or (
                    board[0] == key[1][1] and board[3] == key[1][1] and board[6] == key[1][1]) or (
                    board[1] == key[1][1] and board[4] == key[1][1] and board[7] == key[1][1]) or (
                    board[2] == key[1][1] and board[5] == key[1][1] and board[8] == key[1][1]) or (
                    board[0] == key[1][1] and board[4] == key[1][1] and board[8] == key[1][1]) or (
                    board[2] == key[1][1] and board[4] == key[1][1] and board[6] == key[1][1]):
            clear()
            print_board()
            print("***", key[0], " is the winner***")
            
            ask_to_play_again()
            

# In[]
clear = lambda: os.system('cls')

# In[ ]:
clear_game()
while (game_state):
    print_board()
    take_input()
    place_player()
    check_if_winner()
    switch_player()
    number_of_tries += 1
    if number_of_tries == 9:
        ask_to_play_again()
    clear()
    
