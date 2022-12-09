import math
import os
import time
import cutie
from random import randint
from art import *
from block import Block_list


def clean_console():
    os.system('cls')
    return 1


def convertion_matrice(ligne_matrice):  # Fonction permettant la convertion d'une matrice en chaine de caractère
    chaine_liste = ""
    for i in range(len(ligne_matrice)):
        chaine_liste += str(ligne_matrice[i])
    return chaine_liste  # F


def cercle(dimension):
    file_cercle = open("cercle.txt", "w")
    # plateau = [[0 for j in range(0, dimension)] for i in range(0, dimension)]
    for i in range(dimension):
        for j in range(dimension):
            if math.sqrt((i - dimension // 2) ** 2 + (j - dimension // 2) ** 2) <= dimension // 2 + 1:
                file_cercle.write("1")
            else:
                file_cercle.write("0")
        if i < dimension + 1:
            file_cercle.write("\n")


def losange(dimension):
    file_losange = open("losange.txt", "w")
    plateau = [[0 for _ in range(0, dimension)] for _ in range(0, dimension)]
    compt = 0
    millieu = (dimension // 2)
    for i in range(dimension // 2):
        for j in range(millieu - compt, millieu + compt + 1):
            plateau[i][j] = 1
        compt += 1
    for i in range(dimension // 2, dimension):
        for j in range(millieu - compt, millieu + compt + 1):
            plateau[i][j] = 1
        compt -= 1
    for lignes in plateau:
        file_losange.write(convertion_matrice(lignes) + '\n')
    file_losange.close()
    return 1


def triangle(dimension):  # Besoin des var dimension_l
    file_triangle = open("triangle.txt", "w")
    plateau = [[0 for _ in range(0, dimension)] for _ in range(0, dimension)]
    compt = 0
    millieu = (dimension // 2)
    for i in range(dimension // 2):
        for j in range(millieu - compt, millieu + compt + 1):
            plateau[i][j] = 1
        compt += 1
    for b in range(dimension // 2 + 1):
        plateau.pop()
    for lignes in plateau:
        file_triangle.write(convertion_matrice(lignes) + '\n')

    file_triangle.close()
    return 1


# FONCTIONS GRID #
def read_grid(path: str):
    file_path = open(path, "r")
    file_read = file_path.readlines()
    file_path.close()
    grid = []
    for lignes in file_read:
        ligne = lignes.replace("\n", "")
        ligne_a_ajouter = []
        for nombre in ligne:
            ligne_a_ajouter.append(nombre)
        grid.append(ligne_a_ajouter)
    return grid


def print_grid(grid, dimension):
    # Affichage du cadre avec la grille
    alphabet_min = "abcdefghijklmnopqrstuvwxyz"
    alphabet_maj = alphabet_min.upper()
    print("", end="    ")
    for i in range(dimension):
        print(alphabet_min[i], end=" ")
    print("")

    for i in range(dimension * 2 + 3):  # 3 étant lespacement de la gird
        if i == 0:
            print("  ╔", end="")
        elif i == (dimension * 2) + 2:
            print("╗", end="")
        else:
            print("═", end="")
    print("")
    i = 0
    for lignes in grid:
        print(alphabet_maj[i], end=" ")
        print("║", end=" ")
        for nombre in lignes:
            if nombre == '0':
                print(" ", end=" ")
            elif nombre == '1':
                print("•", end=" ")
            elif nombre == "2":
                print("■", end=" ")
        print("║")
        i += 1
    for i in range(dimension * 2 + 3):
        if i == 0:
            print("  ╚", end="")
        elif i == (dimension * 2) + 2:
            print("╝", end="")
        else:
            print("═", end="")
    print("")



def save_grid(path: str, grid):
    save_file = open(path, "w")
    for lignes in grid:
        ligne = ""
        for nombres in lignes:
            ligne += nombres
        ligne += '\n'
        save_file.write(ligne)


# FONCTIONS BLOCS
def block_dispo(forme_plateau):
    liste_blocks_dispo = []
    ajout_commum = []
    ajout_forme = []
    if forme_plateau == 'triangle':
        matched_block_index = (47, 56)
    elif forme_plateau == 'losange':
        matched_block_index = (33, 46)
    else:
        matched_block_index = (20, 32)
    for i in range(0, 20):

        ajout_commum.append(Block_list[i])
    for i in range(matched_block_index[0], matched_block_index[1] + 1):
        ajout_forme.append(Block_list[i])

    liste_blocks_dispo.append(ajout_commum)
    liste_blocks_dispo.append(ajout_forme)
    return liste_blocks_dispo


def print_block(forme_plateau,cpt):
        # affichage des blocs communs
    liste=block_dispo(forme_plateau)
    compt=0
    nb_espace=len(liste[0][0])*2+2
    print(nb_espace)


    print("",compt+1," "*nb_espace,compt+2," "*nb_espace,compt+3," "*nb_espace,compt+4)
    for j in range(len(liste[0][0])):
        for i in range(4):
            print(liste[0][i][j], end=" ") #Print la premier ligne des 4 premier block
        print("")
    compt+=1
    print("")



def select_bloc(politique,forme_plateau):
    cpt=0
    selection_block=[]
    if politique=="Mode ensemble":
        print_block(forme_plateau,cpt)
    else:
        for i in range(3):
            selection_block.append(block_dispo(forme_plateau)[randint(0, len(block_dispo(forme_plateau)))])
        for elm in selection_block:
            formated_block(elm)



# FONCTIONS POSITIONNEMENT
"""
FONCTION A CONTINUER DANS TEST.PY
def valid_position(grid,block,i,j):
    #i est la ligne la plus bass j est le block le plus a gauche
    for _ in range(len(block)):
        for _ in range(len(block)[0]):
            if grid[]
    return True"""


# Annulation de lignes/colonnes et calcul du score
def row_state(grid, i):
    if "1" in grid[i]:
        return False
    else:
        return True


def col_state(grid, j):
    elm_col = []
    for ligne in grid:
        elm_col.append(ligne[j])
    if "1" in elm_col:
        return False
    else:
        return True



def regles_ou_jouer():
    clean_console()
    tprint("Tetriste ? Arrete!", font='big ')
    print("\x1B[3mby Anaelle Pollart & Maxime Jaconelli\x1B[0m \n")
    liste_choix_debut = ["Jouer", "Afficher les règles du jeu"]
    choix = liste_choix_debut[cutie.select(liste_choix_debut)]
    if choix == "Jouer":
        parametre_jouer()
    else:
        regles()


def parametre_jouer():
    clean_console()
    print("Début du jeu")
    time.sleep(0.3)
    # Forme du plateau
    print("Choisir une forme:")
    liste_choix_forme = ["Cercle", "Triangle", "Losange"]
    forme_plateau = liste_choix_forme[cutie.select(liste_choix_forme)]
    forme_plateau = forme_plateau.lower()

    # Dimension du plateau
    dimension = 20
    while dimension < 21 or dimension > 26 or dimension % 2 == 0:
        dimension = int(input("Largeur du plateau: "))

    # Politique de suggestion de block
    liste_choix_politique = ["Mode ensemble", "Mode Aleatoire"]
    politique = liste_choix_politique[cutie.select(liste_choix_politique)]
    debut_partie(forme_plateau, dimension, politique)
    return 1


def regles():
    # Faire les regle et à la fin, on revient au menu
    clean_console()
    tprint("Regles")


    print("'Tetriste ? Arrete' est un dérivé du célèbre jeu Tetris.\n\n"
          "Principe du jeu:\n"
          "Le but est de faire le score le plus élevé possible en reussissant à placer un maximum de blocs dans un plateau.\n"
          "Une ligne ou une colonne est supprimée lorsqu'elle est pleine.\n\n"
          "Lors du lancement d'une partie, il est proposé de choisir la forme du plateau entre un losange, un triange ou un cercle\n"
          "Le joueur definira ensuite les dimension du plateau parmi 21x21, 23x23 ou 25x25\n\n"
          "Le joueur aura ensuite le choix entre deux modes de jeu:\n"
          "-Mode Ensemble:  \n"
          "En mode Ensemble, le programme affiche à chaque tour l'ensemble des blocs associés à la forme du plateau et en choisi 1 à placer\n"
          "-Mode Unique: \n"
          "En mode Unique, le programme affiche aléatoirement 3 blocs parmi ceux associés à la forme du plateau et en choisi 1 à placer\n\n"
          "Pour placer un bloc, le joueur doit saisir les coordonnées de l'endroit souhaité. Celles-ci correspondent au "
          "coin inférieur gauche du bloc choisi\n\n"
          "Le jeu se termine si:\n"
          "-Le joueur tente 3 tentative invalide (une tentative est considérée comme invalide lorsqu'il n'y a pas de place à l'endroit choisi pour placer le bloc\n"
          "-S'il presse la touche 'ECHAP'\n"
          )
    print("Fin des règles")
    choix_menu_principal = ["Retour au menu", "Quitter"]
    choix = choix_menu_principal[cutie.select(choix_menu_principal)]

    if choix == "Retour au menu":
        regles_ou_jouer()
    elif choix == "Quitter":
        quit()
    return 1


def debut_partie(forme_plateau, dimension, politique):
    global liste_block
    liste_block=block_dispo(forme_plateau)#liste des block a dispo


    # forme_plateau : "triangle" "losange "cercle"
    # dimension entier
    # politique : "Mode ensemble" "Mode Aleatoire
    # génération du plateau
    grid = read_grid(forme_plateau + ".txt")
    print_grid(grid, dimension)  # Poser la question si l'argument dimension supp est autorisé
    print(select_bloc(politique, forme_plateau))

    return 1


