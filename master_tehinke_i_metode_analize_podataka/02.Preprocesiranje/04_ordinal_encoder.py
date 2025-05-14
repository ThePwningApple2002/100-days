from sklearn import preprocessing
import numpy as np

# Svakom kategorijskom atributu se dodeljuje jedan redni broj. Redni brojevi 
# počinju od 0.  
enc = preprocessing.OrdinalEncoder()
# Originalni skup podataka. 
X = [['male', 'from US', 'uses Safari'], 
     ['female', 'from Europe', 'uses Firefox']]

# Poziva se fit funkcija enkodera koja treba da pobroji sve atribute. 
enc.fit(X)

print('Transformacija celog skupa podataka:') 
print(enc.transform(X))

print('Transformacija samo jednog podataka (jednog reda):') 
print(enc.transform([['female', 'from US', 'uses Safari']]))

# Enkodiranje sa nedostajućim vrednostima. 
enc = preprocessing.OrdinalEncoder()
X = [['male'], 
     ['female'], 
     [np.nan], 
     ['female']]
enc.fit_transform(X)
print('Transformacija skupa podataka sa nedostajućim vrednostima (NaN):') 
print(enc.transform(X))

# Nedostajuće vrednosti se menjaju konstantom -1. 
enc = preprocessing.OrdinalEncoder(encoded_missing_value=-1)
X = [['male'], 
     ['female'], 
     [np.nan], 
     ['female']]
enc.fit_transform(X)
print('Nedostajuće vrednosti zamenjene sa -1:') 
print(enc.transform(X))

# Prethodni slučaj korišćenjem pipeline-a. 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
enc = Pipeline(steps=[
     ("encoder", preprocessing.OrdinalEncoder()),
     ("imputer", SimpleImputer(strategy="constant", fill_value=-1)),
    ])
print('Nedostajuće vrednosti zamenjene sa -1 uz korišćenje pipeline-a:')
print(enc.fit_transform(X))

