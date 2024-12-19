# Traveaux-ephec

### Avant-propos

Ce repositerie github est consacré aux travaux à rendre nécessitant des fichiers et/ou un wiki

## Tables des matières

### Dev2

[tp7-9](/wiki/tp7‐9-dev2)

[script perso](#scriptperso)

### Admin1

[troubleshooting dns](/wiki/Troubleshooting-DNS-sysadmin-I)

[troubleshooting web](/wiki/Troubleshooting-web-sysadmin-I)

# Script perso

## Description du programme

Le programme se lance via le terminal avec la commande suivante :<br>``python script.py [*fichier_csv]``
avec [*fichiers_csv] les noms des fichiers csv à inclure<br>
Exemple:
``python script.py Alimentation.csv Electronique.csv Mobilier.csv Mix1.csv Mix2.csv``

Les données des fichiers seront ensuite copiés dans la classe Main et lors de la fermeture du programme, les données seront sauvegardées dans le fichier data.csv

Le programme est utilisé par des prompts avec:
+ a → rajouter un produit
+ s → supprimer un produit
+ i → liste des produits sous la forme d'un tableau (trié ou non)
+ q → quitter le programme (les données seront sauvegardées dans data.csv)