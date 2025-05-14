"""
=============
scatter(x, y)
=============

See `~matplotlib.axes.Axes.scatter`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
np.random.seed(3)
# Nezavisna promenljiva x se generiše kao niz slučajnih podataka sa normalnom 
# raspodelom (prvi argument funkcije je srednja vrednost normalne raspodele, drugi 
# argument je standardna devijacija normalne raspodele, treći argument je broj 
# podataka koji će biti generisan. 
x = 4 + np.random.normal(0, 2, 24)
# Promenljiva y se generiše na sličan način i tako da ima isti broj podataka kao 
# i promenljiva x. 
y = 4 + np.random.normal(0, 2, len(x))
# Generiše se niz veličina krugova na dijagramu rasipanja i to kao niz slučajnih 
# podataka sa uniformnom raspodelom. 
# sizes = np.random.uniform(15, 80, len(x))
# Generiše se niz boja krugova na dijagramu rasipanja i to kao niz slučajnih 
# podataka sa uniformnom raspodelom. 
# colors = np.random.uniform(15, 80, len(x))

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

plt.grid(True)  # Prikazuje se mreža u pozadini
# Kreira se dijagram rasipanja sa zadatim argumentima. 
ax.scatter(x, y,  vmin=0, vmax=100)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 9 (gornja granica 9 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks) 
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
