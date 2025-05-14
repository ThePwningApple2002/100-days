import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, classification_report
from matplotlib.colors import ListedColormap

# Učitavanje skupa podataka. Poslednja kolona "Purchased" predstavlja labelu 
# klase i označava da li je korisnik kupio proizvod reklamiran na društvenim mrežama. 
dataset = pd.read_csv('Social_Network_Ads.csv')
print(dataset)

# U matricu X se smeštaju numerički atributi "Age" i "EstimatedSalary", a 
# u vektor y se smeštaju labele klasa.   
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Podela skupa podataka na trening (75%) i test deo (25%).  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size = 0.25, random_state = 0)

# Skaliranje podataka nije neophodno za rad Naive Bayes algoritma. Radi se zbog
# kasnijeg grafičkog prikaza podataka. 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Kreiranje i obučavanje modela. Za rad sa realnim numeričkim atributima se 
# koristi GaussianNB varijanta. 
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predikcija klase za objekte iz test skupa podataka. 
y_pred = classifier.predict(X_test)

# Prikazuje se matrica konfuzije
cm = confusion_matrix(y_test, y_pred)
print("Matrica konfuzije")
print(cm)
print()

# Prikazuju se izvedene mere - preciznost, odziv, F-mera
print(classification_report(y_test,y_pred))
print()

# Prikaz predviđenih i stvarnih vrednosti klase
# Od 2 vektora koordinata kreiraju se 2 matrice koordinata. 
X1, X2 = np.meshgrid(np.arange(start = X_test[:, 0].min() - 1, stop = X_test[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_test[:, 1].min() - 1, stop = X_test[:, 1].max() + 1, step = 0.01))
# Matrica predikcija. Prvo se matrice atributa X1 i X2 preoblikuju u nizove, 
# transponuju se, izvrši se predikcija. Zatim se rezultati iz vektora preoblikuju
# u matricu. 
Y_pred_diag = classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape)
# Iscrtavanje konturnog dijagrama. 
plt.contourf(X1, X2, Y_pred_diag,
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
plt.scatter(X_test[y_test == 0, 0], X_test[y_test == 0, 1], c = 'red', label = 0)
plt.scatter(X_test[y_test == 1, 0], X_test[y_test == 1, 1], c = 'green', label = 1)
plt.title('Procenjene i stvarne vrednosti klasa')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
