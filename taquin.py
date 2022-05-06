#########################################
# groupe 1 MIASHS TD2
# '' projet taquin ''
# Julien De Barros 
# Sofian Amri
# Leo Goncalves
# Suleyman Charpentier
# https://github.com/uvsq21916036/projet_taquin.git
#########################################


#########################
# import des librairies 
import tkinter as tk
import random as rd

############################
# définition des constantes

# hauteur et largeur du canevas
H = 400
L = 400

# grille = []


##############
# fonctions

def création_de_terrain():
    'cette fonction va nous permettre de générer un damier avec 16 cases numérotées dont celle en bas à droite est vide'
    nb_taquin = [i for i in range(1, 17)]
    rd.shuffle(nb_taquin)                                                     
    grille = [[nb_taquin[4*m+n]for n in range(4)] for m in range(4)]
    
    for i in range(4):
        for j in range(4):
            x = j*100
            y = i*100
            a = (x, y)
            b = (x + 100, y + 100)
            centre = (x + 50, y + 50)
            rectangle = canvas.create_rectangle(a, b, fill="white")
            txt = grille[i][j]
            nb = canvas.create_text(centre, text = grille[i][j], fill="black")

    #items[txt] = (rectangle, nb)
    canvas.delete(rectangle)
    canvas.delete(nb)
    #return txt

    
   
def sauvegarde():
    'cette fonction va nous permettre de sauvegarder une partie en cours dans un fichier'
    taquin_en_cours = items[txt]
    fic = open('sauvegardedejeu.txt', 'w+')
    fic.write(taquin_en_cours)
    fic.close
    

def gen_sauv():
    'cette fonction va nous permettre de récupérer une sauvegarde de la partie précédente'

    pass

def déplacement():
    'cette fonction va gérer les déplacement des cases sur le damier'
    pass


#########################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title('projet taquin')

canvas = tk.Canvas(racine, bg ='white', height= H,width= L )

bouton_sauv = tk.Button(racine, text='sauvegarde', command = sauvegarde)
bouton_gen = tk.Button(racine, text='généré sauvegarde', command = gen_sauv)
bouton_création = tk.Button(racine, text='démarrer', command = création_de_terrain)

# position des widgets
canvas.grid(rowspan = 3)
bouton_création.grid(column = 0, row = 3)
bouton_gen.grid(column = 1 , row = 1)
bouton_sauv.grid(column = 1, row = 2)

canvas.bind('<Button-1>', déplacement)


racine.mainloop()
