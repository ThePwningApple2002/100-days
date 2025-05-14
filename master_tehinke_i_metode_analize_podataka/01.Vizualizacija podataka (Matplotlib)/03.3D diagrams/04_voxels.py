"""
=========================
voxels([x, y, z], filled)
=========================

See `~mpl_toolkits.mplot3d.axes3d.Axes3D.voxels`.
"""
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# Za svaku od koordinata kreira se matrica mogućih vrednosti dimenzija 8 x 8 x 8. 
x, y, z = np.indices((8, 8, 8))

# Definišu se kocke u gornjem levom i donjem desnom uglu. Elementi kocki su logičke 
# vrednosti True ili False. 
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)

# Dva objekta se kombinuju u jednu bulovsku matricu. 
voxelarray = cube1 | cube2

# Kreira se objekat Figure i njemu pridruženi objekat Axes (3D koordinatni sistem)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Iscrtavaju se definisane kocke. 
ax.voxels(voxelarray, edgecolor='k')

#ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()
