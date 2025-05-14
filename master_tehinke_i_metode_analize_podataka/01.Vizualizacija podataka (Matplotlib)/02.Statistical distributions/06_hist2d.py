"""
============
hist2d(x, y)
============

See `~matplotlib.axes.Axes.hist2d`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery-nogrid')

# Generisanje podataka
np.random.seed(1)
# Promenljiva x se generiše kao niz od 5000 elemenata sa normalnom raspodelom 
# čija je srednja vrednost 0 i standardna devijacija 1. 
x = np.random.randn(5000)
# Promenljiva y ima jednu komponentu koja je u korelaciji sa x i drugu manju 
# slučajnu komponentu (šum)
y = 1.2 * x + np.random.randn(5000) / 3

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Iscrtava se 2D histogram sa promenljivama x i y tako što se kreiraju zadati 
# binovi po x i po y osi. Na dijagramu svaki bin dobija boju prema broju podataka
# koji sadrži. 
ax.hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))

# Granice za prikaz po x osi su -2 i 2, a po y osi -3 i 3. 
ax.set(xlim=(-2, 2), ylim=(-3, 3))

plt.show()
