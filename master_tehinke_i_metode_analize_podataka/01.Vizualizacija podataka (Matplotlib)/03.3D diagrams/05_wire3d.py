"""
=======================
plot_wireframe(X, Y, Z)
=======================

See `~mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe`.
"""
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

#plt.style.use('_mpl-gallery')

# Generišu se test podaci sa rastojanjem između tačaka po x i y osi od 0.05. 
X, Y, Z = axes3d.get_test_data(0.05)

# Kreira se objekat Figure i njemu pridruženi objekat Axes (3D koordinatni sistem)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


# Iscrtava se dijagram zavisnosti Z od X i Y. Parametri rstride i cstride definišu 
# rastojanja između linija po x i y osi, odnosno definišu mrežu po kojoj se 
# iscrtava funkcija. 
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

#ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()
