from sklearn import preprocessing
import numpy as np

X = [[ 1., -1.,  2.],
     [ 2.,  0.,  0.],
     [ 0.,  1., -1.]]

# Moguće je izabrati norme l1, l2, max. Izborom norme l2 (Euklidska norma), 
# svaki podatak će biti predstavljen jediničnim vektorom. 
X_normalized = preprocessing.normalize(X, norm='l2')

print('Skup podataka posle normalizacije:')
print(X_normalized)

# Moguće je koristiti i klasu Normalizer (slično kao kod standardizacije). Razlika
# je ta što se tamo čuvaju srednja vrednost i standardna devijacija trening skupa 
# da bi se koristile i na test skupu. Ovde nema potrebe da se nešto čuva jer se 
# normalizacija primenjuje na svaki podatak posebno. 
normalizer = preprocessing.Normalizer().fit(X)

print('Skup podataka posle normalizacije pomoću klase:')
print(normalizer.transform(X))

print('Normalizacija na samo jednom vektoru:')
print(normalizer.transform([[-1.,  1., 0.]]))