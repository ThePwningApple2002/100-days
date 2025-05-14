"""
==============
stairs(values)
==============

See `~matplotlib.axes.Axes.stairs`.

.. redirect-from:: /plot_types/basic/step
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Niz granica stepenica mora da ima 1 element više u odnosu na niz vrednosti.
x = [0., 1.5, 2., 3.5, 4., 5.5, 6., 7.5, 8.]
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Funkciji za iscrtavanje stepenastog dijagrama se prosleđuje niz vrednosti y,
# niz granica vrednosti x i debljina linije. 
ax.stairs(values=y, edges=x, linewidth=2.5)
# Ako se funciji ne prosledi niz granica vrednosti podrazumeva se niz granica
# [0., 1., 2., 3., 4.,...  
#axes.stairs(values=y, linewidth=2.5)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
