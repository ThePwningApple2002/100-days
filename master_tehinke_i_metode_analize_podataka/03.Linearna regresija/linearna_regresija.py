import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from pprint import pprint


# Učitavanje skupa podataka
abalone = pd.read_csv('abalone.csv')

# Prikaz dimenzija skupa podataka
print(abalone.shape)

# Prikaz naziva kolona u skupu podataka
pprint(abalone.columns)

# Opis skupa podataka - prikazuju se statističke mere za sve atribute u skupu.
pprint(abalone.describe())

# Opis skupa podataka - prikazuju se statističke mere samo za navedene atribute.  
pprint(abalone[["Length", "Diameter"]].describe())

# Funkcija head prikazuje nazive kolona i prvih nekoliko (podrazumevano 5)
# redova podataka
pprint(abalone.head())

# Na box dijagramu se prikazuju svi numerički atributi. 
abalone.boxplot()
plt.show()

# Na dijagramu rasipanja se prikazuje zavisnost visine od težine ljušture. 
abalone.plot(x='Shell weight', y='Height', style='o')  
plt.title('Visina u zavisnosti od težine ljušture')
plt.xlabel('Težina')
plt.ylabel('Visina')
plt.show()

# Iz skupa podataka se izdvaja jedna nezavisna promenljiva X i druga promenljiva 
# čiju vrednost procenjujemo (labela) y. U reshape funkciji prvi argument je broj 
# broj vrsta (-1 znači da se broj vrsta preuzima iz originalnog niza), a drugi 
# argument je broj kolona.  
X = abalone['Shell weight'].values.reshape(-1, 1)
y = abalone['Height'].values.reshape(-1, 1)

# Atribut i labela se dele na deo za treniranje i deo za testiranje (u odnosu 80:20). 
# Podaci se u train i test skupove ubacuju na slučajan način. Parametar random_state
# je seed za taj slučajni izbor da bi izbor za svako izvršenje programa bio isti. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

# Obučavanje modela
model = LinearRegression()
model.fit(X_train, y_train)
print('Slobodni član: ', model.intercept_)
print('Nagib prave: ', model.coef_)

# Predviđanje vrednosti regresionim modelom
y_pred = model.predict(X_test)

# Poređenje stvarnih i predviđenih vrednosti
df = pd.DataFrame({'Stvarno': y_test.flatten(), 'Predviđeno': y_pred.flatten()})
print(df.head(15))

# Prikaz stvarnih i predviđenih vrednosti (prvih 15 redova)
df1 = df.head(15)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.show()

# Prikaz svih stvarnih vrednosti (dijagram rasipanja) i regresione prave. 
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('Predviđena visina i skup podataka')
plt.xlabel('Težina ljušture')
plt.ylabel('Visina')
plt.show()

# Određivanje kvaliteta procene
print('Srednja apsolutna greška:', metrics.mean_absolute_error(y_test, y_pred))  
print('Srednja kvadratna greška:', metrics.mean_squared_error(y_test, y_pred))  
print('Koren iz srednje kvadratne greške:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print('Koeficijent determinacije:', model.score(X_test, y_test))
