##########################################################
#   Projet : Tetriste? Arrete!                           #
#   Fichier : main.py                                    #
#   Auteurs : Anaëlle POLART & Maxime JACONELLI          #
#   Rôle : Appeler les fonctions de lancement du jeu     #
##########################################################

from functions import *

if __name__ == '__main__':
    if start_or_rules()=="play":
        game_configuration()
    elif start_or_rules()=="rules":
        rules()
