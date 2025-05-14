"""
==========
stem(x, y)
==========

See `~matplotlib.axes.Axes.stem`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Nezavisna promenljiva x se generiše pozivom metode np.arange(8) koja vraća 
# celobrojne vrednosti od 0 zaključno sa 7.
x = 0.5 + np.arange(8)
# Promenljiva y se zadaje direktno kao niz od 8 elemenata.
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Funckiji axes.stem se prosleđuju nizovi podataka x i y.
ax.stem(x, y)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
