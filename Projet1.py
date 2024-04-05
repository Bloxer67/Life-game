
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
    ''' 
        T est un tableau à deux dimensions d'entiers
        
        Modifie chaque cellule du tableau en fonction des
        cellules voisines
    ''' 
    pass      
                
    
def afficher_case(T, i, j):
    global w,h
    ''' 
        T est un tableau à deux dimensions d'entiers
        i et j sont les coordonnées de la case à afficher
        c est la longueur (en pixels) du côté d'un carré
        w esd la largeur d'une cellule
        h est la hauteur d'une cellule
                
        Dessine la case de coordonnées (i, j).
    '''
    
    rect(j*w,i*h,w,h)    
    
def afficher(T):
    global w,h
    '''
        T est un tableau à deux dimensions d'entiers
        
        Dessine toutes les cases du tableau.
    '''
    for i in range(len(T)): 
        for j in range(len(T[0])): 
            rect(j*w, i*h, w, h)
    

        
    
def setup():
    global T, etape, w, h
    background(255)
    T = creer_tableau(50, 100)
    # Plein écran
    fullScreen()
    w = 30
    h = 30
    # Rapidité 
    frameRate(2)
    
def draw():
    global T, etape
    afficher(T)
    
    
def mousePressed():
    exit()
    
 

