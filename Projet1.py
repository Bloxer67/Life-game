
'''
Indiquez ici :

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
    print(T) 

def etape_suivante(T):
    ''' 
        T est un tableau à deux dimensions d'entiers
        
        Modifie chaque cellule du tableau en fonction des
        cellules voisines
    ''' 
    pass      
                
    
def afficher_case(T, i, j, w, h):
    ''' 
        T est un tableau à deux dimensions d'entiers
        i et j sont les coordonnées de la case à afficher
        c est la longueur (en pixels) du côté d'un carré
        w esd la largeur d'une cellule
        h est la hauteur d'une cellule
                
        Dessine la case de coordonnées (i, j).
    '''
    pass
    
def afficher(T):
    '''
        T est un tableau à deux dimensions d'entiers
        
        Dessine toutes les cases du tableau.
    '''
    pass
        
    
def setup():
    global T, etape
    
    # Plein écran
    fullScreen()
    
    # Rapidité 
    frameRate(2)
        
def draw():
    global T, etape
    
def mousePressed():
    exit()
    
 
creer_tableau(5, 6)
