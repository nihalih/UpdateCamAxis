import requests
import json
import os
from requests.auth import HTTPDigestAuth

# Fonction pour envoyer la requête de mise à jour du firmware
def update_firmware(camera_ip, username, password, firmware_file_path):
    url = f"https://{camera_ip}/axis-cgi/firmwaremanagement.cgi"
    headers = {"Content-Type": "multipart/form-data"}
    
    # Vérification si le fichier existe
    if not os.path.isfile(firmware_file_path):
        print(f"Le fichier {firmware_file_path} n'existe pas.")
        return
    
    # Données à envoyer avec la requête
    data = {
        "apiVersion": "1.6",
        "context": "abc",
        "method": "upgrade"
    }
    
    files = {
        'data': (None, json.dumps(data), 'application/json'),
        'firmware': (os.path.basename(firmware_file_path), open(firmware_file_path, 'rb'), 'application/octet-stream')
    }

    # Authentification basique
    auth = HTTPDigestAuth(username, password)


    try:
        # Envoi de la requête POST
        response = requests.post(url, files=files, auth=auth, verify=False)
        
        # Vérification de la réponse
        if response.status_code == 200:
            print(f"Mise à jour du firmware réussie pour la caméra {camera_ip}.")
        else:
            print(f"Erreur lors de la mise à jour pour {camera_ip}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erreur de connexion à {camera_ip}: {e}")

# Lecture des données depuis le fichier JSON
def load_camera_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

# Fonction principale
def main():
    cameras = load_camera_data("cameras.json")
    
    for camera in cameras:
        print(f"Début de la mise à jour pour la caméra {camera['ip']}...")
        update_firmware(camera['ip'], camera['username'], camera['password'], camera['firmware_file'])

if __name__ == "__main__":
    main()
