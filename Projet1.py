from random import*
'''
Indiquez ici 

- évolution d'une population
- le code couleur utilisé (légende)
- les règles de votre automate cellulaire (pas la peine de détailler)
'''

def creer_tableau(n, m):
    T = list()
    for j in range(n):
        M = list()
        for i in range(m):
            M.append(0)
        T.append(M)
    return T  

def ajouter_case_noire_aleatoire(T):
    n = len(T)
    m = len(T[0])
    i = randint(0, n-1)
    j = randint(0, m-1)
    T[i][j] = 1

def etape_suivante(T):
    global etape 
    etape += 1 
    n = len(T)
    m = len(T[0])

    # Créer une copie temporaire de la grille pour les calculs
    nouvelle_generation = creer_tableau(n, m)

    for i in range(n):
        for j in range(m):
            # Compter le nombre de voisins noirs
            voisins = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if i + x >= 0 and i + x < n and j + y >= 0 and j + y < m and (x != 0 or y != 0):
                        voisins += T[i + x][j + y]

            # Appliquer les règles de reproduction
            if T[i][j] == 1:
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
            # Les cellules vivantes restent inchangées
            elif T[i][j] == 1:
                nouvelle_generation[i][j] = 1

    # Mettre à jour la grille originale avec la nouvelle génération
    for i in range(n):
        for j in range(m):
            T[i][j] = nouvelle_generation[i][j]
    if randint(0,5) == 1 :
        ajouter_case_noire_aleatoire(T)

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
    
    rect(j*w,i*h,w,h)    
    
def afficher(T):
    '''
        T est un tableau à deux dimensions d'entiers
        
        Dessine toutes les cases du tableau.
    '''
    for i in range(len(T)): 
        for j in range(len(T[0])): 
            afficher_case(T,i, j, width/len(T[0]), height/len(T))
    
        
def setup():
    global T, etape
    etape = 0
    T = creer_tableau(40, 35)
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
