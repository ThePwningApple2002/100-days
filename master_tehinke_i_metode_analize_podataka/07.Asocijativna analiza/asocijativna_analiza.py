import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import fpgrowth

data = pd.read_csv("OnlineRetail.csv", encoding='latin1')
print(data.head())
print()
print(data.info())
print()

# Provera nedostajućih podataka
print(data.isnull().any())
# Izbacivanje redova sa nedostajućim podacima
data = data.dropna(subset=["Description"])
print(data.isnull().any())


# Grupisanje transakcija po broju racuna i opisu proizvoda
transactions = data.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo')
transactions = transactions.applymap(lambda x: 1 if x > 0 else 0)
columns = transactions.columns.tolist()

print(transactions.shape)

# Kodiranje proizvoda kao binarnih atributa
te = TransactionEncoder()
te.fit(transactions)
te_ary = te.transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
for i, col in enumerate(df.columns):
    df.rename(columns={col: columns[i]}, inplace=True)
    
print(df.head())

# Apriori algoritam
min_support_values = [0.02, 0.03]
min_confidence_values = [0.5, 0.6, 0.7, 0.8, 0.9]

best_avg_lift = 0
best_min_support = 0
best_min_confidence = 0 
# Traženje najboljih vrednosti za min_support i min_confidence
# for min_support in min_support_values:
#     for min_confidence in min_confidence_values:
#         frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
#         rules = association_rules(frequent_itemsets, metric="confidence", min_threshold = min_confidence)
#         avg_lift = rules["lift"].mean()
#         print(f"Za min_support = {min_support} i min_confidence = {min_confidence} prosecni lift je {avg_lift}.")
#         if avg_lift > best_avg_lift:
#             best_avg_lift = avg_lift
#             best_min_support = min_support
#             best_min_confidence = min_confidence
#
# print(f"Najbolji parametri su: min_support = {best_min_support}, i min_confidence = {best_min_confidence}.")

# FP growth
min_support_values = [0.02, 0.03]
min_confidence_values = [0.5, 0.6, 0.7, 0.8, 0.9]

best_avg_lift = 0
best_min_support = 0
best_min_confidence = 0
# Traženje najboljih vrednosti za min_support i min_confidence
# for min_support in min_support_values:
#     for min_confidence in min_confidence_values:
#         frequent_itemsets = fpgrowth(df, min_support=min_support, use_colnames=True)
#         rules = association_rules(frequent_itemsets, metric="confidence", min_threshold = min_confidence)
#         avg_lift = rules["lift"].mean()
#         print(f"Za min_support = {min_support} i min_confidence = {min_confidence} prosecni lift je {avg_lift}.")
#         if avg_lift > best_avg_lift:
#             best_avg_lift = avg_lift
#             best_min_support = min_support
#             best_min_confidence = min_confidence
#
# print(f"Najbolji parametri su: min_support = {best_min_support}, i min_confidence = {best_min_confidence}.")

# Izvršavanje algoritma za zadate vrednosti parametara
frequent_itemsets = fpgrowth(df, min_support=0.03, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print(rules.head())

# Raspodela lift vrednosti pravila
sns.histplot(rules['lift'], kde=True)
plt.xlabel('Lift')
plt.ylabel('Broj pravila')
plt.title('Raspodela lift vrednosti pravila')
plt.show()

# Vizualizacija asocijativnih pravila
plt.scatter(rules["support"], rules["confidence"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Association Rules")
plt.show()
