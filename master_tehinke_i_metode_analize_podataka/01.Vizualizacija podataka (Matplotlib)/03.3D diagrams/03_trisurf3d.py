"""
=====================
plot_trisurf(x, y, z)
=====================

See `~mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf`.
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

#plt.style.use('_mpl-gallery')

# Generisanje podataka
# Kreira se niz od 8 vrednosti za radijus u polarnim koordinatama. 
radii = np.linspace(0.125, 1.0, 8)
# Kreira se niz od 36 vrednosti za ugao u polarnim koordinatama. Taj niz se 
# odmah formatira kao vektor-kolona. 
angles = np.linspace(0, 2*np.pi, 36, endpoint=False)[..., np.newaxis]

# Konverzija polarnih (radii, angles) u Dekartkove koordinate (x, y). Množenjem 
# se dobijaju matrice dimenzija 36x8 čiji se elementi kasnije funkcijom flatten 
# prebacuju u običan niz. Na početku oba niza dodaje se koordinata 0.  
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())
# Koridnata z se računa kao funkcija koordinata x i y. 
z = np.sin(-x*y)

# Kreira se objekat Figure i njemu pridruženi objekat Axes (3D koordinatni sistem)
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

# Funkcija plot_trisurf kreira površinu u 3D prostoru od prosleđenih koordinata 
# tako što koristi metodu triangulacije (povezivanje 3 susedne tačke u jedan 
# trougao.   
ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)

#ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()
