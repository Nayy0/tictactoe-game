# Compléter ici (noms, groupe, contenu fichier, date)
#Benessalah Nayssam
#MI21
#
#
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>


####################
# Jeu du Tic Tac Toe
####################

#Initialisation du jeu

def affiche_grille(grille:list[str])->None:
    """
    Précondition : len(grille)==9
    """
    
    print(" "+grille[0]+" | "+grille[1]+" | "+grille[2]+ " ")
    print("---+---+---")
    print(" "+grille[3]+" | "+grille[4]+" | "+grille[5]+ " ")
    print("---+---+---")
    print(" "+grille[6]+" | "+grille[7]+" | "+grille[8]+ " ")

def affiche_grille_numerote()->None:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print("Les positions sont numérotées ainsi :")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

#Verification de victoire
def est_gagne(grille, symbole)->bool:
    """ Renvoie True ssi 3 symboles sont aligné dans la grille

    Précondition : len(grille)==9
    symbole est "X" ou "O"
    Exemple(s) :
    $$$ est_gagne(["X","X","X","O"," ","O"," ","O"," "],"X")
    True
    $$$ est_gagne(["X","O","O","X","X","X","O","O","X"],"X")
    True
    $$$ est_gagne([" ","O","O","X","O"," ","X","X","X"],"X")
    True
    $$$ est_gagne(["X","O","O","X","O"," ","X"," "," "],"X")
    True
    $$$ est_gagne(["X","O","O","X","O"," ","X"," "," "],"X")
    True
    $$$ est_gagne([" ","X","O","X","X"," ","X","X"," "],"X")
    True
    $$$ est_gagne([" "," "," "," "," "," "," "," "," "],"X")
    False
    """
    combinaisons=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7]\
                  , [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    comb = 0
    while comb<len(combinaisons) and not (grille[combinaisons[comb][0]]==grille[combinaisons[comb][1]]==grille[combinaisons[comb][2]]==symbole):
        comb+=1
    return comb<len(combinaisons)
    

#Fonction de saisie des pseudos
def saisie_pseudo()->tuple[str,str]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    joueur_x=input("Entrez le pseudo du joueur X : ")
    joueur_o=input("Entrez le pseudo du joueur O : ")
    while joueur_x == joueur_o:
        print("Pseudo déjà utilisé, entrez un pseudo différent.")
        joueur_o=input("Entrez le pseudo du joueur O: ")
    return (joueur_x,joueur_o)

#Fonction de saisie des choix
def saisie_choix(joueur_courant,symbole_courant)->str:
    return input(joueur_courant+" ("+symbole_courant+")"+" choisissez une case (1-9) : ")    
            
def est_valide(choix:str)->bool:
    """ renvoie True ssi le choix est valide

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return choix.isdigit() and int(choix)>=1 and int(choix)<=9
        
def est_libre(grille:list[str],position:int):
    """ renvoi True ssi la case n'est pas prise

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return grille[position]==" "


def place_choix(joueur_courant,symbole_courant,grille):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    choix=saisie_choix(joueur_courant,symbole_courant)
    
    while not est_valide(choix):
        print("Entrez invalide. Réessayez.")
        choix=saisie_choix(joueur_courant,symbole_courant)
    
    position=int(choix)-1
    
    while not est_libre(grille,position):
        print("Case déjà prise. Réessayez.")        
        choix=saisie_choix(joueur_courant,symbole_courant)
        position=int(choix)-1
    
    grille[position]=symbole_courant

def egalite(grille, symbole):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return (" " not in grille) and not est_gagne(grille,symbole)

def change_joueur(symbole_courant :str, joueur_o:str,joueur_x:str)->tuple[str]:
    """ Fait le changement de joueur sans rien retourner

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    if symbole_courant=="X":
        symbole_courant="O"
        joueur_courant=joueur_o
    else:
        symbole_courant="X"
        joueur_courant=joueur_x
    return (joueur_courant,symbole_courant)

def affiche_victoire(joueur_courant:str,grille:list[str])->None:
    """ Affiche le message de victoire

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    affiche_grille(grille)
    print("Félicitations, "+joueur_courant+" a remporté la partie !")

def affiche_egalite(grille:list[str])->None:
    """ Affiche le message d'égalité

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    affiche_grille(grille)
    print("Egalité! Il n'y a plus de case")

def main()->None:
    grille=[" "]*9
    symbole_courant="X"
    print("Bonjour, bienvenue dans le jeu du Tictactoe !")
    joueurs=saisie_pseudo()
    joueur_x=joueurs[0]
    joueur_o=joueurs[1]
    joueur_courant=joueur_x
    affiche_grille_numerote()
    
    while not est_gagne(grille,symbole_courant) and not egalite(grille,symbole_courant):
        affiche_grille(grille)
        place_choix(joueur_courant,symbole_courant,grille)
        if est_gagne(grille,symbole_courant):
            affiche_victoire(joueur_courant,grille)
        elif egalite(grille,symbole_courant):
            affiche_egalite(grille)
        else:
            joueur_courant=change_joueur(symbole_courant,joueur_o,joueur_x)[0]
            symbole_courant=change_joueur(symbole_courant,joueur_o,joueur_x)[1]
    print("Merci d'avoir joué !")
    



if __name__ == '__main__':
    # éxécuté qd ce module n'est pas initialisé par un import.
    main()