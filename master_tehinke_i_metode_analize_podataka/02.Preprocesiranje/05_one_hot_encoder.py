from sklearn import preprocessing
import numpy as np

# Za svaki atribut koji ima K mogućih vrednosti, generiše se novih K atributa. 
# Svaki od tih K atributa može da dobije vrednost 0 ili 1, a u jednom redu
# samo jedan atribut dobija vrednost 1 (ostali dobijaju vrednost 0).  
enc = preprocessing.OneHotEncoder()
# Originalni skup podataka.
X = [['male', 'from US', 'uses Safari'], 
     ['female', 'from Europe', 'uses Firefox']]
# Poziva se fit funkcija enkodera koja treba da pobroji sve atribute.
enc.fit(X)
print('Transformacija celog skupa podataka:')
print(enc.transform([['female', 'from US', 'uses Safari'],
               ['male', 'from Europe', 'uses Safari']]).toarray()) 
print('Automatski pobrojane kategorije:')
print(enc.categories_)

# Moguće je ručno pobrojati kategorije. 
genders = ['female', 'male']
locations = ['from Africa', 'from Asia', 'from Europe', 'from US']
browsers = ['uses Chrome', 'uses Firefox', 'uses IE', 'uses Safari']
enc = preprocessing.OneHotEncoder(categories=[genders, locations, browsers])
X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
enc.fit(X)
print('Transformacija pomoću enkodera kom su ručno podešene kategorije:')
print(enc.transform([['female', 'from Asia', 'uses Chrome']]).toarray())

# Podešavanje kako se obrađuju nepoznate vrednosti.
enc = preprocessing.OneHotEncoder(handle_unknown='infrequent_if_exist')
X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
enc.fit(X)
print('Nepoznate vrednosti atributa se kodiraju nulom:')
print(enc.transform([['female', 'from Asia', 'uses Chrome']]).toarray())

# Korišćenje drop parametra da bi se izbegle linearno zavisne kolone u matrici podataka. 
# Matrica sa linearno zavisnim kolonama nema inverznu matricu i to predstavlja 
# problem za neke algoritme (npr. linearnu regresiju). 
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]
drop_enc = preprocessing.OneHotEncoder(drop='first').fit(X)
print(drop_enc.categories_)
print('Za svaki od originalnih atributa generiše se za 1 manje novih atibuta:')
print(drop_enc.transform(X).toarray())

# Ako želimo da smanjimo broj generisanih kolona samo za binarne atribute onda 
# se koristi drop='if_binary'
X = [['male', 'US', 'Safari'],
     ['female', 'Europe', 'Firefox'],
     ['female', 'Asia', 'Chrome']]
drop_enc = preprocessing.OneHotEncoder(drop='if_binary').fit(X)
print(drop_enc.categories_)
print('Samo za binarne originalne atribute generiše se za 1 manje novih atibuta:')
print(drop_enc.transform(X).toarray())

# Ako je uključen drop i handle_unknown postavljen na 'ignore', onda se nepoznate
# vrednosti kodiraju sa 0 i to može da dovede do zabune. 
drop_enc = preprocessing.OneHotEncoder(drop='first', handle_unknown='ignore').fit(X)
X_test = [['unknown', 'America', 'IE']]
print(drop_enc.transform(X_test).toarray())
