import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Učitavanje skupa podataka
data = pd.read_csv('tripadvisor_review_FULL.csv')
print(data.head())

# Izbacivanje atributa "User ID" tako da su svi preostali 
# atributi realni brojevi. 
data.drop(columns="User ID", inplace=True)
print(data.head())
print(data.describe())

# Skaliranje podataka tako da se svaki atribut preslikava u opseg od 0 do 1. 
mms = MinMaxScaler()
mms.fit(data)
data_transformed = mms.transform(data)
data_transformed_df = pd.DataFrame(data_transformed, columns=data.columns)  
print(data_transformed_df.describe())

# "Elbow" metod za pronalaženje optimalnog broja klastera. Isprobava se 
# klasterizacija sa brojem klastera K od 1 do 10. Iscrtava se grafik sume 
# kvadrata rastojanja (elemenata svakog od klastera do odgovarajućeg centroida).   
Sum_of_squared_distances = []
K = range(1,10)
for k in K:
    km = KMeans(n_clusters=k, n_init=10)
    km = km.fit(data_transformed)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-') # bx je za plave krstice
plt.xlabel('k')
plt.ylabel('Suma kvadrata razdaljina')
plt.title('Metoda lakta za nalaženje k')
plt.show()

# Za optimalni broj klastera uzima se 3 jer tu prethodna kriva ima "lakat", tj. 
# za veće vrednosti K se ne dobija značajno poboljšanje. Parametar n_init=10 
# određuje broj ponavljanja algoritma sa različitim početnim centroidima 
# izabranim na slučajan način. 
km = KMeans(n_clusters=3, n_init=10, random_state=11)
km.fit(data_transformed)

color_theme=np.array(['lightgray', 'lightsalmon', 'powderblue'])

# Prikaz različitih klastera u 2D u funkciji od atibuta letnji barovi i 
# atributa pozorista. Prikazuju se podaci na originalnoj skali, pre primene 
# min-max skaliranja. 
plt.scatter(x=data.iloc[:, 2], y=data.theaters, c=color_theme[km.labels_], s=50)
plt.title('K-Means klasterizacija')
plt.show()

# Prikaz različitih klastera u 3D u funkciji od sledećih atibuta:  
# letnji barovi, pozorista, hramovi. Prikazuju se podaci na originalnoj skali, 
# pre primene min-max skaliranja.  
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(data.iloc[:, 2], data.iloc[:, 8], data.iloc[:, 9], c=color_theme[km.labels_])
plt.show()

print(km.cluster_centers_)

# Isto kao i prethodni dijagram, samo što se sada prikazuju skalirani podaci i 
# dodatno se iscrtavaju i centroidi. 
fig_transformed, ax_transformed = plt.subplots(subplot_kw={"projection": "3d"})
ax_transformed.scatter(data_transformed[:, 2], data_transformed[:, 8], data_transformed[:, 9],
                       c=color_theme[km.labels_])
# obelezavamo polozaje centroida
C = km.cluster_centers_
ax_transformed.scatter(C[:, 2], C[:, 8], C[:, 9], marker='*', c='#050505', s=100)
plt.show()