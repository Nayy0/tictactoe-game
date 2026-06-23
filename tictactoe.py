

####################
#  Tic Tac Toe game
####################

#print the grid with symbols
def print_grid(grille:list[str])->None:
    """
    Precondition : lenght of grille is 9
    """
    
    print(" "+grille[0]+" | "+grille[1]+" | "+grille[2]+ " ")
    print("---+---+---")
    print(" "+grille[3]+" | "+grille[4]+" | "+grille[5]+ " ")
    print("---+---+---")
    print(" "+grille[6]+" | "+grille[7]+" | "+grille[8]+ " ")

#print a numbered grid
def print_grid_numbered()->None:

    print("Positions are numbered like this:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

#return True if 3 symboles are aligned in the grid
def is_won(grille, symbole)->bool:
    """ 
    Precondition : lenght of grille is 9
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
    while comb<len(combinaisons) and not (grille[combinaisons[comb][0]]==grille[combinaisons[comb][1]]==grille[combinaisons[comb][2]]==symbole):
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
def saisie_choix(current_player,current_symbol)->str:
    return input(current_player+" ("+current_symbol+")"+" choisissez une case (1-9) : ")    

#return True if the choice is valid
def est_valide(choix:str)->bool:
    

    return choix.isdigit() and int(choix)>=1 and int(choix)<=9
        
#return True if the square is empty
def est_libre(grille:list[str],position:int):

    return grille[position]==" "

#place the symbole of the player in the grid
def place_choix(current_player,current_symbol,grille):

    choix=saisie_choix(current_player,current_symbol)
    
    while not est_valide(choix):
        print("Entrez invalide. Réessayez.")
        choix=saisie_choix(current_player,current_symbol)
    
    position=int(choix)-1
    
    while not est_libre(grille,position):
        print("Case déjà prise. Réessayez.")        
        choix=saisie_choix(current_player,current_symbol)
        position=int(choix)-1
    
    grille[position]=current_symbol

#return True if the game is a draw
def egalite(grille, symbole):

    return (" " not in grille) and not is_won(grille,symbole)

#Changes the current player. Returns void
def change_joueur(current_symbol :str, player_o:str,player_x:str)->tuple[str]:
    if current_symbol=="X":
        current_symbol="O"
        current_player=player_o
    else:
        current_symbol="X"
        current_player=player_x
    return (current_player,current_symbol)

#print a win message
def affiche_victoire(current_player:str,grille:list[str])->None:
    

    print_grid(grille)
    print("Félicitations, "+current_player+" a remporté la partie !")

#print a draw message
def affiche_egalite(grille:list[str])->None:
    
    print_grid(grille)
    print("Egalité! Il n'y a plus de case")

#the main function
def main()->None:

    # game set up
    grille=[" "]*9
    current_symbol="X"
    print("Hello, welcome in the Tictactoe game !")
    joueurs=pseudo_input()
    player_x=joueurs[0]
    player_o=joueurs[1]
    current_player=player_x
    print_grid_numbered()
    print("\n\n")

    #main loop of the game
    while not is_won(grille,current_symbol) and not egalite(grille,current_symbol):
        print_grid(grille)
        place_choix(current_player,current_symbol,grille)
        if is_won(grille,current_symbol):
            affiche_victoire(current_player,grille)
        elif egalite(grille,current_symbol):
            affiche_egalite(grille)
        else:
            current_player=change_joueur(current_symbol,player_o,player_x)[0]
            current_symbol=change_joueur(current_symbol,player_o,player_x)[1]
    print("Merci d'avoir joué !")
    



if __name__ == '__main__':
    # éxécuté qd ce module n'est pas initialisé par un import.
    main()