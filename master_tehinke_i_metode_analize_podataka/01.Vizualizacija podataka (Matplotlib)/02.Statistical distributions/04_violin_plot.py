"""
=============
violinplot(D)
=============

See `~matplotlib.axes.Axes.violinplot`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Generiše se skup od 100 podataka od po 3 atributa gde svaki atribut ima normalnu 
# raspodelu. Srednje vrednosti atributa su redom 3, 5 i 4, a njihove standardne 
# devijacije 0.75, 1.0 i 0.75.  
np.random.seed(10)
D = np.random.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Iscrtava "violin" dijagram sa zadatim parametrima
vp = ax.violinplot(D,  # skup podataka 
                     [2, 4, 6],  # pozicije po x osi gde će se prikazati svaki od atributa 
                     widths=1,   # maksimalna širina svake od violina
                     showmeans=True, showmedians=True, showextrema=True)
# Prethodna funkcija vraća dictionary koji sadrži prikazane objekte pa ovde mogu
# da se preuzmu tela violina i da im se podesi transparentnost. 
for body in vp['bodies']:
    body.set_alpha(0.5)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
