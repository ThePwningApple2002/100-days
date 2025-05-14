"""
=====================
plot_surface(X, Y, Z)
=====================

See `~mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface`.
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Nizovi x i z se generišu kao nizovi realnih brojeva u intervalu [-5, 5) na međusobnom 
# rastojanju 0.25.  
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
# Od dva niza sa po n elemenata se kreira koordinatna mreža sa n*n tačaka. 
# X je matrica x koordinata generisanih tačaka, a Y je matrica y koordinata 
# generisanih tačaka.    
X, Y = np.meshgrid(x, y)
# R je matrica rastojanja od koordinatnog početka za svaku od tačaka. 
R = X**2 + Y**2
# Z je matrica sinusa prethodnih rastojanja. 
# Z = np.sin(R)


# Kreira se objekat Figure i njemu pridruženi objekat Axes (3D koordinatni sistem)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Iscrtava se dijagram funkcije Z u zavisnosti od X i Y. 
ax.plot_surface(X, Y, R,
                vmin=R.min() * 2, # parametar za normalizaciju
                cmap=cm.Blues)    # mapa boja u koje će se mapirati različite vrednosti funkcije


#ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()
