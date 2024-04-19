from random import*
import winsound

'''
Theme : évolution d'une population
Code couleur : 
    Cellule noir : civil lambda
    Cellule rouge : civil résistant 
    Cellule Bleu : civil terroriste
Notre automatre cellulaire simule le développement d'une population à partir des des voisins qui entourent une cellule déjà vivante
Il permet au délà de ce que fait le Jeu de la vie une intéraction entre differentes branches au sein d'une même population ce qui rend la simulation plus 
'''

def BOOM(T, i, j,):
    n = len(T)
    m = len(T[0])
    
    # Définir le rayon de l'explosion
    rayon = 1
    
    # Parcourir les cellules dans le rayon de l'explosion
    for x in range(i - rayon, i + rayon ):
        for y in range(j - rayon, j + rayon):
            if T[x][y] != 2:
                T[x][y] = 0
    winsound.PlaySound("tnt",winsound.SND_FILENAME)
                

def creer_tableau(n, m):
    T = list()
    for j in range(n):
        M = list()
        for i in range(m):
            M.append(0)
        T.append(M)
    return T  

def ajouter_terroriste_aleatoire(T):
    n = len(T)
    m = len(T[0])
    i = randint(0, n-1)
    j = randint(0, m-1)
    T[i][j] = 3
    

def etape_suivante(T):
    global etape 
    if etape >= 1 :
        etape += 1 
    n = len(T)
    m = len(T[0])

    # Créer une copie temporaire de la grille pour les calculs
    nouvelle_generation = creer_tableau(n, m)

     # Créer une copie temporaire de la grille pour les calculs
    nouvelle_generation = creer_tableau(n, m)

    #ajout aléatoire d'un terroriste
    ajouter_terroriste_aleatoire(T)
    
    #parcourir la liste T
    for i in range(n):
        for j in range(m):
            # Compter le nombre de voisins noirs
            voisins = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if i + x >= 0 and i + x < n and j + y >= 0 and j + y < m :
                        if T[i +x][j+y] == 1 :
                            voisins += 1
            # Appliquer les règles de reproduction
            if T[i][j] == 0:
                # Si une cellule noire a exactement trois voisins noirs ou plus, elle se reproduit
                if voisins >= 3:
                    nouvelle_generation[i][j] = 1
            else:
                # Si une cellule vide a exactement trois voisins noirs, elle devient noire
                if voisins == 3:
                    nouvelle_generation[i][j] = 1

            # Si une cellule est entourée de 9 cases noires, elle devient rouge
            if T[i][j] == 1 and voisins == 9:
                nouvelle_generation[i][j] = 2
            # Les cellules vivantes ne changent pas 
            elif T[i][j] == 1:
                nouvelle_generation[i][j] = 1
             # Si une cellule est bleu, elle ne peut pas être changé
            if T[i][j] == 3 : 
                nouvelle_generation[i][j] = 4
            elif T[i][j] == 4 : 
                nouvelle_generation[i][j] = 5
            elif T[i][j] == 5 : 
                BOOM(T,i,j)
            

    for i in range(n):
        for j in range(m):
            T[i][j] = nouvelle_generation[i][j]
            # Vérifier si une cellule rouge a été créée il y a deux étapes et déclencher une explosion
            if T[i][j] == 3 and etape - T[i][j+1] == 2:
                BOOM(T, i, j)

def afficher_case(T, i, j,w ,h):
    ''' 
        T est un tableau à deux dimensions d'entiers
        i et j sont les coordonnées de la case à afficher
        c est la longueur (en pixels) du côté d'un carré
        w esd la largeur d'une cellule
        h est la hauteur d'une cellule
                
        Dessine la case de coordonnées (i, j).
    '''
    if T[i][j] == 1: 
        fill(0)
    elif T[i][j] == 0 :
        fill(255)
    elif T[i][j] == 2:
        fill(250,10,10)
    elif T[i][j] == 3:
        fill(10,10,170)
    elif T[i][j] == 4:
        fill(10,10,210)
    elif T[i][j] == 5:
        fill(10,10,255)
    rect(j*w,i*h,w,h)    
    
def afficher(T):
    '''
        T est un tableau à deux dimensions d'entiers
        
        Dessine toutes les cases du tableau.
    '''
    for i in range(len(T)): 
        for j in range(len(T[0])): 
            afficher_case(T,i, j,22,22)
    
        
def setup():
    global T, etape
    etape = 0
    T = creer_tableau(38, 64)
    T[12][12] = 1
    T[13][13] = 1
    T[12][14] = 1
    T[14][14] = 1
    T[15][14] = 1
    # Plein écran
    fullScreen()
    # Rapidité 
    frameRate(2)


def draw():
    global T, etape, Start
    strokeWeight(1)
    afficher(T)
    etape_suivante(T)


def mousePressed():
    global T, etape
    '''
    taille_cellule = min(width // 100, height // 50)
    
    # Convertir les coordonnées de la souris en indices de cellule
    while etape == 0:
        i = int(mouseY / taille_cellule)
        j = int(mouseX / taille_cellule)
        if mouseButton == LEFT:
            T[i][j] = 1
        elif mouseButton == RIGHT:
            T[i][j] = 0
    '''
