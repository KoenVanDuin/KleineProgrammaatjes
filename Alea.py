"""
Hier speel ik met threads.
Ik laat meerdere stochastische wandelingen samenlopen op een rooster
en interageren als ze botsen.
Ik heb dit jammer genoeg vrijwel geheel in het Frans gedaan.
In de terminal te starten om het gebeuren het meest inzichtelijk te houden.
"""

import os
import sys
from time import sleep	
import random
from threading import Thread, RLock
from random import expovariate

# Les constantes.
DIM = 10
DUREE = 50
INFO = False
RELEVE = False

verrou = RLock()

class Meurtre:
    """
    Chaque fois qu'une puce en mange une autre,
    on crée un objet de ce type.
    """
    # TODO: Finir cette classe.

    lesMeurtres = [] # On range tous les meurtres là-dedans.

    def __init__(self,meurtrier,victime):
        self.meurtrier = meurtrier
        self.victime = victime
        Meurtre.lesMeurtres.append(self)

    def fantome():
        taille = len(Meurtre.lesMeurtres)
        chaine = ""
        ajout = "\nLa puce morte {} a mangé {}."
        lesMeurtriers = [meurtre.meurtrier for meurtre in Meurtre.lesMeurtres]
        lesVictimes = [meurtre.victime for meurtre in Meurtre.lesMeurtres] 
        for k in range(taille):
            if lesMeurtriers[k] in lesVictimes[:k]:
                chaine += ajout.format(lesMeurtriers[k],lesVictimes[k])
            if lesVictimes[k] in lesVictimes[:k]:
                chaine += "\nLa puce morte {} a encore été mangé !"
        return chaine
            
        

    def __repr__(self):
        return "{} mange {}".format(self.meurtrier,self.victime)


# J'aurai besoin de l'alphabet pour reprÃ©senter les puces.
alfabet = list("abcedfghijlkmnopqrstuvwxyz".upper())

def info(chaine):
    """Fonction d'affichage pour dÃ©boguer plus aisÃ©ment."""
    mot = "INFO: \t{}".format(chaine)
    if INFO:
        print(mot)

class ParoiException(Exception):
    """
    L'exception qu'on lève quand la puce se heurte
    au bord du tableau.
    """
    def __init__(self):
        pass

    def __str__(self):
        return "La puce ne peut pas aller plus loin."

class PuceException(Exception):
    """
    L'exception qu'on lève quand la puce se heurte
    à une autre puce.
    """

    def __init__(self,x,y):
        # Les coordonnées sont celles de l'autre puce.
        self.x = x
        self.y = y

    def __str__(self):
        retour = "La puce doit s'arrêter devant la case ({},{})."
        return retour.format(self.x,self.y)

puceListe = []

class Puce:
    """
    Une Puce se caractÃ©rise par son aspect,
    par la taille des bonds qu'elle fait,
    par sa "promptitude" Ã  bouger,
    et par l'endroit sur l'Ã©chiquier oÃ¹ elle se trouve.    
    """

    def laPuce(x,y):
        """Renvoie la puce qui se trouve sur la case (x,y)."""
        for puce in puceListe:
            if (x,y) == (puce.x,puce.y):
                return puce
    
    def __init__(self,x,y,sigma=1,labda=1):
        """Le constructeur paramÃ©trÃ© de cette classe."""
        self.symbole = 2 * alfabet[len(puceListe)%26]
        self.sigma = sigma  # fixe la taille des bonds qu'elle fait.
        self.labda = labda   # fixe la vitesse de la puce.
        self.x = x
        self.y = y
        puceListe.append(self)
        

    def __repr__(self):
        return self.symbole

    def expose(self):
        retour = "La puce {} se trouve sur ({},{})"
        return retour.format(self,self.x,self.y)
        
    def bondis(self):
        info("bondis est appelé")
        tailleBond = int(random.gauss(3,self.sigma))
        sens = random.choice(PointCard.listePC)
        for pC in PointCard.listePC:
            if sens == pC:
                compteur = 0
                while compteur < tailleBond:
                    xN = pC.fDep(self.x,self.y)[0]
                    yN = pC.fDep(self.x,self.y)[1]
                    mot = "La puce {} peut se déplacer vers ({},{}) ?"
                    levePuce(xN,yN)
                    leveParoi(xN,yN)
                    compteur += 1
                    self.x = xN
                    self.y = yN
                    os.system("cls")
                    affiche()
                releve()


    def laPuce(x,y):
        """Renvoie la puce qui se trouve sur la case (x,y)."""
        for puce in puceListe:
            if (x,y) == (puce.x,puce.y):
                return puce
    

