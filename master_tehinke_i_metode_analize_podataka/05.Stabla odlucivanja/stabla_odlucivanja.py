import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

# Učitavanje skupa podataka. Labela klase je "quality" i ima moguće vrednosti 
# "good" i "bad". 
missing_values = ["n/a", "na", "--","NaN","Na"]
dataset=pd.read_csv('wine.csv',na_values = missing_values)

# Provera nedostajućih vrednosti. 
print(dataset.isnull().sum())
print(dataset.describe())

# Prevođenje kategoričkog atributa (labele klase) u numerički (0 ili 1). 
le = preprocessing.LabelEncoder()
dataset.quality = le.fit_transform(dataset.quality)
print(dataset)

# Svi atributi osim poslednjeg se smeštaju u matricu X. 
X=dataset.iloc[:, :-1].values
print(X)
# Labela klase se smešta u vektor y. 
y=dataset.iloc[:, 11].values
print(y)

# Kreiranje modela stabla odlučivanja. 
decision_tree = DecisionTreeClassifier(criterion='gini', splitter='best', 
                    min_samples_split=2, min_samples_leaf=1, random_state=43)
# Evaluacija modela postupkom unakrsne validacije. Radi se 5-ostruka unakrsna validacija.  
scores = cross_val_score(decision_tree, X, y, cv=5)
print("Tačnost %0.2f sa standardnom devijacijom %0.2f" % (scores.mean(), scores.std()))

# Ručno deljenje skupa podataka na deo za treniranje i deo za testiranje. 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=67)
decision_tree = DecisionTreeClassifier(criterion='gini', splitter='best', 
                    min_samples_split=2, min_samples_leaf=1, random_state=43)
# Obučavanje modela. 
model = decision_tree.fit(X_train, y_train)
# Testiranje modela. 
y_pred=decision_tree.predict(X_test)
print("Tačnost stabla odlučivanja:")
print(metrics.accuracy_score(y_test, y_pred))

# Iscrtavanje matice konfuzije korišćenjem seaborn biblioteke. 
from sklearn.metrics import confusion_matrix
class_names=[0,1]
matrix = confusion_matrix(y_test, y_pred)
# Kreiranje DataFrame objekta za prikaz. 
dataframe = pd.DataFrame(matrix, index=class_names, columns=class_names)
# Iscrtavanje heatmap-e. 
sns.heatmap(dataframe, annot=True, cbar=None, cmap="Blues")
plt.title("Matrica konfuzije"), plt.tight_layout()
plt.ylabel("Stvarna klasa"), plt.xlabel("Predviđena klasa")
plt.show()

# Prikaz matrice konfuzije u konzoli. 
print("Matrica konfuzije")
print(matrix)

# Korišćenje classification_report za prikaz izvedenih mera:
# preciznost, odziv, F-mera
target_names = ['0', '1']
print(classification_report(y_test, y_pred, target_names=target_names))

# Stablo odlučivanja gde se kao kriterijum podele koristi entropija. 
decision_tree1 = DecisionTreeClassifier(criterion='entropy', splitter='best', 
                    min_samples_split=2, min_samples_leaf=1, random_state=43)
model = decision_tree1.fit(X_train, y_train)
# Testiranje modela. 
y_pred=decision_tree1.predict(X_test)
print("Tačnost stabla odlučivanja primenom entropije i bez orezivanja:")
print(metrics.accuracy_score(y_test, y_pred))
print()

# Prikaz stabla odlučivanja pomoću graphviz biblioteke.  
feature_cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']
dot_data = StringIO()
export_graphviz(decision_tree1, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols, class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('01_vina_celo_stablo.png')
Image(graph.create_png())

# Stablo odlučivanja gde se kao kriterijum podele koristi entropija i 
# sa uključenim orezivanjem. Podstablo sa najvećom kompleksnošću koja je manja
# od ccp_alpha će biti orezano.  
decision_tree2 = DecisionTreeClassifier(criterion='entropy', splitter='best', 
                    min_samples_split=2, min_samples_leaf=1, random_state=43,
                    ccp_alpha=0.01)
model = decision_tree2.fit(X_train, y_train)
# Testiranje modela. 
y_pred=decision_tree2.predict(X_test)
print("Tačnost stabla odlučivanja primenom entropije i sa orezivanjem:")
print(metrics.accuracy_score(y_test, y_pred))

# Prikaz stabla odlučivanja pomoću graphviz biblioteke.  
feature_cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']
dot_data = StringIO()
export_graphviz(decision_tree2, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols, class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('02_vina_pruning.png')
Image(graph.create_png())