from sklearn import preprocessing
import numpy as np

# Standardizacija na svaki od atributa X primenjuje formulu
# X = (X - srednja_vrednost(X)) / standardna_devijacija(X) 
# Na taj način skup podataka se transformiše tako da svaki atribut ima 
# srednju vrednost 0 i standardnu devijaciju 1. 

X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])

scaler = preprocessing.StandardScaler().fit(X_train)
# U konstruktoru StandardScaler() moguće je isključiti centriranje po srednjoj 
# vrednosti pomoću parametra with_mean=False. Moguće je isključiti skaliranje po 
# standardnoj devijaciji pomoću parametra with_std=False. 

print('Srednje vrednosti za svaki od atributa (za svaku kolonu):')
print(scaler.mean_)

print('Standardne devijacije za svaki od atributa (za svaku kolonu):')
print(scaler.scale_)

print('Standardizovan skup podataka:')
X_scaled = scaler.transform(X_train)
print(X_scaled)

print('Srednje vrednosti posle standardizacije:')
print(X_scaled.mean(axis=0))

print('Standardne devijacije posle standardizacije:')
print(X_scaled.std(axis=0))
