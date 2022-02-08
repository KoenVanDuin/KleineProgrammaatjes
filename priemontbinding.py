"""
Een code voor het ontbindingen van getallen in priemgetallen.
De ontbindingen worden in ontbindingen.txt geschreven.
"""

# TODO: Afficher "2 * 2 * 3" comme "2^2 * 3", et ainsi de suite.

# TODO: Tout ce code gagnerait à être rendu plus économe en temps.
#       Peut-être ça veut le coup de regarder comment rendre cette
#       fonction moins lente.

def estPremier(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def premiersInf(n):
    """Renvoie une liste contenant les premiers inférieurs à n"""
    retour = []
    for i in range(2,n+1):
        if estPremier(i):
            retour.append(i)
    return retour

def facteur():
    """
    fonction qui divise n par le plus petit premier
    par lequel on peut diviser.
    Elle rajoute chaque diviseur à la liste.
    Elle ne renvoie rien.
    """
    global n
    global diviseurs
    pI = premiersInf(n)
    for p in pI:
        if n % p == 0:
            n = int(n/p)
            diviseurs.append(p)
##    print("Hier komen de delers:")
##    print(diviseurs)
         
Max = 10**4 # Le nombre d'entiers dont on veut avoir la décomposition.

# Hier volgt de oude versie van miseEnForme.

##def miseEnForme(n,liste):
##    """Fonction mettant en forme un décomposition."""
##    if liste == []:
##        return "1\t=\t1\n"
##    retour = "{}\t=\t".format(n)
##    lengte = len(liste)
##    retour += str(liste[0])
##    for i in range(1,lengte):
##        retour += " * {}".format(liste[i])
##    return retour + "\n"

def miseEnForme(n,liste):
    """Fonction mettant en forme un décomposition."""
    if liste == []:
        return "1\t=\t1\n"
    liste.sort()
    retour = "{}\t=\t".format(n)
    lengte = len(liste)
    retour += str(liste[0])
    for i in range(1,lengte):
        retour += " * {}".format(liste[i])
    return retour + "\n"

##def miseEnForme2(n,liste):
##    """Deuxième fonction mettant en forme une décomposition."""
##    if liste == []:
##        return "1\t=\t1\n"
##    retour = "{}\t=\t".format(n)
##    lengte = len(liste)
##    retour += str(liste[0])
##    for i in range(1,lengte):
##        retour += " * {}".format(liste[i])
##    return retour + "\n" 
    
with open('ontbindingen.txt', 'w') as fichier:
    for n in range(1,Max+1):
        if n % 100 == 0:
            print(n)
        N = n   # Je mets de côté la valeur de départ de n.
        diviseurs = []
        # Ici je cherche tous les facteurs.
        while n != 1:
            facteur()
        fichier.write(miseEnForme(N,diviseurs))
        
print("fin du programme")

# TODO: Essayer d'ouvrir deux fichiers en même temps.
