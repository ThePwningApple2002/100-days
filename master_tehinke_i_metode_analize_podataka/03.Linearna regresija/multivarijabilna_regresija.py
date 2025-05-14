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
pprint(abalone[["Length", "Diameter", "Height", "Whole weight", "Rings"]].describe())

# Funkcija head prikazuje nazive kolona i prvih nekoliko (podrazumevano 5)
# redova podataka
pprint(abalone.head())

# Na box dijagramu se prikazuju svi numerički atributi. 
abalone.boxplot()
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# Iscrtava se dijagram rasipanja sa zadatim nizovima. 
ax.scatter(abalone["Height"], abalone["Diameter"], abalone["Whole weight"], 
           c = abalone["Rings"], vmin = 0, vmax = 30)
ax.set_xlabel('Height')
ax.set_ylabel('Diameter')
ax.set_zlabel('Whole weight')
#ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
plt.show()

# Iz skupa podataka se izdvaja nezavisna promenljiva X (sa svim numeričkim atributima
# osim broja prstenova) i druga promenljiva čiju vrednost procenjujemo (broj prstenova)
# labela y. 
X = abalone[['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight']]
y = abalone['Rings']

# Atributi i labela se dele na deo za treniranje i deo za testiranje (u odnosu 80:20). 
# Podaci se u train i test skupove ubacuju na slučajan način. Parametar random_state
# je seed za taj slučajni izbor da bi izbor za svako izvršenje programa bio isti. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

# Obučavanje modela
model = LinearRegression()
model.fit(X_train, y_train)
print('Slobodni član: ', model.intercept_)
print('Koeficijenti hiperravni: ', model.coef_)

# Koeficijente možemo da prikažemo preglednije uz odgovarajuće atribute
coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])  
print(coeff_df)

# Predviđanje vrednosti modelom linearne regresije
y_pred = model.predict(X_test)

# Poređenje stvarnih i predviđenih vrednosti
df = pd.DataFrame({'Stvarno': y_test, 'Predviđeno': y_pred})
print(df.head(15))

# Prikaz stvarnih i predviđenih vrednosti (prvih 15 redova)
df1 = df.head(15)
df1.plot(kind='bar',figsize=(10, 8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.show()

# Određivanje kvaliteta procene
print('Srednja apsolutna greška:', metrics.mean_absolute_error(y_test, y_pred))  
print('Srednja kvadratna greška:', metrics.mean_squared_error(y_test, y_pred))  
print('Koren iz srednje kvadratne greške:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print('Koeficijent determinisanosti:', model.score(X_test, y_test))
