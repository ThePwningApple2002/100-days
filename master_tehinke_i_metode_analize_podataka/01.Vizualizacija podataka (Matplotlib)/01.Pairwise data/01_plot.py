"""
==========
plot(x, y)
==========

See `~matplotlib.axes.Axes.plot`.
"""

import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery')

# Generisanje podataka
# Podaci za nezavisnu promenljivu x se generišu pozivom funkcije linspace koja 
# vraća niz od 100 realnih brojeva na podjednakom međusobnom rastojanju  
# iz intervala od 0 do 100 uključujući i donju i gornju granicu intervala.
x = np.linspace(0, 15, 100)  
# Podaci za zavisnu promenljivu y se generišu po sledećoj formuli
y = 4 + 2 * np.sin(2 * x)

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots() 
plt.grid(True)  # Prikazuje se mreža u pozadini
# Poziva se funkcija plot sa zadatim nizovima vrednostima za x i y i sa zadatom 
# debljinom linije.  
ax.plot(x, y, linewidth=5.0)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 9 (gornja granica 9 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks) 
ax.set(xlim=(0, 14), xticks=np.arange(1, 15), ylim=(0, 8), yticks=np.arange(1, 9))

plt.show()
