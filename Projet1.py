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

def etape_suivante(T):
    global etape 
    n = len(T)
    m = len(T[0])
    for i in range(n):
        for j in range(m):
            if T[i][j] == 1:
                # Mettre à jour les cellules voisines

    etape += 1


    
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
    background(255)
    T = creer_tableau(50, 100)
    T[12][12] = 1
    # Plein écran
    fullScreen()
    # Rapidité 
    frameRate(2)
    

def draw():
    global T, etape
    strokeWeight(1)
    afficher(T)
    etape_suivante(T)
    
def mousePressed():
    exit()
 

