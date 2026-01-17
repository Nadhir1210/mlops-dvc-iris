# mlops-dvc-iris

Ce projet illustre l'utilisation de **DVC** pour le versionnage de données avec un remote **MinIO** (S3 local).

## Configuration de l'environnement

### 1. Lancer MinIO
Utilisez Docker Compose pour démarrer le serveur MinIO :
```bash
docker-compose up -d
```
- **Console Web** : [http://localhost:9001](http://localhost:9001)
- **Identifiants** : `minio` / `minio12345`

### 2. Configuration DVC
Le projet est déjà initialisé avec DVC. Pour configurer le remote local :
```bash
dvc remote add -d storage s3://mlops-dvc
dvc remote modify storage endpointurl http://localhost:9000
dvc remote modify storage use_ssl false
dvc remote modify storage region us-east-1
dvc remote modify storage access_key_id minio
dvc remote modify storage secret_access_key minio12345
```

### 3. Pipeline de données
Pour reproduire l'entraînement du modèle :
```bash
dvc repro
```
Cela exécute `src/train.py` et génère `models/model.pkl`.

### 4. Synchronisation
- **Push** : `dvc push` pour envoyer les données vers MinIO.
- **Pull** : `dvc pull` pour récupérer les données depuis MinIO.

## Captures d'écran

### État de MinIO (Bucket)
![MinIO Bucket](screenshots/minio_bucket.png)

### Status du conteneur MinIO
![MinIO Status](screenshots/minio_status.png)

## Vérifications
- Local : `dvc status`
- Cloud : `dvc status --cloud`
