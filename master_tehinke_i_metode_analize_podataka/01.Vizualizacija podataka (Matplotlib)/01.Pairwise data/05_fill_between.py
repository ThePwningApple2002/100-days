"""
=======================
fill_between(x, y1, y2)
=======================

See `~matplotlib.axes.Axes.fill_between`.
"""

import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Podaci za nezavisnu promenljivu x se generišu pozivom funkcije linspace koja 
# vraća niz od 17 realnih brojeva na podjednakom međusobnom rastojanju  
# iz intervala od 0 do 8 uključujući i donju i gornju granicu intervala.
# [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8. ]
x = np.linspace(0, 8, 17)
# Inicijalizacija random generatora. 
np.random.seed(1)
# Promenljive y1 i y2 predstavljaju granice oblasti koja se ispunjava bojom. 
# Kod obe promenljive prva dva člana predstavljaju pravu liniju, a treći član je 
# slučajno generisan po uniformnoj raspodeli u opsegu 0.0 do 0.5.   
y1 = 3 + 0.5*x + np.random.uniform(0.0, 0.5, len(x))
y2 = 1 + 0.25*x + np.random.uniform(0.0, 0.5, len(x))

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()
# Oblast između funkcija y1 i y2 se ispunjava bojom čija je transparentnost 
# zadata vrednošću alpha. 
ax.fill_between(x, y1, y2, alpha=0.1)
# Iscrtava se obična linija debljine 2 na sredini oblasti između y1 i y2 koja je 
# prethodno ispunjena bojom. 
ax.plot(x, (y1 + y2)/2+3, linewidth=2)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
