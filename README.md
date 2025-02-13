# Script de mise à jour de firmware Axis

## Description
Ce projet Python permet d'effectuer la mise à jour du firmware de caméras Axis via l'API Axis. Le script lit une liste de caméras à mettre à jour depuis un fichier JSON et utilise une authentification HTTP Digest pour sécuriser les requêtes.

## Prérequis
- Python 3 installé https://www.python.org/downloads/
- Environnement virtuel Python (virtual environment) : `pip install virtualenv`
- Fichier `cameras.json` contenant les informations des caméras


## Installation
1. **Cloner le projet (ou télécharger le zip : https://github.com/nihalih/UpdateCamAxis/archive/refs/heads/main.zip)** :
```bash
git clone https://github.com/nihalih/UpdateCamAxis.git
cd repo-axis-firmware
```
2. **Créer et activer l'environnement virtuel pour installer les dépendances** :
```bash
python -m venv axis-env
source axis-env/bin/activate  # Sur Linux/macOS/Gitbash
axis-env\Scripts\activate     # Sur Windows (ADMIN)
```
3. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

## Fichier `cameras.json`
Le fichier JSON doit contenir la liste des caméras avec les informations nécessaires :
```json
[
  {
    "ip": "192.168.1.10",
    "firmware_file": "firmware_v1.2.bin",
    "username": "admin",
    "password": "password",
  },
  {
    "ip": "192.168.1.11",
    "firmware_file": "firmware_v1.3.bin",
    "username": "admin",
    "password": "password",
  }
]
```


## Utilisation
Pour exécuter le script :
```bash
python main.py
```
Le script va parcourir chaque caméra listée dans `cameras.json` et tenter de mettre à jour son firmware.

## Fonctionnement du script
- **Lecture du fichier JSON** : Récupère les informations de chaque caméra.
- **Vérification du fichier de firmware** : Vérifie l'existence du fichier avant l'envoi.
- **Requête API Axis** : Envoie une requête HTTP POST avec authentification HTTP Digest.
- **Affichage du résultat** : Indique si la mise à jour a réussi ou échoué.

## Dépendances
- `requests`

## Fichier `requirements.txt`
```txt
requests
```


