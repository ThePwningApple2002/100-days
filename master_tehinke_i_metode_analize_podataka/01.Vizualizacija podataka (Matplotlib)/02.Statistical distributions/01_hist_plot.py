"""
=======
hist(x)
=======

See `~matplotlib.axes.Axes.hist`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Generiše se skup od 200 podataka sa normalnom raspodelom, čija je srednja 
# vrednost 4 i standardna devijacija 1.5. 
# np.random.seed(1)
x = np.random.normal(0, 4, 2500)

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Iscrtava se histogram nad skupom podataka x tako što se podaci grupišu u 8 
# opsega iste veličine ("binova"). Parametri linewidth i edgecolor definišu 
# izgled okvira na histogramu. 
ax.hist(x, bins=16)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks) od 0 do 57 (gornja granica se ne uključuje)
# sa korakom 7. 
ax.set(xlim=(-8, 8), xticks=np.arange(-8, 8), ylim=(0, 1000), yticks=np.arange(0, 1000, 10))

plt.show()
