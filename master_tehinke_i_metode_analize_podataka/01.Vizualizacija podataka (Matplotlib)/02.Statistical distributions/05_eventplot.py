"""
============
eventplot(D)
============

See `~matplotlib.axes.Axes.eventplot`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Generiše se skup od 50 podataka od po 3 atributa gde svaki atribut ima gama  
# raspodelu. Parametar oblika gama raspodele je 4.  
np.random.seed(1)
D = np.random.gamma(4, size=(3, 50))
# Pozicije po x osi gde će se prikazati svaki od atributa. 
x = [2, 4, 6]

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Iscrtava se event dijagram nad zadatim podacima. 
ax.eventplot(D, orientation="vertical", lineoffsets=x, linewidth=0.75)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks).
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
