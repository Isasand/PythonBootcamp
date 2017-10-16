
# coding: utf-8

# In[517]:


from IPython.display import clear_output

#global variables
board =[" "]*10
game_state = True
position = 0
player = {"Player one": [True, "X"], "Player two": [False, "O"]}
number_of_tries = 0
invalid_input = True
not_empty_position = True


# In[518]:


def clear_game():
    global board,game_state,position, number_of_tries
    board = [" "] * 10
    game_state = True
    position = 0
    number_of_tries = 0
    invalid_input = True


# In[519]:


def print_board():
    global board
    print("x-->")
    print("y |"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("| |"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("V |"+board[6]+"|"+board[7]+"|"+board[8]+"|")
    


# In[520]:


def take_input():
    global position, invalid_input, number_of_tries
    invalid_input = True
    while(invalid_input):
        position = int(input("Input player position: "))
        check_input()
    


# In[521]:


def place_player():
    global board, position, player
    if player["Player one"][0]:
        board[position-1] = player["Player one"][1]
    elif player["Player two"][0]:
        board[position-1] = player["Player two"][1]


# In[522]:


def switch_player():
    global player
    if player["Player one"][0]:
        player["Player one"][0] = False
        player["Player two"][0] = True
    else:
        player["Player one"][0] = True
        player["Player two"][0] = False


# In[523]:


def ask_to_play_again():
    global game_state
    ans = input("Want to play again (y/n)? ")
    if ans == "Y" or ans == "y":
        game_state = True
        clear_game()
        clear_output(wait=False)
    else:
        game_state = False
    return game_state


# In[524]:


def check_input():
    global position, invalid_input
    if position > 10 or position < 0:
        print("Invalid position, input number between 1-9")
        invalid_input = True
    else:
        if check_if_position_is_empty():
            print("Position is not empty, try again:")
            invalid_input= True
        else:
            invalid_input = False
                
    return invalid_input


# In[525]:


def check_if_position_is_empty():
    global board, position, not_empty_position
    not_empty_position = True
    if board[position-1] == " ":
        not_empty_position = False
    else:
        not_empty_position = True
    return not_empty_position


# In[527]:


def clear_cell():
    clear_output(wait = True)


# In[529]:


while (game_state):
    clear_cell()
    take_input()
    place_player()
    print_board()
    switch_player()
    number_of_tries += 1
    if number_of_tries == 9:
        ask_to_play_again()
    


# ###### 
