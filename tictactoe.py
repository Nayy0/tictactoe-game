

####################
#  Tic Tac Toe game
####################

#print the grid with symbols
def print_grid(grid:list[str])->None:
    """
    Precondition : lenght of grid is 9
    """
    
    print(" "+grid[0]+" | "+grid[1]+" | "+grid[2]+ " ")
    print("---+---+---")
    print(" "+grid[3]+" | "+grid[4]+" | "+grid[5]+ " ")
    print("---+---+---")
    print(" "+grid[6]+" | "+grid[7]+" | "+grid[8]+ " ")

#print a numbered grid
def print_grid_numbered()->None:

    print("Positions are numbered like this:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

#return True if 3 symboles are aligned in the grid
def is_won(grid, symbole)->bool:
    """ 
    Precondition : lenght of grid is 9
    symbole est "X" ou "O"
    Examples :
    $$$ is_won(["X","X","X","O"," ","O"," ","O"," "],"X")
    True
    $$$ is_won(["X","O","O","X","X","X","O","O","X"],"X")
    True
    $$$ is_won([" ","O","O","X","O"," ","X","X","X"],"X")
    True
    $$$ is_won(["X","O","O","X","O"," ","X"," "," "],"X")
    True
    $$$ is_won(["X","O","O","X","O"," ","X"," "," "],"X")
    True
    $$$ is_won([" ","X","O","X","X"," ","X","X"," "],"X")
    True
    $$$ is_won([" "," "," "," "," "," "," "," "," "],"X")
    False
    """
    combinaisons=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7]\
                  , [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    comb = 0
    while comb<len(combinaisons) and not (grid[combinaisons[comb][0]]==grid[combinaisons[comb][1]]==grid[combinaisons[comb][2]]==symbole):
        comb+=1
    return comb<len(combinaisons)
    

#input the name of the players and return a tuple
def pseudo_input()->tuple[str,str]:

    player_x=input("Entrez le pseudo du joueur X : ")
    player_o=input("Entrez le pseudo du joueur O : ")
    while player_x == player_o:
        print("The pseudo is already used, enter a different one.")
        player_o=input("Enter player 0 's pseudo")
    return (player_x,player_o)

#input function of the choice
def choice_input(current_player,current_symbol)->str:
    return input(current_player+" ("+current_symbol+")"+" chose a square (1-9) : ")    

#return True if the choice is valid
def is_valid(choice:str)->bool:
    
    return choice.isdigit() and int(choice)>=1 and int(choice)<=9
        
#return True if the square is empty
def est_libre(grid:list[str],position:int):

    return grid[position]==" "

#place the symbole of the player in the grid
def place_choice(current_player,current_symbol,grid):

    choice=choice_input(current_player,current_symbol)
    
    while not is_valid(choice):
        print("Input invalid. Try again.")
        choice=choice_input(current_player,current_symbol)
    
    position=int(choice)-1
    
    while not est_libre(grid,position):
        print("Square already taken. Retry.")        
        choice=choice_input(current_player,current_symbol)
        position=int(choice)-1
    
    grid[position]=current_symbol

#return True if the game is a draw
def is_a_draw(grid, symbole):

    return (" " not in grid) and not is_won(grid,symbole)

#Changes the current player. Returns void
def change_current_player(current_symbol :str, player_o:str,player_x:str)->tuple[str]:
    if current_symbol=="X":
        current_symbol="O"
        current_player=player_o
    else:
        current_symbol="X"
        current_player=player_x
    return (current_player,current_symbol)

#print a win message
def print_win_message(current_player:str,grid:list[str])->None:
    

    print_grid(grid)
    print("Congratulations, "+current_player+" won !")

#print a draw message
def print_draw_message(grid:list[str])->None:
    
    print_grid(grid)
    print("Draw! No more squares available.")

#the main function
def main()->None:

    # game set up
    grid=[" "]*9
    current_symbol="X"
    print("Hello, welcome in the Tictactoe game !")
    joueurs=pseudo_input()
    player_x=joueurs[0]
    player_o=joueurs[1]
    current_player=player_x
    print_grid_numbered()
    print("\n\n")

    #main loop of the game
    while not is_won(grid,current_symbol) and not is_a_draw(grid,current_symbol):
        print_grid(grid)
        place_choice(current_player,current_symbol,grid)
        if is_won(grid,current_symbol):
            print_win_message(current_player,grid)
        elif is_a_draw(grid,current_symbol):
            print_draw_message(grid)
        else:
            current_player=change_current_player(current_symbol,player_o,player_x)[0]
            current_symbol=change_current_player(current_symbol,player_o,player_x)[1]
    print("Thank you for playing !")
    



if __name__ == '__main__':
    # éxécuté qd ce module n'est pas initialisé par un import.
    main()