## Présentation du sujet
# Sujet 2: Forecasting and Tactical allocation for crypto-assets portfolios

"En anticipant les rendements futurs, les sociétés de gestion peuvent améliorer la performance globale des portefeuilles qu'elles gèrent.
Les modèles prédictifs aident à déterminer quels actifs ou combinaisons d'actifs sont susceptibles de fournir les meilleurs rendements.
Cela permet aux gestionnaires de portfeuille de prendre des décisions d'investissements plus informées en allouant des ressources de manière optimale."

## Points d'attention:
1. Données
    - Données de prix et de volume pour 11 crypto-monnaies disctinctes
    - Données macroéconomques et financières
    - Données de sentiments et d'attention
   
3. Attendus
    - Réaliser des prévisions sur un horizon de 1 jour
    - Le nombre de crypto-monnaies considérées pour la prévision sera de 5 au minimum
    - Un backtest financier consistant à simuler une gestion active de portefeuille

3. Critères d'évaluation
   - Présentation orale de la solution
   - Capacité prédictive du modèle (RSME, Taux de bonnes prévisions)
   - Performance de la stratégie d'allocation (Ratio de Sharpe)

## Présentation équipe: 
Points forts:
- Econométrie
- Connaissances financières et macroéconomiques
- optimisation de portfeuille
- Orale/marketing

Points faibles:
- Machine Learning

## Approche du sujet:
  Le sujet est lié au domaine de la finance associé à de la prédiction. Le double enjeux est de proposer un modèle précis tout en selectionant des variables interressantes (financières, macroéconomiqes, indicateur de sentiment via Deep Learning). Le volume de données, les variables de sentiment comprise entre [-1;1], la dimension temporelle ou encore l'absence de données pour certaine date rend l'analyse plus complexe. C'est pourquoi nous avons du etre précautionneux lors du nettoyage de nos données. 

# Filtrage des données:
Nous avons d'abord réalisé un premier filtrage des variables expliquatives de la base de données à partir de nos connaissances macroéconomiqes et financières.
Cela nous a permis de retenir une quarantaine de variables.
Nous avons ensuite sélectioner nos 5 cryptomonnaiess (Bitcoin, Ethereum, Binance Coin, Litecoin et Ripple). Nous avons pris les cryptomonnaies les plus anciennes afin de disposer du plus de données possibles pour réaliser nos entrainements de données (elles s'étalent du 2018-05-08 au 2023-03-24)
Ce nettoyage à été réalisé sur excel dans un premier temps.

*A noté que nous nous sommes d'abords pencher sur la prédiction et l'analyse du prix et rendement du Bitcoin et à la fin réaliser nos prédictions sur les autres actifs numériques.
Le deuxième filtrage a été réalisé sur R via des analyses de corrélations entre chaques variables à expliquer (Close_BTC, Close_ETH, Close_BNB, Close_LCT, Close_XRP) et les variables explicatives ainsi qu'avec des tests de significativités.
lien code R (mettre les analyses économétriques de Arthur)

Ajout des variables de rendements (returns) de chaques actifs en utilisant le logarithme(prix présent/prix passé). Cela permet de résoudre le problèmede non-stationnarité.

## Modèle de prédiction:
Plusieurs modèles de prédictions se présentaient à nous: le modèle ARIMA, la simulation de Monte-Carlo ou encore le modèle de Foret Aléatoire (Random Forest).
Nous nous sommes orientés sur un Random Forest pour réaliser notre prédiction.
(--mettre le lien vers le code--)
Nous avons retiré, pour chaque Close_Price, le prix des autres Close_Prise car ils sont interconnectés ainsi que la valeur du SP&500
![Figure_1](https://github.com/MATHRD/RennesDataChallenge2024/assets/147998549/167582af-e24d-4d59-abcf-6ce323113e6e)
Cela nous modifie donc l'importance des variables:
![Figure_2](https://github.com/MATHRD/RennesDataChallenge2024/assets/147998549/508ed58d-e48a-4829-b955-6c70e17f107f)
Notre modèle obtient un Root-mean-square deviation (RMSE) de ___ ainsi qu'une précison à __%.

## Création du portfeuille optimal:
  Ce portefeuille se construit grace à la prédiction à 1 jours de nos 5 actifs. A partir de cela, nous pouvons leur attribuer un poids dans le portefeuilles selon notre aversion au risque.

## Savoir vendre le projet (Pitch Elevator):
Le coté marketing et la présentation représentent une part importante du projet. Nous avons donc consacrer une partie de notre temps afin de proposer une inovation pour entourer notre projet. Pour rappel, le Crédit Mutuel Arkéa
souhaite offrir un fond d'investissement basé sur des portefeuilles d'actifs numériques. Notre idée est donc de basé notre stratégie marketing sur la facilité que ce fond permettra d'apporter à des invidus souhaitant investir dans ce nouvel actif sans y consacrer un temps colossal. En france, 9% de la population possède ou a possédé une cryptomonnaie ce qui signifie qu'une grande part de marché est prete à etre conquise. Cependant les francais restent sceptiques quant à la liquidité, aux formalités d'impositions ou encore la sureté des établissements proposant des actifs numériques (ex: Binance). La création de ce fond permettra donc de combler ces problèmes grace à la notoriéter et la masse d'une banquqe systémique francaise.
Le marketing lié à l'ouverture de ce fond d'investissement proposera donc un rendement par rapport à un niveau de risque (cf création portfeuille) ainsi qu'une simplification de l'accès aux cryptomonnaies.

## Conclusion:


