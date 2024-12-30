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

### [wiki](https://github.com/roquetar/Traveaux-ephec/wiki/Script-perso)

## Description du programme

Le programme se lance via le terminal avec la commande suivante :<br>``python script.py [*fichiers_csv]``
avec [*fichiers_csv] les noms des fichiers csv à inclure<br>
Exemple:
``python script.py Alimentation.csv Electronique.csv Mobilier.csv Mix1.csv Mix2.csv``

Les données des fichiers seront ensuite copiés dans la classe Main et lors de la fermeture du programme, les données seront sauvegardées dans le fichier data.csv

Le programme est utilisé par des prompts avec:
+ a → rajouter un produit
+ s → supprimer un produit
+ i → liste des produits sous la forme d'un tableau (trié ou non)
+ q → quitter le programme (les données seront sauvegardées dans data.csv)

## Description des actions disponibles

### Ajout d'un produit

On peut rajouter un produit depuis l'interface avec 'a'<br>
Le programme demande le nom du produit et la quantité via des prompts.  Ensuite il demande si le produit existe déjà dans la database<br>
Si oui, il essaye de rajouter la quantité au produit existant et renvoie une erreur si le produit n'existe pas<br>
Si non, le programme demande le prix unitaire ainsi que la catégorie grâce à des prompts et ensuite il le rajoute<br>

### Supprimer un produit

On peut supprimer un produit depuis l'interface avec 's'<br>
Le programme demande le nom du produit à supprimer<br>
Si le produit existe, il le supprime de la database, sinon il renvoie un message d'erreur

### Information

Le programme affiche un tableau (trié ou non) avec les infos demandées<br>
Un prompt demande par quoi on veut trier (vide si aucun tri)<br>
Un prompt demande les données à afficher (vide si tout afficher)
