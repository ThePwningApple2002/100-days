"""
======
pie(x)
======

See `~matplotlib.axes.Axes.pie`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery-nogrid')


# Generisanje podataka
x = [1, 2, 3, 4]
# Iz mape boja se uzimaju 4 nijanse plave boje
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Iscrtava se pie dijagram nad podacima x, bojama iz niza colors, poluprečnika 3, 
# sa centrom u tački (4, 4). Parametar wedgeprops definiše izgled kružnih 
# isečaka na dijagramu.  
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks).
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
