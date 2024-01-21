import numpy as np
import pandas as pd
import numpy.random as rd
import matplotlib.pyplot as plt
import math
import yfinance as yf
from datetime import datetime

seed_value = 123
np.random.seed(seed_value)

chemin_fichier_excel = r"C:\Users\kerla\OneDrive\Bureau\PYTHON\dataset.csv"
data = pd.read_csv(chemin_fichier_excel)
data = pd.DataFrame(data)


closeBTC = data.loc[:,"Close_BTC"].copy().dropna()
print(closeBTC)
plt.plot(closeBTC)
plt.show()


rdm = [(closeBTC[i+1] - closeBTC[i]) / closeBTC[i] for i in range(len(closeBTC)-1)]
vol = rdm.std()
#vol = np.sqrt(1275)*np.std(rdm)

print(vol)
print(rdm)

S_0 = closeBTC.iloc[1250]
print(S_0)
S_m = []
for i in range(200):
    S=[S_0]
    for i in range(26):    #26
        S.append(S[i]*np.exp( (np.mean(rdm)-vol**2/2)*1 + vol*rd.normal(0,1)*1))
    plt.plot([i for i in range(len(S))],S,lw=0.5)
    S_m.append(S)
plt.show()

prix_espere = np.mean(S_m)
print(f"la moyenne des prix aléatoires du BTC : {prix_espere}")



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

liste_actifs = list(["Close_BTC","Close_ETH","Close_BNB","Close_LTC","Close_XRP"])

for i in liste_actifs:
    X = data.drop(i, axis=1).drop("Date",axis=1)#.drop("regulation_attention_twitter.1",axis=1).drop("regulation_vader_polarity_compound_mean",axis=1).drop("crisis_vader_polarity_compound_mean",axis=1).drop("sdcc_vader_polarity_compound_mean",axis=1).drop("monp_vader_polarity_compound_mean",axis=1).drop("regulation_attention_twitter",axis=1).drop("sdcc_attention_twitter",axis=1).drop("monp_attention_twitter",axis=1).drop("uncertainty_attention_twitter",axis=1).drop("eth_vader_polarity_compound_mean",axis=1).drop("eth_tweet_count",axis=1).drop("btc_tweet_count",axis=1).drop("USEPUINDXD",axis=1).drop("PercentHikeCut",axis=1).drop("H15T3M_Index",axis=1).drop("H15T1M_Index",axis=1).drop("TreasuryYield5Years",axis=1).drop("SP500",axis=1).drop("Brent_CrudeOil",axis=1).drop("ECRPUS1YIndex",axis=1).drop("Gold",axis=1).drop("VStoxx",axis=1).drop("Volume_XRP",axis=1).drop("Returns_XRP",axis=1).drop("Close_XRP",axis=1).drop("Volume_LTC",axis=1).drop("Returns_LTC",axis=1).drop("Close_LTC",axis=1).drop("Volume_BNB",axis=1).drop("Returns_BNB",axis=1).drop("Close_BNB",axis=1)
    Y = data[i]
    print(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, random_state=42)

    # Création et entraînement du modèle
    random_forest = RandomForestRegressor(oob_score=True)
    random_forest.fit(X_train,Y_train)

    # Prédiction sur la base d'apprentissage et la base de test
    Y_train_pred = random_forest.predict(X_train)
    Y_test_pred = random_forest.predict(X_test)
    print("The model score is: ", random_forest.score(X,Y))

    new_data = data.drop(i,axis=1).drop("Date",axis=1).tail(1)
    prediction = random_forest.predict(new_data)
    print("The model predict the last row or days to be: ", prediction)
    print("Actual value is: ", data[[i]].tail(1).values[0][0])

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