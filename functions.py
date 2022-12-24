##########################################################
#   Projet : Tetriste? Arrete!                           #
#   Fichier : functions.py                               #
#   Auteurs : Anaëlle POLART & Maxime JACONELLI          #
#   Rôle : Contient l'ensemble des fonctions nécessaires #
#          au fonctionnement du jeu                      #
##########################################################


import math
import os
import time
import cutie  # Module pour les menus
from random import randint
from art import *  # Module pour L'affichage du texte du début
from block import Block_list


def clean_console():
    # Fonction réinitialisant l'affichage de la fonction, elle retourne 1 si tout c'est bien passé
    if os.name == 'nt':
        os.system('cls')
        return 1
    else:
        os.system('clear')
        return 1


def matrix_conversion(matrix_line):
    # Fonction permettant la conversion en chaine de caractère, elle prend en parametre une liste
    # et retourne un str
    str_list = ""
    for i in range(len(matrix_line)):
        str_list += str(matrix_line[i])
    return str_list  # F


def circle(dimension):
    # Fonction qui génère un cercle constitué de 0 et 1, en fonction du paramètre dimension, un entier, décrivant la
    # largeur/longueur du plateau, elle retourne 1 pour indiquer qu'elle s'est bien executée
    circle_file = open("cercle.txt", "w")
    # plateau = [[0 for j in range(0, dimension)] for i in range(0, dimension)]
    for i in range(dimension):
        for j in range(dimension):
            if math.sqrt((i - dimension // 2) ** 2 + (j - dimension // 2) ** 2) <= dimension // 2 + 1:
                circle_file.write("1")
            else:
                circle_file.write("0")
        if i < dimension + 1:
            circle_file.write("\n")
    circle_file.close()
    return 1

def rhombus(dimension):
    # Génère un losange de taille "dimension", un entier, et retourne 1 pour indiquer que tout c'est bien passé
    rhombus_file = open("losange.txt", "w")
    board = [[0 for _ in range(0, dimension)] for _ in range(0, dimension)]
    counter = 0
    center = (dimension // 2)
    for i in range(dimension // 2):
        for j in range(center - counter, center + counter + 1):
            board[i][j] = 1
        counter += 1
    for i in range(dimension // 2, dimension):
        for j in range(center - counter, center + counter + 1):
            board[i][j] = 1
        counter -= 1
    for lines in board:
        rhombus_file.write(matrix_conversion(lines) + '\n')
    rhombus_file.close()
    return 1


def triangle(dimension):
    # Génère un triangle de largeur dimension et de hauteur dimension divisé par 2
    triangle_file = open("triangle.txt", "w")
    board = [[0 for _ in range(0, dimension)] for _ in range(0, dimension)]
    counter = 0
    center = (dimension // 2)
    for i in range(dimension // 2 + 1):
        for j in range(center - counter, center + counter + 1):
            board[i][j] = 1
        counter += 1
    for b in range(dimension // 2):
        board.pop()
    for lignes in board:
        triangle_file.write(matrix_conversion(lignes) + '\n')

    triangle_file.close()
    return 1


# FONCTIONS GRID #
def read_grid(path: str):
    # Fonction prends en paramètre un str, décrivant le chemin d'accès d'un fichier text, et convertissant ce fichier en
    # matrice
    file_path = open(path, "r")
    file_read = file_path.readlines()
    file_path.close()
    grid = []
    for lines in file_read:
        line = lines.replace("\n", "")
        added_lines = []
        for number in line:
            added_lines.append(number)
        grid.append(added_lines)
    return grid


def print_grid(grid, dimension):
    # Fonction affichant le plateau de sorte à remplacer les 0 1 et 2 par des caractères plus graphique, et à générer un
    # cadre autour du plateau. Grid est le plateau de jeu et dimension la largeur du plateau. Elle ne retourne rien car
    # c'est une fonction d'affichage.
    # Affichage du cadre avec la grille
    min_alphabet = "abcdefghijklmnopqrstuvwxyz"
    maj_alphabet = min_alphabet.upper()
    print("", end="    ")
    for i in range(dimension):
        print(min_alphabet[i], end=" ")
    print("")
    for i in range(dimension * 2 + 3):  # 3 étant l'espacement de la grid
        if i == 0:
            print("  ╔", end="")
        elif i == (dimension * 2) + 2:
            print("╗", end="")
        else:
            print("═", end="")
    print("")
    i = 0
    for lines in grid:
        print(maj_alphabet[i], end=" ")
        print("║", end=" ")
        for number in lines:
            if number == '0':
                print(" ", end=" ")
            elif number == '1':
                print("•", end=" ")
            elif number == "2":
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
    #Fonction qui sauvegarde le plateau grid au chemin d'accès path
    save_file = open(path, "w")
    for lines in grid:
        line = ""
        for numbers in lines:
            line += numbers
        line += '\n'
        save_file.write(line)


def invalid_choice(error):
    # Affiche que l'utilisateur a rentré une mauvaise position et ses tentatives restantes.
    # Elle prend en paramètre error qui est un entier contenant le nombre d'érreurs du joueur et retourne un entier
    # qui est error incrémentée de 1.
    print("Choix invalide, nombre de tentatives restantes: ", 3 - error)
    return error + 1  # Cela ajoutera 1 au compteur d'erreur


def select_block(available_blocks, dimension):
    # Fonction qui permet de choisir le block à placer et sa position.
    # Elle prend en parametre une liste de blocks qui correspond aux blocs proposés au joueur et dimension un entier
    # correspondant à la largeur du plateau.
    # Elle renvoie les informations du block choisi (son indice et les coordonnées de placement).
    choosed_block = input("Numéro du block à placer: ")

    while not choosed_block.isdigit() or (0 >= int(choosed_block) or int(choosed_block) > len(
            available_blocks)):  # Saisie sécurisée ; on vérifie que le nombre rentré correspond bien à un block de la liste
        if not choosed_block.isdigit():
            print("Un nombre est requis")  # Si l'utilisateur rentre une lettre
        else:
            print("Aucun block ne correspond ")
        choosed_block = input("Numéro du block à placer: ")
    choosed_block = int(choosed_block)
    cord_x = str(input("Coordonnées de la colonne: "))

    while len(cord_x) > 1 or 97 > ord(cord_x) or ord(
            cord_x) >= 97 + dimension:  # on compare le code ascii des lettres rentrées avec celles ce
        print("Coordonnées inconnues")
        cord_x = str(input("Coordonnées de la colonne: "))
    cord_y = str(input("Coordonnées de la lignes: "))
    while len(cord_y) > 1 or 65 > ord(cord_y) or ord(cord_y) >= 65 + dimension:
        print("Coordonnées inconnues")
        cord_y = str(input("Coordonnées de la lignes: "))

    cord_x = ord(cord_x) - 97
    cord_y = ord(cord_y) - 65

    # Vérifie si la position est valide

    return (choosed_block, cord_x, cord_y)  # Retour des d'informations


def emplace_block(grid, choosed_block, cord_x,
                  cord_y):
    # Fonction qui place le block choisi par l'utilisateur aux coordonnées indiquées.
    # Elle prend en parametre le plateau, le block choisi et ses coordonnées et renvoie la grille avec le bloc placé dessus
    for i in range(len(choosed_block)):
        temp_x = cord_x  # Variable temporaire de x pour ne pas perdre la valeur initiale de x
        for j in range(len(choosed_block)):
            if choosed_block[len(choosed_block) - i - 1][
                j] == 2:  # Car si c'est une case vide, il n'y a rien à modifier
                grid[cord_y][temp_x] = "2"
            temp_x += 1
        cord_y -= 1
    return grid  # Retourne la grille avec le block placé


def valid_position(grid, choosed_block, cord_x,
                   cord_y):
    # Fonction Vérifiant si le block choisi peut se placer aux coordonnées choisies.
    # Elle prend en parametre le plateau, le block choisi et les coordonnées de placement à vérifier.
    # Elle retourne false si le placement est impossible, et true si l'inverse.
    global error_count  # Pour pouvoir modifier le compteur error_count
    temp_cord_x, temp_cord_y = cord_x, cord_y
    for i in range(len(choosed_block)):
        temp_cord_x = cord_x
        for j in range(len(choosed_block)):
            if choosed_block[len(choosed_block) - 1 - i][j] == 2:  # dernière ligne
                # Verifier que la case de cord_x,cord_y soit == 1
                if temp_cord_x < len(grid[0]) and temp_cord_y < len(grid[0]):
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


def available_blocks(shape, blocks_politic):
    # Fonction qui retourne une liste des blocs que l'utilisateur pourra selectionné, en fonction de son mode de jeu
    # Elle prend en paramètre la forme du plateau et le mode de jeu
    availables_blocks_list = []
    common_blocks_list = []
    shape_blocks_list = []
    if shape == 'triangle':
        matched_block_index = (46, 56)
    elif shape == 'rhombus':
        matched_block_index = (32, 45)
    else:
        matched_block_index = (20, 31)
    for i in range(0, 20):
        common_blocks_list.append(Block_list[i])
    for i in range(matched_block_index[0], matched_block_index[1] + 1):
        shape_blocks_list.append(Block_list[i])

    for elm in common_blocks_list:
        availables_blocks_list.append(elm)
    for elm in shape_blocks_list:  # Ajout des blocs dépendants de la forme du plateau
        availables_blocks_list.append(elm)

    if blocks_politic == "Mode aleatoire":
        block1, block2, block3 = 0, 0, 0
        while block1 == block2 or block1 == block3 or block2 == block3:
            block1 = randint(0, len(availables_blocks_list) - 1)
            block2 = randint(0, len(availables_blocks_list) - 1)
            block3 = randint(0, len(availables_blocks_list) - 1)
        random_blocks_list = [availables_blocks_list[block1], availables_blocks_list[block2],
                              availables_blocks_list[block3]]
        return random_blocks_list
    return availables_blocks_list


def reformat_lines(
        lines: list):
    # Fonction formatant l'affichage des blocks, en remplaçant les 1 et 2 par des caractères ascii
    # Elle prend en paramètre une line d'un block et retourne une chaine de caractère
    str_lines = ""
    for elm in lines:
        str_lines += str(elm)
        str_lines += " "
    str_lines = str_lines.replace("1", "•")
    str_lines = str_lines.replace("2", "■")
    return str_lines


def print_blocks(politic, blocks_list):
    # Affichage des blocks disponibles en fonctions du mode de jeu sélectionné
    # Elle prend en paramètre le mode de jeu et la liste des blocks associés à ce mode
    print("")
    counter = 0
    num = 1
    if politic == "Mode ensemble":
        for i in range(0, len(blocks_list) // 10):
            if i + counter > len(blocks_list):  # Pour éviter l'out of range
                break
            for k in range(len(blocks_list[i + counter])):  # Affichage des numéros des blocks
                if k - 1 == -1:
                    for m in range(10):
                        text_num = ""
                        text_num += str(num)
                        espace = len(blocks_list[i + counter]) + 7 + len(
                            blocks_list[counter + i]) - 4  # Affichage adaptatif
                        while len(text_num) != espace:
                            text_num += " "

                        print(text_num, end="")
                        num += 1
                    print("")
                for j in range(10):
                    print(reformat_lines(blocks_list[j + counter][k]), end="   ")
                print("")
            print("")
            counter += 10
        # BLOCKS RESTANTS
        for k in range(len(blocks_list[-1])):
            if k - 1 == -1:
                for m in range(len(blocks_list) - counter):
                    text_num = ""
                    text_num += str(num)
                    espace = len(blocks_list[counter]) + 7 + len(blocks_list[counter]) - 4
                    while len(text_num) != espace:
                        text_num += " "
                    print(text_num, end="")
                    num += 1
                print("")
            for j in range(len(blocks_list) - counter - 1, -1, -1):
                print(reformat_lines(blocks_list[len(blocks_list) - j - 1][k]), end="   ")
            print("")
    else:
        for elm in blocks_list:
            print(num)
            for lignes in elm:
                print(reformat_lines(lignes))
            print("")
            num += 1


# Annulation de lignes/colonnes et calcul du score
def row_state(grid, i):
    # Verifie si une ligne est pleine.
    # Elle prend en paramètre le plateau et l'indice de la ligne à vérifié.
    # Elle retourne True si la ligne est pleine et False sinon.
    if grid[i].count("2") == 1:
        return False
    for j in range(len(grid[i])):
        if grid[i][j] != "0" and grid[i][j] != "2":
            return False
    return True


def row_clear(grid, i):
    # Suppression d'une ligne.
    # Elle prend en paramètre le plateau et l'indice de la ligne à supprimer

    global score  # Afin de mettre à jour le score
    score += grid[i].count("2")  # Ajoute au score le nombre de cases supprimées
    # Supprime la ligne complete
    for j in range(len(grid[0])):
        if grid[i][j] == "2":
            grid[i][j] = "1"
    # Décale les lignes du dessus
    for k in range(i, 0, -1):
        for m in range(len(grid[k])):
            if grid[k][m] == "1" or grid[k][m] == "2":
                if (grid[k - 1][m] == "1" or grid[k - 1][m] == "2") and k - 1 >= 0:
                    # Car sinon cela va ramener la ligne du bas en haut
                    grid[k][m] = grid[k - 1][m]
    return True  # Retour de test, signifie que la fonction s'est bien passée


def col_state(grid, j):
    # Verifie si une colonne est pleine
    # Prends en paramètre le plateau et l'indice de la colonne à vérifier
    # Retourne True si la clonne est pleine et False sinon
    counter = 0
    for i in range(len(grid)):
        if grid[i][j] == "2":
            counter += 1
        if grid[i][j] != "0" and grid[i][j] != "2":
            return False
    if counter > 1:  # Car une colonne ne fait pas 1 block de haut
        return True
    else:
        return False


def col_clear(grid, i):
    # Supprime la colonne d'indice i.
    # Elle prend en parametre le plateau et l'indice de la colonne à supprimer.
    # Elle retourne True pour indiquer que tout c'est bien passé.
    global score
    for j in range(len(grid)):
        if grid[j][i] != "0":
            score += 1  # Ajoute au score le nombre de cases supprimées
            grid[j][i] = "1"
    return True

def start_or_rules():
    # Fonction du début du jeu, elle propose au jouer de soit lire les règles soit de commencer à jouer.
    clean_console()
    tprint("Tetriste ? Arrete!", font='big ')
    print("\x1B[3mby Anaelle Pollart & Maxime Jaconelli\x1B[0m \n")
    starting_choices_list = ["Jouer", "Afficher les règles du jeu"]
    choice = starting_choices_list[cutie.select(starting_choices_list)]  # Menu à cases
    if choice == "Jouer":
        return "play"
    else:
        return "rules"


def game_configuration():
    # Parametrage global du jeu
    #Elle retourne True pour indquer que tout c'est bien passé
    clean_console()
    print("Début du jeu\n")
    time.sleep(0.3)
    # Forme du plateau
    print("Choisir une forme:")
    shaping_choices_list = ["Cercle", "Triangle", "Losange"]
    shape = shaping_choices_list[cutie.select(shaping_choices_list)]
    shape = shape.lower()
    print("")
    # Dimension du plateau
    print("Choisir la taille du plateau:")
    dimension_choices_list = [21, 23, 25]
    dimension = dimension_choices_list[cutie.select(dimension_choices_list)]
    print("")
    # Generation du fichier
    if shape == 'cercle':
        circle(dimension)
    if shape == 'triangle':
        triangle(dimension)
    elif shape == 'losange':
        rhombus(dimension)
    # Politique de suggestion de block
    print("Choisir la politique d'affichage (cf. Règles)")
    politic_choices_list = ["Mode ensemble", "Mode aleatoire"]
    politic = politic_choices_list[cutie.select(politic_choices_list)]
    start_game(shape, dimension, politic)
    return True


def rules():
    # Affiche les règles du jeu et propose au joueur de quitter ou revenir au menu principal.
    # Retourne True pour indiquer que tout c'est bien passé.
    clean_console()
    tprint("Regles")

    print("'Tetriste ? Arrete' est un dérivé du célèbre jeu Tetris.\n\n"
          "Principe du jeu:\n"
          "Le but est de faire le score le plus élevé possible en reussissant à placer un maximum de blocs dans un "
          "plateau.\n "
          "Une ligne ou une colonne est supprimée lorsqu'elle est pleine.\n\n"
          "Lors du lancement d'une partie, il est proposé de choisir la forme du plateau entre un losange, un triange "
          "ou un cercle\n "
          "Le joueur définira ensuite les dimension du plateau parmi 21x21, 23x23 ou 25x25\n\n"
          "Le joueur aura ensuite le choix entre deux modes de jeu:\n"
          "-Mode Ensemble:  \n"
          "En mode Ensemble, le programme affiche à chaque tour l'ensemble des blocs associés à la forme du plateau "
          "et en choisi 1 à placer\n "
          "-Mode Unique: \n"
          "En mode Unique, le programme affiche aléatoirement 3 blocs parmi ceux associés à la forme du plateau et en "
          "choisi 1 à placer\n\n "
          "Pour placer un bloc, le joueur doit saisir les coordonnées de l'endroit souhaité. Celles-ci correspondent "
          "au "
          "coin inférieur gauche du bloc choisi\n\n"
          "Le jeu se termine si:\n"
          "-Le joueur tente 3 tentative invalide (une tentative est considérée comme invalide lorsqu'il n'y a pas de "
          "place à l'endroit choisi pour placer le bloc)\n "
          "-S'il presse la touche 'ECHAP'\n"
          )
    print("Fin des règles")
    main_menu_choices = ["Retour au menu", "Quitter"]
    choice = main_menu_choices[cutie.select(main_menu_choices)]

    if choice == "Retour au menu":
        start_or_rules()
    elif choice == "Quitter":
        quit()
    return True


def start_game(shape, dimension, politic):
    # Fonction qui lance le jeu en fonction de shape, la forme du plateau, dimension, la largeur du plateau et politic
    # le mode de jeu
    # Elle retourne True pour indiquer que tout c'est bien passer
    global score, error_count
    score = 0
    error_count = 0
    # forme_plateau : "triangle" "losange "cercle"
    # dimension entier
    # politique : "Mode ensemble" "Mode Aleatoire
    # génération du plateau
    grid = read_grid(shape + ".txt")  # Matrice de caractères numériques
    # À faire en boucle
    while error_count < 3:
        blocks_list = available_blocks(shape, politic)
        clean_console()
        print("")
        print_grid(grid, dimension)  # Poser la question si l'argument dimension supp est autorisé
        if error_count == 0:
            print("Score actuel:", score, end="")
        else:
            print("Score actuel:", score, "Tentative restantes:", 3 - error_count, end="")
        print_blocks(politic, blocks_list)
        block_data = select_block(blocks_list,
                                  dimension)  # block data est un tuple contenant le block choisi et les coordonnées
        choosed_block = blocks_list[block_data[0] - 1]  # le block à placer
        if valid_position(grid, choosed_block, block_data[1], block_data[2]):
            grid = emplace_block(grid, choosed_block, block_data[1], block_data[2])
        # Vérification des lignes / colonnes pleines
        for i in range(len(grid)):
            if row_state(grid, i):
                row_clear(grid, i)
            if col_state(grid, i):
                col_clear(grid, i)

    #Si le joueur à fait trop de tentatives invalides:
    if error_count >= 3:
        print("")
        print("Trop de position invalides!\n"
              "Fin du jeu\n"
              "Score final: ", score)

        newgame_choices_list = ["Rejouer", "Quitter"]
        newgame_choice = newgame_choices_list[cutie.select(newgame_choices_list)]
        if newgame_choice == "Rejouer":
            start_or_rules()
        else:
            quit()
    return True
