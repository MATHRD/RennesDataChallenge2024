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
En effet, nous avons réalisé une régression linéaire avec un stratégie Backward pour garder uniquement les variables significatives à 3 étoiles. Nous avons fais une exception pour le "Brent Oil Price", qui est  une variable macroéconomique de tendance importante. Nous considérons que les Cryptos sont devenus pour certains des actifs de refuge ou alternatifs. Ainsi, nous avons gardé 11 variables explicatives pour expliquer le "returns_BTC". Pour completer notre analyse de la variable, nous avons réalisé une matrice de corrélation pour déterminer les corrélations positives ou négatives du returns_BTC avec les autres variables et une ACP.

Grâce à notre retaitements des données, nous avons pu commencer à construire notre modèle de Prédiction.

lien code R (mettre les analyses économétriques de Arthur)

Ajout des variables de rendements (returns) de chaques actifs en utilisant le logarithme(prix présent/prix passé). Cela permet de résoudre le problème de non-stationnarité.

## Modèle de prédiction:
Plusieurs modèles de prédictions se présentaient à nous: le modèle ARIMA, la simulation de Monte-Carlo ou encore le modèle de Foret Aléatoire (Random Forest).
Nous nous sommes orientés sur un Random Forest pour réaliser notre prédiction.
Nous devons d'abord implémenter un lag de notre variable à expliquer avant de faire notre régression; y_lag = x + y
On rajoute le rendement passé car le meilleur indicateur d'un rendement futur est le rendement passé.
(--mettre le lien vers le code--)
Graphique d'importance des variables:
![Figure_1](https://github.com/MATHRD/RennesDataChallenge2024/assets/147998549/3117cf3b-2b84-4afd-a23b-3fd4e12d547a)

Nous avons retiré, pour chaque Close_Price, le prix des autres Close_Prise car ils sont interconnectés ainsi que la valeur du SP&500.
Cela nous modifie donc l'importance des variables:

![Figure_2](https://github.com/MATHRD/RennesDataChallenge2024/assets/147998549/c71a8746-084f-47a2-bd5e-6b36c8cf9a64)

Notre modèle obtient un Root-mean-square deviation (RMSE) de ___ ainsi qu'une précison à __%.

# Modèle de secours:
Le domaine informatique et financier est exposé à des risques divers tels que la cybercriminalité, la volatilté extreme d'un titre ou encore des problèmes de con
## Création du portfeuille optimal:
  Dans ce Paragraphe, nous allons détailler notre stratégie d'investisssement innovante. Federal Finance Gestion veut devenir un futur leader de l'Investissement dans les nouvelles technologies et l'investissement responsables. C'est pourquoi, nous allons créer un nouveau livret de placement long terme. il se rapproche de la stratégie du Plan Epargne Logement. A partir du moment ou le dépot est effectué sur le livret, il est alors impossible de retirer le montant investi avant une échéance 5 ans. les avantages sont multiples: premièrement, diminution du risque de retrait massif de la part des déposants. Federal Finance Gestion pourra ainsi sécurisé une certaine mise de fond pour son portefeuille au fil des années. Deuxièmement, Federal Finance Gestion pourra alors entreprendre une stratégie de placement long terme permettant de minimiser les risques de perte du dépot de ses clients. Cette stratégie s'inscrit  dans la volonté de renforcer la confiance envers l'institution et renforcer les investissements dans des cryptos actifs porteurs de projet répondants aux critères ESG.
  Nous allons créer un portefeuille pour chaque crypto-actif associé avec un ASR(Actif sans risque). Nous considérons que les BTC avec l'actif de référence du marché des Crypto-actifs. Alors notre mise de départ initial de 10 000 euros va être investi sur le portefeuille du BTC. 100% de la mise de fond sera sur l'ASR rapportant 0%. en cas de prévision haussière du BTC, on augmentera l'exposition sur la crypto-monnaie à 100%. Ainsi, imaginons que le returns du BTC est de 1%, alors notre portefeuille vaudra maintenant 10 100 euros. nous procederons à une vente de l'équivalent de 100 euros de BTC (soit la plus value) afin de nous assurer un gain. on maintiendra alors 10 000 euros sur le BTC. les 100 euros de plus value seront réaffecter sur le portefeuille N, comprenant une crypto et un ASR. Le portefeuille sélectionné, comprendra la crypto qui a pour valeur de returns le max des rendements prédits. Ainsi au fur et à mesure des gains, nous diversifions sans nous exposer de trop à un risque de perte de la mise initiale. De plus, nous pourrons espérer des gains potentiels futurs sur le Portefeuille N. En cas de prévision baissière, on réduit l'exposition sur la crypto-monnaie de 50%. Ainsi, l'exposition passe de 50% de 100%. Du fait d'une vision long terme, nous relancerons nos prévsions afin de compenser cette perte et finir en positif à la fin de l'année civile. En cas de prévision neutre, on ne modifie pas notre exposition.  En cas de previson haussière du crypto-actif N, on réalisera le même procédé. 
  En fin, les interets seront versés sur le livret à la fin de l'année civile. ils pourront être retirés ou reinvestis par les clients.
 

## Savoir vendre le projet (Pitch Elevator):
Le coté marketing et la présentation représentent une part importante du projet. Nous avons donc consacrer une partie de notre temps afin de proposer une inovation pour entourer notre projet. Pour rappel, le Crédit Mutuel Arkéa
souhaite offrir un fond d'investissement basé sur des portefeuilles d'actifs numériques. Notre idée est donc de basé notre stratégie marketing sur la facilité que ce fond permettra d'apporter à des invidus souhaitant investir dans ce nouvel actif sans y consacrer un temps colossal. En france, 9% de la population possède ou a possédé une cryptomonnaie ce qui signifie qu'une grande part de marché est prete à etre conquise. Cependant les francais restent sceptiques quant à la liquidité, aux formalités d'impositions ou encore la sureté des établissements proposant des actifs numériques (ex: Binance). La création de ce fond permettra donc de combler ces problèmes grace à la notoriéter et la masse d'une banquqe systémique francaise.
Le marketing lié à l'ouverture de ce fond d'investissement proposera donc un rendement par rapport à un niveau de risque (cf création portfeuille) ainsi qu'une simplification de l'accès aux cryptomonnaies.

## Conclusion:


