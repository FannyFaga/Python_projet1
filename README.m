# Project: Changer l'adresse MAC avec Python

## Description

Ce script Python permet de modifier l'adresse MAC d'une interface réseau sous Linux. Il utilise la bibliothèque `optparse` pour gérer les arguments en ligne de commande et `subprocess` pour exécuter des commandes système.

## Prérequis

1. *Système d'exploitation* : Linux (Debian, Ubuntu, Kali, etc.).
2. **Permissions root** : Le script doit être exécuté avec des privilèges administratifs (`sudo`).
3. **Python 3** : Assurez-vous que Python 3 est installé sur votre système (`python3 --version`).

## Installation

Si `python3` n'est pas installé, utilisez :
```bash
sudo apt update && sudo apt install python3
```

## Utilisation

###  Télécharger le script
Copiez le script dans un fichier nommé `change_mac.py` :
### 2.Rendre le script exécutable

Dans un terminal, exécutez la commande suivante :
```bash
chmod +x change_mac.py
```

### 3.Exécuter le script

### 4. Vérifier le changement d'adresse MAC
Après exécution, vérifiez si l'adresse MAC a été modifiée avec:
```bash
ifconfig eth0
```
Ou :
```bash
ip link show eth0
```

## Explication du fonctionnement

1. **Lecture des arguments** :
   - L'utilisateur spécifie l'interface et la nouvelle adresse MAC via des arguments en ligne de commande.
2. **Récupération de l'adresse MAC actuelle** :
   - Le script récupère et affiche l'adresse MAC actuelle de l'interface spécifiée.
3. **Changement de l'adresse MAC** :
   - L'interface est désactivée (`down`).
   - La nouvelle adresse MAC est appliquée.
   - L'interface est réactivée (`up`).
4. **Vérification du changement** :
   - Le script récupère et affiche la nouvelle adresse MAC pour confirmer la modification.
 Sécurité
Changer l'adresse MAC peut être détecté par certains systèmes de sécurité réseau. Assurez-vous d'avoir l'autorisation nécessaire avant d'utiliser ce script.



