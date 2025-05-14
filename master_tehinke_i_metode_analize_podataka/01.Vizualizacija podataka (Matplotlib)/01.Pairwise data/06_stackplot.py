"""
===============
stackplot(x, y)
===============
See `~matplotlib.axes.Axes.stackplot`
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Podaci za nezavisnu promenljivu x se generišu pozivom funkcije np.arrange koja 
# vraća niz brojeva od 0 (uključujući donju granicu) do 10 (ne uključujući gornju 
# granicu), na podjednakom međusobnom rastojanju 2. 
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
# Funkcija np.vstack kreira matricu u kojoj su vrste ay (vrsta sa indeksom 0), 
# by (vrsta sa indeksom 1), cy (vrsta sa indeksom 2). 
y = np.vstack([ay, by, cy])
print(y)    
# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()    

# Funkciji stackplot se prosleđuje nezavisna promenljiva x i matrica "naslaganih" 
# vrednosti po y osi. 
ax.stackplot(x, y)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
