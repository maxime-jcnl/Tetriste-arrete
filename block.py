###########################################################################
#   Projet : Tetriste? Arrete!                                            #
#   Fichier : block.py                                                    #
#   Auteurs : Anaëlle POLART & Maxime JACONELLI                           #
#   Rôle : Contient les blocks et la liste des blocks nécessaires au jeu  #
###########################################################################


communs_1 = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [2, 1, 1, 1],
             [2, 2, 1, 1]]

communs_2 = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 2, 1, 1],
             [2, 2, 1, 1]]

communs_3 = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [2, 1, 1, 1],
             [2, 2, 2, 1]]

communs_4 = [[1, 1, 1, 1],
             [2, 2, 1, 1],
             [1, 2, 1, 1],
             [1, 2, 1, 1]]

communs_5 = [[1, 1, 1, 1],
             [2, 1, 1, 1],
             [2, 2, 1, 1],
             [2, 1, 1, 1]]

communs_6 = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 2, 1, 1],
             [2, 2, 2, 1]]

communs_7 = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [2, 2, 1, 1],
             [1, 2, 2, 1]]

communs_8 = [[1, 1, 1, 1],
             [2, 1, 1, 1],
             [2, 2, 1, 1],
             [1, 2, 1, 1]]

communs_9 = [[2, 1, 1, 1],
             [2, 1, 1, 1],
             [2, 1, 1, 1],
             [2, 1, 1, 1]]

communs_10 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [2, 2, 1, 1],
              [2, 2, 1, 1]]

communs_11 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [2, 2, 1, 1],
              [1, 2, 1, 1]]

communs_12 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [2, 2, 1, 1],
              [2, 1, 1, 1]]

communs_13 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 2, 1],
              [2, 2, 2, 1]]

communs_14 = [[1, 1, 1, 1],
              [2, 1, 1, 1],
              [2, 1, 1, 1],
              [2, 2, 1, 1]]

communs_15 = [[1, 1, 1, 1],
              [1, 2, 1, 1],
              [2, 2, 1, 1],
              [1, 2, 1, 1]]

communs_16 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [2, 2, 2, 1],
              [1, 2, 1, 1]]

communs_17 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 2, 2, 1],
              [2, 2, 1, 1]]

communs_18 = [[1, 1, 1, 1],
              [1, 2, 1, 1],
              [2, 2, 1, 1],
              [2, 1, 1, 1]]

communs_19 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [2, 2, 2, 2]]

communs_20 = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [2, 1, 1, 1]]

# figure 1 du plateau cercle
cercle_1 = [[1, 1, 1, 1, 1],
            [2, 2, 2, 2, 1],
            [2, 2, 2, 2, 1],
            [2, 2, 2, 2, 1],
            [2, 2, 2, 2, 1]]

# figure 2 du plateau cercle
cercle_2 = [[1, 1, 1, 1, 1],
            [1, 2, 2, 1, 1],
            [2, 2, 2, 2, 1],
            [2, 2, 2, 2, 1],
            [1, 2, 2, 1, 1]]

# figure 3 du plateau cercle
cercle_3 = [[1, 1, 1, 1, 1],
            [2, 1, 1, 2, 1],
            [2, 1, 1, 2, 1],
            [2, 1, 1, 2, 1],
            [2, 2, 2, 2, 1]]

# figure 4 du plateau cercle
cercle_4 = [[1, 1, 1, 1, 1],
            [2, 2, 2, 2, 1],
            [1, 1, 1, 2, 1],
            [1, 1, 1, 2, 1],
            [1, 1, 1, 2, 1]]

# figure 5 du plateau cercle
cercle_5 = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 1],
            [2, 2, 2, 1, 1]]

# figure 6 du plateau cercle
cercle_6 = [[1, 1, 1, 1, 1],
            [2, 2, 2, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 2, 1, 1],
            [2, 2, 2, 1, 1]]

# figure 7 du plateau cercle
cercle_7 = [[1, 1, 1, 1, 1],
            [2, 2, 1, 1, 1],
            [2, 2, 1, 1, 1],
            [2, 2, 1, 1, 1],
            [2, 2, 1, 1, 1]]

# figure 8 du plateau cercle
cercle_8 = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 1],
            [2, 2, 2, 2, 1]]

# figure 9 du plateau cercle
cercle_9 = [[2, 1, 1, 1, 1],
            [2, 1, 1, 1, 1],
            [2, 1, 1, 1, 1],
            [2, 1, 1, 1, 1],
            [2, 1, 1, 1, 1]]

