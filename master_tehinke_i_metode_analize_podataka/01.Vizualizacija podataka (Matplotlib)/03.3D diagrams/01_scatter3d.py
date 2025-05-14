"""
===================
scatter(xs, ys, zs)
===================

See `~mpl_toolkits.mplot3d.axes3d.Axes3D.scatter`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Generisanje podataka
np.random.seed(19680801)
n = 100
# Generiše se po 100 elemenata u nizovma xs, ys, zs sa uniformnom raspodelom.  
rng = np.random.default_rng()
xs = rng.uniform(23, 32, n)
ys = rng.uniform(0, 100, n)
zs = rng.uniform(-50, -25, n)

# Kreira se objekat Figure i njemu pridruženi objekat Axes (3D koordinatni sistem)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Iscrtava se dijagram rasipanja sa zadatim nizovima. 
ax.scatter(xs, ys, zs)

#ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()
