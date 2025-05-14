import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn import preprocessing

# Učitavanje skupa podataka (koristi se skraćeni skup podataka u odnosu na 
# K-Means primer. 
data = pd.read_csv('tripadvisor_review.csv')

# Izbacivanje atributa "User ID" tako da su svi preostali 
# atributi realni brojevi.
data.drop(columns="User ID", inplace=True)
data.columns = ['art_galleries', 'dance_clubs', 'juice_bars', 'restaurants',
                   'museums', 'resorts', 'parks', 'beaches',
                   'theaters', 'religious_institutions']
print(data.head())

# Kreira se model za hijerarhijsko klasterovanje. 
clustering = AgglomerativeClustering(linkage="ward", n_clusters=3)
clustering.fit(data);

# Koristi se MinMax skaliranje tako da se podaci za prikaz preslikavaju u 
# opseg 0.0-1.0 za prikaz. Funkcija fit_transform prilagođava sklaliranje 
# podacima pa onda nad tim istim podacima primenjuje skaliranje (identično kao 
# da se prvo pozove funkcija fit pa zatim funkcija transform sa istim argumentom.  
data_plot = preprocessing.MinMaxScaler().fit_transform(data)

# Iscravaju se podaci prema dodeljenim klasterima u funkciji od 2 atributa. 
colors = 'rgb'
for i in range(data.shape[0]):
    plt.text(data_plot[i, 2], data_plot[i, 8], str(clustering.labels_[i]),
             color=colors[clustering.labels_[i]],
             fontdict={'weight': 'bold', 'size': 9}
        )
#plt.xticks([])
#plt.yticks([])
#plt.axis('off')
plt.show()


from scipy.cluster.hierarchy import dendrogram, linkage

linkage_matrix = linkage(data, 'ward')
figure = plt.figure(figsize=(7.5, 5))
dendrogram(linkage_matrix, color_threshold=0)
plt.title('Hijerarhijski klastering - dendrogram')
plt.xlabel('Indeks sloga')
plt.ylabel('Razdaljina (ward kriterijum)')
plt.tight_layout()
plt.show()

figure = plt.figure(figsize=(7.5, 5))
dendrogram(
    linkage_matrix,
    truncate_mode='lastp',  # Prikaz samo poslednjih p objedinjenih klastera. 
    p=24,  # Prikaz samo poslednjih 24 objedinjenih klastera.
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.title('Hijerarhijski klastering - dendrogram')
plt.xlabel('Indeks sloga ili (veličina klastera)')
plt.ylabel('Razdaljina (ward kriterijum)')
plt.show()