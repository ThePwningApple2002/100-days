"""
===============
hexbin(x, y, C)
===============

See `~matplotlib.axes.Axes.hexbin`.
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

# Iscrtava se slično kao 2D histogram sa tom razlikom što su binovi nisu kvadratni
# nego su šestougaoni. Parametar gridsize zadaje broj binova po x osi. Broj binova 
# po y osi računa sama funkcija tako da se dobiju pravilni šestouglovi. Na 
# dijagramu svaki bin dobija boju prema broju podataka koji sadrži. 
ax.hexbin(x, y, gridsize=30)

# Granice za prikaz po x osi su -2 i 2, a po y osi -3 i 3.
ax.set(xlim=(-2, 2), ylim=(-3, 3))

plt.show()
