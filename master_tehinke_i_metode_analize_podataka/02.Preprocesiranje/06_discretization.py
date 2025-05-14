from sklearn import preprocessing
import numpy as np
import pandas as pd

# KBinsDiscretizer prema numeričkoj vrednosti atributa određuje opseg vrednosti
# ("bin") u kome se nalazi ta vrednost atributa. 
X = np.array([[ -3., 5., 15 ],
              [  0., 6., 14 ],
              [  6., 3., 11 ]])
# U konstruktoru se zadaje broj binova za svaki od atributa. Granice binova se 
# određuju automatski tako da u svakom binu bude približno jednak broj atributa. 
est = preprocessing.KBinsDiscretizer(n_bins=[3, 2, 2], encode='ordinal').fit(X)

# Granice binova su sledeće (interval uvek uključuje donju granicu, a ne uključuje 
# gornju granicu.  
print(est.bin_edges_)

print('Transformisani podaci:')
print(est.transform(X))

# Moguće je ručno zadati granice binova i naziv za svaki od njih. Potrebno je 
# zadati za 1 više granica nego što ima binova. Za do se koristi funkcija pandas.cut
bins = [0, 1, 13, 20, 60, np.inf]
labels = ['infant', 'kid', 'teen', 'adult', 'senior citizen']
transformer = preprocessing.FunctionTransformer(
     pd.cut, kw_args={'bins': bins, 'labels': labels, 'retbins': False}
)
X = np.array([2, 0.2, 25, 15, 97])
print(transformer.fit_transform(X))
#['infant', 'kid', 'teen', 'adult', 'senior citizen']
#Categories (5, object): ['infant' < 'kid' < 'teen' < 'adult' < 'senior citizen']