"""
Deze code bevat een functie die de eerste alle priemgetallen onder
de in de parameter aangegevern bovengrens in een lijst terugstuurt.
Hij gebruikt hiervoor de schrapmethode:
We beginnen met een lijst list(range(2,N)), veelvouden van priemgetallen
worden geschrapt, zodat de overblijvende getallen als priemgetallen
kunnen worden herkend.
"""

import numpy as np

def getPriemen(N):

    priemen = []
    
    zoeklijst = list(range(2,N+1))

    while zoeklijst != []:
        priem = zoeklijst[0]
        priemen.append(priem)
        ##print("We voegen {} toe aan de priemenlijst.".format(priem))
    ##    sleep(1)
        ##print("")
        zin = "We gaan tot en met {}."
        ##print(zin.format(int(np.ceil(N/priem))))
        ##print(list(range(1,int(np.ceil(N/priem)))))
        # Hier schrappen we veelvouden van het priemgetal.
        for k in range(1,int(np.ceil(N/priem))+1):
            ##print("We zitten nu op k = {}.".format(k))
            veelvoud = k * priem
            if veelvoud in zoeklijst:
                zoeklijst.remove(veelvoud)
                ##print("We verwijderen {}".format(veelvoud))
            else:
                zin = "{} not in {}, kennelijk."
                ##print(zin.format(veelvoud,zoeklijst))

    # Als de zoeklijst leeg is, dan hebben we alle priemgetallen gehad.
    return priemen

