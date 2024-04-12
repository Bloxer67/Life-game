from random import*
'''
Indiquez ici 

- évolution d'une population
- le code couleur utilisé (légende)
- les règles de votre automate cellulaire (pas la peine de détailler)
'''

Start = False


def creer_tableau(n, m):
    T = list()
    for j in range(n):
        M = list()
        for i in range(m):
            M.append(0)
        T.append(M)
    return T  

def etape_suivante(T):
    global etape
    etape += 1 
    n = len(T)
    m = len(T[0])

    # Parcourir le tableau
    for i in range(n):
        for j in range(m):
            # Compter le nombre de voisins noirs
            black_neighbors = 0
            for x in range(max(0, i-1), min(n, i+2)):
                for y in range(max(0, j-1), min(m, j+2)):
                    if T[x][y] == 1 and (x != i or y != j):
                        black_neighbors += 1

            # Appliquer les règles du jeu de la vie de Conway
            if T[i][j] == 1:
                if black_neighbors != 2 and black_neighbors != 3:
                    T[i][j] = 0
            else:
                if black_neighbors == 3:
                    T[i][j] = 1
    

    
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
    else :
        fill(255)
    
    rect(j*w,i*h,w,h)    
    
def afficher(T):
    '''
        T est un tableau à deux dimensions d'entiers
        
        Dessine toutes les cases du tableau.
    '''
    for i in range(len(T)): 
        for j in range(len(T[0])): 
            afficher_case(T,i, j, 30, 30)
    
        
def setup():
    global T, etape
    etape = 0
    T = creer_tableau(50, 60)
    T[12][12] = 1
    # Plein écran
    fullScreen()
    # Rapidité 
    frameRate(2)
    

def draw():
    global T, etape, Start
    strokeWeight(1)
    afficher(T)
    if not Start : 
        text("Sélectionnez les cellules (clic gauche pour vivante, clic droit pour morte)", 20, 20)
        rect(displayWidth - 40 ,displayHeight - 30,100,40)
        fill(0)
        textSize(16)
        textAlign(CENTER)
        text("Start", displayWidth - 30, displayHeight - 20)
    else :
        etape_suivante(T)
    
def demarrer_simulation():
    global Start
    Start = True
    


def mousePressed():
    global T, etape, Start

    taille_cellule = min(displayWidth // 100, displayHeight // 50)
    
    # Convertir les coordonnées de la souris en indices de cellule
    
    if not Start:
        i = int(mouseY / taille_cellule)
        j = int(mouseX / taille_cellule)
        if mouseButton == LEFT:
            T[i][j] = 1
        elif mouseButton == RIGHT:
            T[i][j] = 0
    elif:
        exit()

