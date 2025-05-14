"""
==========
boxplot(X)
==========

See `~matplotlib.axes.Axes.boxplot`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Generiše se skup od 100 podataka od po 3 atributa gde svaki atribut ima normalnu 
# raspodelu. Srednje vrednosti atributa su redom 3, 5 i 4, a njihove standardne 
# devijacije 1.25, 1.0 i 1.5.  
np.random.seed(10)
D = np.random.normal((3, 5, 4), (1.25, 1.0, 1.25), (100, 3))

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Iscrtava "box and whiskers" dijagram sa zadatim parametrima
VP = ax.boxplot(D, # skup podataka
                positions=[2, 4, 6], # pozicije po x osi gde će se prikazati svaki od atributa 
                widths=1.5, # širina kućica ("boxova") po x osi 
                patch_artist=True, # True da bi se kućice iscrtavale korišćenjem Patch artista
                showmeans=True, # True da bi se prikazale i srednje vrednosti 
                showfliers=True, # True da bi se prikazali i podaci koji odstupaju od raspodele (outliers)
                medianprops={"color": "white", "linewidth": 1}, # atributi za iscrtavanje medijane
                boxprops={"facecolor": "blue", "edgecolor": "white", "linewidth": 0.5},
                # atributi za iscrtavanje kućica
                whiskerprops={"color": "red", "linewidth": 1.5}, # atributi za 
                # iscrtavanje "whiskers" linija između kućica 
                capprops={"color": "violet", "linewidth": 1.5}) # atributi za 
                # iscrtavanje početka 1. kvartila i kraja 4. kvartila

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
