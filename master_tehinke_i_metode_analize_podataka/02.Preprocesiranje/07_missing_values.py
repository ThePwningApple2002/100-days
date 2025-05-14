import numpy as np
from sklearn.impute import SimpleImputer

# SimpleImputer radi popunjavanje nedostajućih vrednosti korišćenjem zadate strategije. 
# Ovde je strategija "mean" tj. zamena nedostajućih vrednosti svakog od atributa 
# srednjom vrednošću tog atributa. U procesu fitovanja se računa srednja vrednost 
# svakog od atributa na osnovu postojećih vrednosti. 
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit([[1, 2], 
         [np.nan, 3], 
         [7, 6]])

# Srednje vrednosti izračunate u procesu fitovanja se koriste za popunjavnje 
# ovde zadatog skupa podataka. 
X = [[np.nan, 2], 
     [6, np.nan], 
     [7, 6]]
print("Skup sa dodatim vrednostima podataka:")
print(imp.transform(X))

# Korišćenje sparse matrice za fitovanje SimpleImputer-a
import scipy.sparse as sp
X = sp.csc_matrix([[1, 2], 
                   [0, -1], 
                   [8, 4]])
imp = SimpleImputer(missing_values=-1, strategy='mean')
imp.fit(X)
X_test = sp.csc_matrix([[-1, 2], 
                        [6, -1], 
                        [7, 6]])
print("Korišćenje sparse matrica:")
print(imp.transform(X_test).toarray())

# SimpleImputer može da radi i sa kategorijskim atributima. 
import pandas as pd
df = pd.DataFrame([["a", "x"],
                   [np.nan, "y"],
                   ["a", np.nan],
                   ["b", "y"]], dtype="category")

imp = SimpleImputer(strategy="most_frequent")
print('Popunjavanje nedostajućih vrednosti najfrekventnijom postojećom vrednošću:') 
print(imp.fit_transform(df))

# Za složenije modeliranje nedostajućih vrednosti može da se koristi IterativeImputer. 
# Radi tako što svaku kolonu sa nedostajućim vrednostima proglašava za y, a sve 
# ostale kolone za X. Na osnovu redova u y gde postoje vrednosti obučava se model
# linearne regresije. Onda se obučeni model koristi za procenu nedostajućih 
# vrednosti. 
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp = IterativeImputer(max_iter=10, random_state=0)
imp.fit([[1, 2], 
         [3, 6], 
         [4, 8], 
         [np.nan, 3], 
         [7, np.nan]])

X_test = [[np.nan, 2], 
          [6, np.nan], 
          [np.nan, 6]]
print("Nedostajuće vrednosti popunjene primenom lineare regresije:")
print(np.round(imp.transform(X_test)))