def leveParoi(x,y):
    """
    Ceci est une fonction qui lève une exception quand
    les coordonnées fournies ne correspondent à acune case.
    """
    if x not in list(range(DIM)):
        raise ParoiException
    if y not in list(range(DIM)):
        raise ParoiException

def levePuce(x,y):
    """
    Ceci est une fonction qui lève une exception quand
    il y a déjà une puce ayant les coordonnées précisées.
    """
    for puce in puceListe:
        if (x,y) == (puce.x,puce.y):
            raise PuceException(x,y)
                   
def pasNord(x,y):
    return (x,y+1)

def pasEst(x,y):
    return (x+1,y)

def pasSud(x,y):
    return (x,y-1)

def pasOuest(x,y):
    return (x-1,y)

class PointCard:
    """
    Les sens dans lesquels les puces peuvent bondir.
    Cette classe permet de rendre le code plus joli.
    """
    listePC = [] # On mettra tous les points cardinaux dans cette liste.
    
    def __init__(self,fDep):
        self.fDep = fDep
        PointCard.listePC.append(self)

# Ici je crÃ©e tous les points cardinaux.
N = PointCard(pasNord)
O = PointCard(pasEst)
Z = PointCard(pasSud)
W = PointCard(pasOuest)

def Y(y):
    """Un petit changement de coordonnÃ©es."""
    return DIM-y-1

# Voici deux fonctions d'affichage:

def affiche():
    """Une fonction qui affiche la grille avec toutes les puces."""
    print("\n"*8)
    print("__" * (DIM + 1))
    for y in range(DIM):
        ligne = "|"
        for x in range(DIM):
            pasDePuce = True
            for puce in puceListe:
                if (puce.x,puce.y) == (x,Y(y)):
                    ligne += puce.symbole
                    pasDePuce = False
            if pasDePuce:
                ligne += "  "
            pasDePuce = True
        ligne += "|"
        print(ligne)
    print("--" * (DIM + 1))

def releve():
    """Fonction qui affiche toutes les puces."""
    if not RELEVE:
        return
    for puce in puceListe:
        print(puce)
    print("/"*25)
    

class Fil(Thread):
    """Une unité de traitement qui fait bondir une puce."""
    
    def __init__(self, puce):
        Thread.__init__(self)
        self.puce = puce
        
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        """
        Laisse une puce faire des sauts de maniere alÃ©atoire.
        Quand elle aura fait N sauts, elle arrête de bouger.
        """
        compteur = 0
        while compteur < DUREE:
            if self.puce not in puceListe:
                return
            sleep(expovariate(self.puce.labda))
            with verrou:
                compteur += 1
                try:
                    self.puce.bondis()
                except PuceException as e:
                    mange = random.choice([True,False])                    
                    if mange:
                        autrePuce = Puce.laPuce(e.x,e.y)
                        info("{} mange {}".format(self.puce,autrePuce))
                        puceListe.remove(autrePuce)
                        del autrePuce
                except ParoiException as e:
                    pass

    def __repr__(self):
        retour = "Voici le fil qui fait bouger {}.\n".format(self.puce)
        if self.puce in puceListe:
            retour += "La puce s'est maintenue.\n"
        else:
            retour += "La puce a dû être mangée.\n\n"
        return retour
        
# ---------------------------------------------------------
print("Ici je fais mes essais.")
print("-"*78)

N = 20
for x in range(N):
    for y in range(N):
        Puce(x,y,labda=3)
        
desFils = {}
for puce in puceListe:
    desFils[puce] = Fil(puce)

for fil in desFils.values():
    fil.start()

for fil in desFils.values():
    fil.join()

for fil in desFils.values():
    print(fil)
    
input("Appuyez sur ENTREE pour terminer le programme.")
