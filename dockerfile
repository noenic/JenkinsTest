# Utilisez l'image Python officielle comme base
FROM python:3.8-slim-buster

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . .

# Installez les dépendances Python
RUN pip install -r requirements.txt 

# Port sur lequel l'application Flask écoutera
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "src/main.py"]

