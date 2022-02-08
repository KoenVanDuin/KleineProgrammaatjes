"""
In deze code gebruik ik de hoog/laag-methode om een nulpunt
van een functie te vinden.
"""

# Les données sur lesquelles je vais "lacher" mes fonctions tout à l'heure.
def functie(x):
    """Onze (eerste) testfunctie."""
    return x**2-2

a = 0
b = 5

def iteratie(f):
    """
    Met deze functie kunnen we één iteratie uitvoeren
    van het hoog/laag-alogrithme.
    De getallen moeten zo worden gekozen dat f(a) <= 0 <= f(b).
    Dit is geen beperking van de algemeenheid omdat we f
    door -f kunnen vervangen.
    """
    # Eerst kijken we of de getallen "goed" zijn.
    if not f(a) <= 0 and f(b) >= 0:
        print(f(a))
        print(f(b))
        raise ValueError("Les nombres a, b sont mal choisis !")
    # Nu is alles goed en kunnen we (a,b) bewerken.
    m = float((a+b)/2)
    global a
    global b
    if f(m) > 0:
        b = m
    else:
        a = m
    return

def hoogLaag(f,N):
    """
    De functie waarmee we de hoog-laagmethode uitvoeren.
    """
    for k in range(N):
        iteratie(f)
        print("a = {}, \t b = {}, \t, f(m) = {}".format(a,b,f((a+b)/2)))
        # TODO: mieux afficher toutes les données.


# TODO: Convergentiesnelheid en rekentijd bepalen.

print("Ici je fais mes essais.")
print("-"*72)

hoogLaag(functie,20)
print("Nu kijken we wat de fout is:")
print(a**2-2)

    
        

