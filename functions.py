import math
import os
import time
import cutie
from random import randint
from art import *
from block import Block_list


def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return 1


def conversion_matrice(ligne_matrice):  # Fonction permettant la convertion d'une matrice en chaine de caractère
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
    file_cercle.close()


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
        file_losange.write(conversion_matrice(lignes) + '\n')
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
        file_triangle.write(conversion_matrice(lignes) + '\n')

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


def invalid_choice(error):
    print("Choix invalide, nombre de tentatives restantes: ", 3 - error)
    return error + 1


# FONCTIONS BLOCS

def select_block(block_dispo, dimension):
    cord_x = 0
    cord_y = 0
    block_choisi = int(input("Numero du block à placer: "))
    while 0 >= block_choisi or block_choisi > len(block_dispo):
        print("Numero Invalide")
        block_choisi = int(input("Numero du block à placer: "))
    cord_x = ord(str(input("Coordonnées de la colonne: ")))
    while 97 > cord_x or cord_x >= 97 + dimension:
        print("Coordonnées inconnues")
        cord_x = ord(str(input("Coordonnées de la colonne: ")))
    cord_y = ord(str(input("Coordonnées de la lignes: ")))
    while 65 > cord_y or cord_y >= 65 + dimension:
        print("Coordonnées inconnues")
        cord_y = ord(str(input("Coordonnées de la lignes: ")))

    cord_x = cord_x - 97
    cord_y = cord_y - 65

    # Vérifie si la postition est valid

    return (block_choisi, cord_x, cord_y)


def emplace_block(grid, block_choisi, cord_x, cord_y):
    temp_x, temp_y = cord_x, cord_y
    for i in range(len(block_choisi)):
        temp_x = cord_x
        for j in range(len(block_choisi)):
            if block_choisi[len(block_choisi) - i - 1][j] == 2:
                grid[temp_y][temp_x] = "2"
            temp_x += 1
        temp_y -= 1
    return grid


def valid_position(grid, block_choisi, cord_x, cord_y):
    global error_count
    temp_cord_x, temp_cord_y = cord_x, cord_y
    modified_grid = []
    for elm in grid:
        modified_grid.append(elm)
    # CAS 1, BLOCK A PLACE: VERIF SI CASE EXISTE, VERIF SI CASE !=2
    # CAS 2, VIDE, ALORS ON SEN FICHE ET ON PASSE A CELLE DAPRES
    # SENS DE DEPLACEMENT DE GAUCHE A DROITE ET BAS VERS LE HAUT

    for i in range(len(block_choisi)):
        temp_cord_x = cord_x
        for j in range(len(block_choisi)):
            if block_choisi[len(block_choisi) - 1 - i][j] == 2:  # derniere ligne
                # Verifier que la case de cord_x,cord_y soit ==1

                if temp_cord_x < len(grid) and temp_cord_y < len(grid):
                    if grid[temp_cord_y][temp_cord_x] != "1":
                        error_count += 1
                        print("Position invalide, tentatives restantes: ", 3 - error_count)
                        time.sleep(1)

                        return False


                else:
                    error_count += 1
                    print("Position invalide, tentatives restantes: ", 3 - error_count)
                    time.sleep(1)
                    return False
            temp_cord_x += 1
        temp_cord_y -= 1

    return True


def block_dispo(forme_plateau, politique):
    liste_blocks_dispo = []
    ajout_commum = []
    ajout_forme = []
    if forme_plateau == 'triangle':
        matched_block_index = (47, 56)
    elif forme_plateau == 'losange':
        matched_block_index = (33, 46)
    else:
        matched_block_index = (20, 31)
    for i in range(0, 20):
        ajout_commum.append(Block_list[i])
    for i in range(matched_block_index[0], matched_block_index[1] + 1):
        ajout_forme.append(Block_list[i])

    for elm in ajout_commum:
        liste_blocks_dispo.append(elm)
    for elm in ajout_forme:
        liste_blocks_dispo.append(elm)

    if politique == "Mode aleatoire":
        block1, block2, block3 = 0, 0, 0
        while block1 == block2 or block1 == block3 or block2 == block3:
            block1 = randint(0, len(liste_blocks_dispo)-1)
            block2 = randint(0, len(liste_blocks_dispo)-1)
            block3 = randint(0, len(liste_blocks_dispo)-1)
        liste_blocks_aleatoire = []
        liste_blocks_aleatoire.append(liste_blocks_dispo[block1])
        liste_blocks_aleatoire.append(liste_blocks_dispo[block2])
        liste_blocks_aleatoire.append(liste_blocks_dispo[block3])
        return liste_blocks_aleatoire
    return liste_blocks_dispo


def reformat_lines(lines: list):
    str_lines = ""
    for elm in lines:
        str_lines += str(elm)
        str_lines += " "
    str_lines = str_lines.replace("1", "•")
    str_lines = str_lines.replace("2", "■")
    return str_lines


