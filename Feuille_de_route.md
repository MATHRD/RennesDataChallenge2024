### Présentation du sujet
Sujet 2: Forecasting and Tactical allocation for crypto-assets portfolios

"En anticipant les rendements futurs, les sociétés de gestion peuvent améliorer la performance globale des portefeuilles qu'elles gèrent.
Les modèles prédictifs aident à déterminer quels actifs ou combinaisons d'actifs sont susceptibles de fournir les meilleurs rendements.
Cela permet aux gestionnaires de portfeuille de prendre des décisions d'investissements plus informées en allouant des ressources de manière optimale."

#Points d'attention:
1. Données
    -Données de prix et de volume pour 11 crypto-monnaies disctinctes
    -Données macroéconomques et financières
    -Données de sentiments et d'attention
   
3. Attendus
    -Réaliser des prévisions sur un horizon de 1 jour
    -Le nombre de crypto-monnaies considérées pour la prévision sera de 5 au minimum
    -Un backtest financier consistant à simuler une gestion active de portefeuille

3. Critères d'évaluation
    -Présentation orale de la solution
    -Capacité prédictive du modèle (RSME, Taux de bonnes prévisions)
    -Performancede la stratégie d'allocation (Ratio de Sharpe)

##Présentation équipe:
Points forts:
  -Econométrie
  -Connaissances financières et macroéconomiques
  -optimisation de portfeuille
  -Orale/marketing

Points faibles:
  -Machine Learning

##Approche du sujet:
  Le sujet est lié au domaine de la finance avec un besoin de pr

#Filtrage des données:
Nous avons d'abord réalisé un premier filtrage des variables expliquatives de la base de données à partir de nos connaissances macroéconomiqes et financières.
Cela nous a permis de retenir une quarantaine de variables.
Nous avons ensuite sélectioner nos 5 cryptomonnaiess (Bitcoin, Ethereum, Binance Coin, Litecoin et Ripple). Nous avons pris les cryptomonnaies les plus anciennes afin de disposer du plus de données possibles pour réaliser nos entrainements de données (elles s'étalent du 2018-05-08 au 2023-03-24)
Ce nettoyage à été réalisé sur excel dans un premier temps.

*A noté que nous nous sommes d'abords pencher sur la prédiction et l'analyse du prix et rendement du Bitcoin et à la fin réaliser nos prédictions sur les autres actifs numériques.
Le deuxième filtrage a été réalisé sur R via des analyses de corrélations entre la variable à expliquer (Close_BTC) et les variables explicatives.
  
