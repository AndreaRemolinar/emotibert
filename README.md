# EMOTIBERT

EMOTIBERT est une application web innovante qui utilise la puissance de l'Intelligence Artificielle et du Deep Learning pour analyser et transformer le sentiment d'un texte en français. Construite avec Django, une populaire plateforme de développement web en Python, EMOTIBERT offre une interface conviviale pour interagir avec les modèles d'apprentissage profond de pointe.
La capacité de comprendre et de manipuler le sentiment d'un texte est cruciale dans de nombreux domaines, allant du service client à l'analyse des médias sociaux. Avec EMOTIBERT, vous pouvez non seulement identifier le sentiment d'une phrase, mais aussi modifier ce sentiment, offrant une flexibilité et une puissance sans précédent pour la génération de texte.
Le processus d'entraînement des modèles d'EMOTIBERT repose sur un ensemble de données contenant des tweets en français. Ces données ont été soigneusement prétraitées et adaptées aux exigences spécifiques de ce projet.
Pour l'analyse des sentiments, nous utilisons le modèle CamemBERT, un modèle de langue française basé sur la populaire architecture BERT de Google. Pour le transfert de style de texte, qui permet de modifier le sentiment d'un texte, nous utilisons le modèle T5, également une réalisation de Google.
La combinaison de ces techniques sophistiquées de NLP (Natural Language Processing) fait d'EMOTIBERT un outil puissant et polyvalent pour le traitement des textes en français. Que vous souhaitiez analyser le sentiment général d'un ensemble de données de textes ou modifier le ton d'une seule phrase, EMOTIBERT offre une solution efficace et facile à utiliser.

## Fonctionnalités

1. **Analyse de sentiment** : EMOTIBERT peut prédire le sentiment d'un texte français. Les sentiments possibles sont frustration, tristesse, colère, joie, et neutre.
2. **Traduction de sentiment** : EMOTIBERT peut traduire le sentiment d'un texte en un autre sentiment sélectionné par l'utilisateur.

## Structure du Projet

- `sentiment.py` : Fichier contenant le code pour le chargement du modèle de prédiction du sentiment et la réalisation des prédictions.
- `translate.py` : Fichier contenant le code pour le chargement du modèle de traduction de sentiment et la réalisation des traductions.
- `views.py` : Fichier contenant le code pour les vues Django, y compris la vue pour l'analyse de sentiment et la vue pour la traduction de sentiment.
- `index.html` : Page Web où les utilisateurs peuvent entrer du texte pour l'analyse de sentiment et la traduction de sentiment.

## Technologies utilisées

- **Backend** : Python, Django
- **Machine Learning** : PyTorch, Transformers (CamemBERT pour la prédiction de sentiment et T5 pour la traduction de sentiment)

## Model d'entrainement pour l'analyse des sentiments

Le modèle pour l'analyse de sentiment est basé sur CamemBERT, un modèle de langue BERT formé spécifiquement pour le français. Utilisé de base 
La bibliothèque Transformers de Hugging Face pour charger ce modèle et adapté à la classification de séquence.

- **Préparation des données**
Charger les données du DataFrame base sur twitter à partir d'un fichier CSV dans un DataFrame pandas. Les données sont divisées en un ensemble
d'entraînement et un ensemble de validation à l'aide de la fonction train_test_split de scikit-learn. Pour éviter les erreurs lors de l'encodage
du texte plus tard, remplire les valeur les valeurs manquantes dans notre texte avec une chaîne.
Ensuite, preparer les données pour CamemBERT en les encodant dans le format requis par le modèle. Cela comprend la tokenisation du texte, l'ajout
de tokens spéciaux, le padding du texte à une longueur maximale et la création d'un masque d'attention qui indique au modèle où se trouve le texte
réel et où se trouve le padding.

Création du modèle
Une fois les données préparées, nous initialisons notre modèle CamemBERT pour la classification de séquence en spécifiant le nombre de labels 
uniques dans nos données. Nous utilisons l'optimiseur Adam avec un taux d'apprentissage très faible et définissons notre fonction de perte comme 
la cross-entropie catégorielle.

Entraînement du modèle
Nous entraînons notre modèle en utilisant notre ensemble d'entraînement et en validant sur notre ensemble de validation. La précision de la 
classification est utilisée comme mesure des performances. Nous entraînons le modèle pendant 3 epochs, mais ce nombre peut être augmenté si 
nécessaire.

Visualisation des résultats
Enfin, nous traçons la perte et la précision de notre modèle sur les ensembles d'entraînement et de validation au fil du temps. Cela nous 
aide à visualiser comment notre modèle s'améliore pendant l'entraînement et à détecter tout signe de surapprentissage si notre modèle commence 
à performer beaucoup mieux sur l'ensemble d'entraînement que sur l'ensemble de validation.



## Model d'entrainement pour le transfert de style

Le modèle que nous utilisons pour le transfert de style est le Transformer T5 de Google. Nous utilisons la bibliothèque Transformers de 
Hugging Face pour charger ce modèle.

Préparation des données
Nous commençons par charger nos données annotées à partir d'un fichier CSV dans un DataFrame pandas. Ensuite, nous définissons une classe 
de Dataset personnalisée qui prend en entrée une phrase et un sentiment, et produit une phrase cible en parallèle.

Ensuite, nous divisons notre Dataset en un ensemble d'entraînement et un ensemble de validation.

Création du modèle
Une fois les données préparées, nous initialisons notre modèle T5. Si une carte graphique est disponible, nous transférons notre modèle 
sur cette carte pour accélérer le calcul.

Entraînement du modèle
Nous entraînons notre modèle en utilisant notre ensemble d'entraînement et en validant sur notre ensemble de validation. Le taux 
d'apprentissage est réglé à 1e-3 et l'optimiseur AdamW est utilisé. Un scheduler est également défini pour ajuster le taux d'apprentissage 
au fur et à mesure de l'entraînement.

Pour chaque époque, nous mettons notre modèle en mode d'entraînement et calculons la perte sur notre ensemble d'entraînement. Nous effectuons 
ensuite une passe arrière pour calculer les gradients, effectuer une étape d'optimisation et mettre à jour notre scheduler.

Après avoir calculé la perte sur l'ensemble d'entraînement, nous mettons notre modèle en mode d'évaluation et calculons la perte sur 
l'ensemble de validation. Nous conservons également un échantillon de sortie de notre modèle pour chaque époque.

Nous utilisons également une logique d'arrêt précoce, où si la perte de validation n'améliore pas pendant un certain nombre d'époques 
consécutives, nous arrêtons l'entraînement et conservons le modèle avec la plus petite perte de validation.

Sauvegarde du modèle
Après l'entraînement, nous sauvegardons les poids de notre modèle et le tokenizer pour une utilisation future.

Visualisation des résultats
Enfin, nous traçons les pertes d'entraînement et de validation au fil des époques pour visualiser comment notre modèle s'est amélioré au 
cours de l'entraînement.

## Comment l'utiliser

1. Clonez ce dépôt.
2. Installez les exigences avec `pip install -r requirements.txt`.
3. Exécutez l'application Django avec `python manage.py runserver`.
