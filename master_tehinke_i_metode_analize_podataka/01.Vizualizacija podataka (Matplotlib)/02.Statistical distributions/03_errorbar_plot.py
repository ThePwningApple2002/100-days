"""
==========================
errorbar(x, y, yerr, xerr)
==========================

See `~matplotlib.axes.Axes.errorbar`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Koordinate tačaka po x i y osi.  
x = [2, 4, 6]
y = [3.6, 5, 4.2]
# Intervali greške po x i y osi. 
xerr = [0.5, 0.8, 1.0]
yerr = [0.9, 1.2, 0.5]

# Kreira se objekat Figure i njemu pridruženi objekat Axes (koordinatni sistem)
fig, ax = plt.subplots()

# Funkciji axes.errorbar se prosleđuju koordinate podataka, greške po y i x osi, 
# fmt je format za prikaz tačaka ('o' znači kružić), linewidth je debljina linije,
# a capsize je dužina crtica na krajevima linija.  
ax.errorbar(x, y, yerr, xerr, fmt='o', linewidth=2, capsize=6)

# Postavlja se oblast koja će se prikazati po x-osi (xlim), podeoci po x osi (xticks)
# od 1 do 8 (gornja granica 8 se ne uključuje), oblast koja će se prikazati po y-osi 
# (ylim) i podeoci po y osi (yticks)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
