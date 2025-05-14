import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Skup podataka o tumorima. Atribut klase govori da li se radi o malignom ili 
# benignom tumoru. 
cancer = load_breast_cancer()
df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns = np.append(cancer['feature_names'], ['target']))

print(df_cancer.head())
print(df_cancer.columns)

# Koristi se seaborn za vizualizaciju odnosa nekoliko atributa. Parametar 'hue' 
# se različito postavlja za maligne i benigne tumore. 
sns.pairplot(df_cancer, hue = 'target',
             vars = ['mean radius', 'mean texture', 'mean area'] )
plt.show()

# Sa 1 su oznaceni benigni, a sa 0 maligni tumori. 
print(df_cancer['target'].value_counts())

# Razdvajanje skupa podataka na matricu običnih atributa X 
# i vektor klasa (labela) y 
X = df_cancer.drop('target', axis=1) 
print(X.head())
y = df_cancer['target']
print(y.head())

# Podela na trening i test skup podataka. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 8)
print ('Dimenzije matrice X za treniranje: ', X_train.shape)
print ('Dimenzije matrice X za testiranje: ', X_test.shape)
print ('Dimenzija vektora "y" za treniranje: ', y_train.shape)
print ('Dimenzija vektora "y" za testiranje: ', y_test.shape)

# Normalizacija trening skupa (slično radi i MinMaxScaler)
X_train_min = X_train.min()
X_train_max = X_train.max()
X_train_range = (X_train_max- X_train_min)
X_train_scaled = (X_train - X_train_min)/(X_train_range)
print(X_train_scaled.head())

# Normalizacija test skupa
X_test_min = X_test.min()
X_test_range = (X_test - X_test_min).max()
X_test_scaled = (X_test - X_test_min)/X_test_range

# Kreiranje i obučavanje SVM modela 
svc_model = SVC()
svc_model.fit(X_train_scaled, y_train)

# Testiranje modela za predikciju
y_predict = svc_model.predict(X_test_scaled)
cm = np.array(confusion_matrix(y_test, y_predict, labels=[1,0]))
cm_df = pd.DataFrame(cm, index=['maligno', 'benigno'],
                         columns=['predviđeno_maligno','predviđeno_benigno'])
print()

# Prikazuje se matrica konfuzije
print(cm_df)
print()

# Prikazuju se izvedene mere - preciznost, odziv, F-mera
print(classification_report(y_test,y_predict))
print()

# Optimizacija parametara pretraživanjem po mreži ("grid") parametara. 
from sklearn.model_selection import GridSearchCV
# GridSearch će ispitati sve kombinacije zadatih vrednosti sledeća 3 parametra. 
param_grid = {'C': [0.1, 1, 5], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'linear']}
grid = GridSearchCV(SVC(), param_grid, refit=True, cv=5, verbose=4)
grid.fit(X_train_scaled,y_train)
print("Najbolja kombinacija parametara:")
print(grid.best_params_)
print()
print(grid.best_estimator_)
print()
# Testiranje ove kombinacije
grid_predictions = grid.predict(X_test_scaled)
cm = np.array(confusion_matrix(y_test, grid_predictions, labels=[1,0]))
cm_df = pd.DataFrame(cm, index=['maligno', 'benigno'],
                         columns=['predviđeno_maligno','predviđeno_benigno'])
print(cm_df)
