from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Generisanje skupa podataka za klasifikaciju
X, y = make_classification(random_state=42)
print(X,y)
# Podela skupa podataka na deo za treniranje i deo za testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Kreiranje pipeline objekta kojim se definiše da se prvo primenjuje 
# standardizacija pa zatim logistička regresija. Isti pipeline objekat
# je posle moguće primeniti i za testiranje primenjenog modela. 
pipe = make_pipeline(StandardScaler(), LogisticRegression())

# Primenjuje se standardizacija na podacima za treniranje, pa se zatim obučava 
# klasifikator korišćenjem logističke regresije. 
pipe.fit(X_train, y_train)  

# Određivanje performansi na test skupu
print(pipe.score(X_test, y_test)) 
