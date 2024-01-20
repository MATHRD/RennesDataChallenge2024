import pandas as pd

chemin_fichier_csv = r"C:\Users\kerla\OneDrive\Bureau\PYTHON\dataset.csv"
data = pd.read_csv(chemin_fichier_csv)
data = pd.DataFrame(data).dropna()

import numpy as np 
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, recall_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt 
import datetime as datetime
import yfinance as yf


liste_actifs = list(["Returns_BTC","Returns_ETH","Returns_BNB","Returns_LTC","Returns_XRP"])

for i in liste_actifs:
    X = data.drop("Returns_BTC", axis=1).drop("Close_BTC", axis=1).drop("Date",axis=1)#.drop("regulation_attention_twitter.1",axis=1).drop("regulation_vader_polarity_compound_mean",axis=1).drop("crisis_vader_polarity_compound_mean",axis=1).drop("sdcc_vader_polarity_compound_mean",axis=1).drop("monp_vader_polarity_compound_mean",axis=1).drop("regulation_attention_twitter",axis=1).drop("sdcc_attention_twitter",axis=1).drop("monp_attention_twitter",axis=1).drop("uncertainty_attention_twitter",axis=1).drop("eth_vader_polarity_compound_mean",axis=1).drop("eth_tweet_count",axis=1).drop("btc_tweet_count",axis=1).drop("USEPUINDXD",axis=1).drop("PercentHikeCut",axis=1).drop("H15T3M_Index",axis=1).drop("H15T1M_Index",axis=1).drop("TreasuryYield5Years",axis=1).drop("SP500",axis=1).drop("Brent_CrudeOil",axis=1).drop("ECRPUS1YIndex",axis=1).drop("Gold",axis=1).drop("VStoxx",axis=1).drop("Volume_XRP",axis=1).drop("Returns_XRP",axis=1).drop("Close_XRP",axis=1).drop("Volume_LTC",axis=1).drop("Returns_LTC",axis=1).drop("Close_LTC",axis=1).drop("Volume_BNB",axis=1).drop("Returns_BNB",axis=1).drop("Close_BNB",axis=1)
    Y = data["Returns_BTC"]
    print(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, random_state=42)

    # Création et entraînement du modèle
    random_forest = RandomForestRegressor(oob_score=True)
    random_forest.fit(X_train,Y_train)

    # Prédiction sur la base d'apprentissage et la base de test
    Y_train_pred = random_forest.predict(X_train)
    Y_test_pred = random_forest.predict(X_test)
    print("The model score is: ", random_forest.score(X,Y))


    new_data = data.drop("Returns_BTC",axis=1).drop("Date",axis=1).drop("Close_BTC",axis=1).tail(1)
    prediction = random_forest.predict(new_data)
    print("The model predict the last row or days to be: ", prediction)
    print("Actual value is: ", data[["Returns_BTC"]].tail(1).values[0][0])



importance = random_forest.feature_importances_

importance_df = pd.DataFrame({'Variable':X.columns, 'Importance': importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False).reset_index(drop=True)
print("Importance des variables :")
print(importance_df)
print()

plt.figure(figsize=(8, 6))
plt.bar(importance_df['Variable'], importance_df['Importance'])
plt.xticks(rotation='vertical')
plt.xlabel('Variable')
plt.ylabel('Importance')
plt.title('Importance des variables')
plt.tight_layout()
plt.show()


# RANDOM FOREST QUE SUR BTC EN ENLEVANT DES VARIABLES 



X = data.drop("Returns_BTC", axis=1).drop("Close_BTC", axis=1).drop("Date",axis=1).drop("Close_ETH",axis=1).drop("Close_BNB",axis=1).drop("Close_LTC",axis=1).drop("Close_XRP",axis=1).drop("SP500",axis=1).drop("Returns_ETH",axis=1).drop("Returns_BNB",axis=1).drop("Returns_LTC",axis=1).drop("Returns_XRP",axis=1)
Y = data["Returns_BTC"]
print(X)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, random_state=42)
print(X_train)

# Création et entraînement du modèle
random_forest = RandomForestRegressor(oob_score=True)
random_forest.fit(X_train,Y_train)

# Prédiction sur la base d'apprentissage et la base de test
Y_train_pred = random_forest.predict(X_train)
Y_test_pred = random_forest.predict(X_test)
print("The model score is: ", random_forest.score(X,Y))


new_data = data.drop("Returns_BTC",axis=1).drop("Close_BTC",axis=1).drop("Date",axis=1).drop("Close_ETH",axis=1).drop("Close_BNB",axis=1).drop("Close_LTC",axis=1).drop("Close_XRP",axis=1).drop("SP500",axis=1).drop("Returns_ETH",axis=1).drop("Returns_BNB",axis=1).drop("Returns_LTC",axis=1).drop("Returns_XRP",axis=1).tail(1)
print(new_data)
prediction = random_forest.predict(new_data)
print("The model predict the last row or days to be: ", prediction)
print("Actual value is: ", data[["Returns_BTC"]].tail(1).values[0][0])

importance = random_forest.feature_importances_

importance_df = pd.DataFrame({'Variable':X.columns, 'Importance': importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False).reset_index(drop=True)
print("Importance des variables :")
print(importance_df)
print()

plt.figure(figsize=(8, 6))
plt.bar(importance_df['Variable'], importance_df['Importance'])
plt.xticks(rotation='vertical')
plt.xlabel('Variable')
plt.ylabel('Importance')
plt.title('Importance des variables')
plt.tight_layout()
plt.show()