def print_blocks(politique,liste_blocks):
    print("")
    compt = 0
    num = 1
    if politique=="Mode ensemble":
        for i in range(0, len(liste_blocks) // 5):
            if i + compt > len(liste_blocks):  # Pour eviter le out of range
                break

            for k in range(len(liste_blocks[i + compt])):
                if k - 1 == -1:
                    for m in range(10):
                        text_num = ""
                        text_num += str(num)
                        espace = len(liste_blocks[i + compt]) + 7 + len(liste_blocks[compt + i]) - 4  # Afficage adaptatif
                        while len(text_num) != espace:
                            text_num += " "

                        print(text_num, end="")
                        num += 1

                    print("")
                for j in range(10):
                    print(reformat_lines(liste_blocks[j + compt][k]), end="   ")

                print("")
            print("")
            compt += 10
        # BLOCKS RESTANTS
        for k in range(len(liste_blocks[-1])):
            if k - 1 == -1:
                for m in range(len(liste_blocks) - compt):
                    text_num = ""
                    text_num += str(num)
                    espace = len(liste_blocks[compt]) + 7 + len(liste_blocks[compt]) - 4
                    while len(text_num) != espace:
                        text_num += " "
                    print(text_num, end="")
                    num += 1
                print("")
            for j in range(len(liste_blocks) - compt):  # 0 à 1
                print(reformat_lines(liste_blocks[len(liste_blocks) - j - 1][k]), end="   ")
            print("")
    else:
        for elm in liste_blocks:
            print(num)
            for lignes in elm:
                print(reformat_lines(lignes))
            print("")
            num+=1
# Annulation de lignes/colonnes et calcul du score
def row_state(grid, i):
    for j in range(len(grid[i])):
        if grid[i][j] != "0" and grid[i][j] != "2":
            return False
    return True


def row_clear(grid, i):
    global score
    score += grid[i].count("2")
    # Supprime la ligne complete
    for j in range(len(grid)):
        grid[i][j] = grid[i][j].replace("2", "1")
    # Décale les lignes du dessus
    for k in range(i, -1, -1):
        for m in range(len(grid[k])):
            if grid[k][m] == "1" or grid[k][m] == "2":
                if (grid[k - 1][m] == "1" or grid[k - 1][
                    m] == "2") and k - 1 >= 0:  # Car sinon cela va ramener la ligne du bas en haut

                    grid[k][m] = grid[k - 1][m]
    return True


def col_state(grid, j):
    for i in range(len(grid)):
        if grid[i][j] != "0" and grid[i][j] != "2":
            return False
    return True


def col_clear(grid, i):
    global score
    for j in range(len(grid)):
        if grid[j][i] != "0":
            score += 1
            grid[j][i] = "1"


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
    print("Début du jeu\n")
    time.sleep(0.3)
    # Forme du plateau
    print("Choisir une forme:")
    liste_choix_forme = ["Cercle", "Triangle", "Losange"]
    forme_plateau = liste_choix_forme[cutie.select(liste_choix_forme)]
    forme_plateau = forme_plateau.lower()
    print("")
    # Dimension du plateau
    print("Choisir la taille du plateau:")
    liste_choix_dimension = [21, 23, 25]
    dimension = liste_choix_dimension[cutie.select(liste_choix_dimension)]
    print("")
    # Generation du fichier
    if forme_plateau == 'cercle':
        cercle(dimension)
    if forme_plateau == 'triangle':
        triangle(dimension)
    elif forme_plateau == 'losange':
        losange(dimension)
    # Politique de suggestion de block
    print("Choisir la politique d'affichage (cf. Règles)")
    liste_choix_politique = ["Mode ensemble", "Mode aleatoire"]
    politique = liste_choix_politique[cutie.select(liste_choix_politique)]
    debut_partie(forme_plateau, dimension, politique)
    return True


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
    global score, error_count
      # liste des block a dispo
    score = 0
    error_count = 0

    # forme_plateau : "triangle" "losange "cercle"
    # dimension entier
    # politique : "Mode ensemble" "Mode Aleatoire
    # génération du plateau
    grid = read_grid(forme_plateau + ".txt")  # Matrice de caractere numérique
    # À faire en boucle
    while error_count < 3:
        liste_blocks = block_dispo(forme_plateau, politique)
        clean_console()

        print("")

        print_grid(grid, dimension)  # Poser la question si l'argument dimension supp est autorisé

        if error_count == 0:
            print("Score actuel:", score)
        else:
            print("Score actuel:", score, "Tentative restantes:", 3 - error_count)
        print_blocks(politique,liste_blocks)
        if error_count == 0:
            print("Score actuel:", score)
        else:
            print("Score actuel:", score, "Tentative restantes:", 3 - error_count)
        block_data = select_block(liste_blocks,
                                  dimension)  # block data est un tuple contenant le block choisi et les coordonnées
        block_choisi = liste_blocks[block_data[0] - 1]  # le block à placer
        if valid_position(grid, block_choisi, block_data[1], block_data[2]):
            grid = emplace_block(grid, block_choisi, block_data[1], block_data[2])

        for i in range(len(grid)):
            if row_state(grid, i):
                row_clear(grid, i)
            if col_state(grid, i):
                col_clear(grid, i)

    if error_count >= 3:
        print("")
        print("Trop de position invalides!\n"
              "Fin du jeu\n"
              "Score final: ", score)

        liste_choix_rejouer = ["Rejouer", "Quitter"]
        choix_rejouer = liste_choix_rejouer[cutie.select(liste_choix_rejouer)]
        if choix_rejouer == "Rejouer":
            regles_ou_jouer()
        else:
            quit()
    pass

# TODO:
# [ ]: Revoir le fait de ne pas placer un bloc quand invalide
# [x]: Faire le compteur du score
# [ ]: Afficher les block
# [ ]: Faire des saisie sécurisées