# figure 10 du plateau cercle
cercle_10 = [[1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [2, 1, 1, 1, 2]]

# figure 11 du plateau cercle
cercle_11 = [[1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2]]

# figure 12 du plateau cercle
cercle_12 = [[1, 1, 1, 1, 1],
             [2, 1, 1, 1, 1],
             [2, 1, 1, 1, 1],
             [2, 1, 1, 2, 1],
             [2, 2, 2, 2, 1]]

# creation de la liste qui va contenir les blocs du plateau losange


# figure 1 du plateau losange
losange_1 = [[1, 1, 1, 1, 1],
             [1, 1, 2, 2, 1],
             [1, 2, 2, 1, 1],
             [2, 2, 1, 1, 1],
             [2, 1, 1, 1, 1]]

# figure 2 du plateau losange
losange_2 = [[1, 1, 1, 1, 1],
             [2, 2, 1, 1, 1],
             [1, 2, 2, 1, 1],
             [1, 1, 2, 2, 1],
             [1, 1, 1, 2, 1]]

# figure 3 du plateau losange
losange_3 = [[1, 1, 1, 1, 1],
             [2, 2, 2, 2, 1],
             [1, 2, 2, 1, 1],
             [1, 2, 2, 1, 1],
             [1, 2, 2, 1, 1]]

# figure 4 du plateau losange
losange_4 = [[1, 1, 1, 1, 1],
             [2, 1, 1, 2, 1],
             [1, 2, 2, 1, 1],
             [1, 2, 2, 1, 1],
             [2, 1, 1, 2, 1]]

# figure 5 du plateau losange
losange_5 = [[1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [1, 2, 2, 2, 1],
             [1, 1, 2, 1, 1]]

# figure 6 du plateau losange
losange_6 = [[1, 1, 1, 1, 1],
             [2, 2, 2, 2, 1],
             [2, 2, 2, 2, 1],
             [2, 2, 2, 2, 1],
             [2, 2, 2, 2, 1]]

# figure 7 du plateau losange
losange_7 = [[1, 1, 1, 1, 1],
             [2, 1, 1, 1, 1],
             [2, 2, 1, 1, 1],
             [1, 2, 2, 1, 1],
             [1, 1, 2, 2, 1]]

# figure 8 du plateau losange
losange_8 = [[1, 1, 1, 1, 1],
             [1, 1, 1, 2, 1],
             [1, 1, 2, 2, 1],
             [1, 2, 2, 1, 1],
             [2, 2, 1, 1, 1]]

# figure 9 du plateau losange
losange_9 = [[2, 1, 1, 1, 1],
             [2, 1, 1, 1, 1],
             [2, 1, 1, 1, 1],
             [2, 1, 1, 1, 1],
             [2, 1, 1, 1, 1]]

# figure 10 du plateau losange
losange_10 = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 2, 1],
              [2, 2, 2, 2, 1],
              [1, 1, 1, 2, 1]]

# figure 11 du plateau losange
losange_11 = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [2, 2, 2, 2, 2]]

# figure 12 du plateau losange
losange_12 = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [2, 2, 2, 2, 1],
              [1, 1, 1, 2, 1]]

# figure 13 du plateau losange
losange_13 = [[1, 1, 1, 1, 1],
              [2, 2, 1, 1, 1],
              [1, 2, 1, 1, 1],
              [1, 2, 1, 1, 1],
              [1, 2, 1, 1, 1]]

# figure 14 du plateau losange
losange_14 = [[1, 1, 1, 1, 1],
              [2, 1, 1, 1, 1],
              [2, 1, 1, 1, 1],
              [2, 1, 1, 1, 1],
              [2, 2, 1, 1, 1]]

triangle_1 = [[2, 1, 1],
              [2, 2, 2],
              [1, 1, 2]]

# figure 2 du plateau triangle
triangle_2 = [[2, 2, 1],
              [1, 2, 1],
              [1, 2, 2]]

# figure 3 du plateau triangle
triangle_3 = [[1, 1, 2],
              [2, 2, 2],
              [2, 1, 1]]

# figure 4 du plateau triangle
triangle_4 = [[1, 2, 2],
              [1, 2, 1],
              [2, 2, 1]]

# figure 5 du plateau triangle
triangle_5 = [[1, 1, 2],
              [1, 2, 1],
              [2, 1, 1]]

# figure 6 du plateau triangle
triangle_6 = [[2, 1, 1],
              [1, 2, 1],
              [1, 1, 2]]

# figure 7 du plateau triangle
triangle_7 = [[2, 1, 1],
              [2, 1, 1],
              [2, 1, 1]]

# figure 8 du plateau triangle
triangle_8 = [[1, 1, 1],
              [1, 1, 1],
              [2, 2, 2]]

# figure 9 du plateau triangle
triangle_9 = [[1, 1, 1],
              [2, 1, 1],
              [2, 1, 1]]

# figure 10 du plateau triangle
triangle_10 = [[1, 2, 1],
               [2, 2, 2],
               [1, 2, 1]]

# figure 11 du plateau triangle
triangle_11 = [[1, 1, 1],
               [1, 1, 1],
               [2, 2, 1]]

Block_list = [
    # BLOCKS COMMUNS
    communs_1, communs_2, communs_3, communs_4, communs_5, communs_6, communs_7, communs_8, communs_9, communs_10,
    communs_11, communs_12, communs_13, communs_14, communs_15, communs_16, communs_17, communs_18, communs_19,
    communs_20,
    # BLOCKS CERCLES
    cercle_1, cercle_2, cercle_3, cercle_4, cercle_5, cercle_6, cercle_7, cercle_8, cercle_9, cercle_10,
    cercle_11, cercle_12,
    # BLOCKS LOSANGE
    losange_1, losange_2, losange_3, losange_4, losange_5, losange_6, losange_7, losange_8, losange_9, losange_10,
    losange_11,
    losange_12, losange_13, losange_14,
    # BLOCKs TRIANGLE
    triangle_1, triangle_2, triangle_3, triangle_4, triangle_5, triangle_6, triangle_7, triangle_8, triangle_9,
    triangle_10, triangle_11
]

