from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Endpoint pour convertir un texte en majuscules
@app.route('/toupper')
def toupper():
    text = request.args.get('text', '')
    return text.upper()

# Endpoint pour obtenir la date d'aujourd'hui au format jj/mm/aaaa
@app.route('/date')
def get_date():
    import datetime
    today = datetime.date.today()
    return today.strftime('%d/%m/%Y')

# Variable globale pour stocker la version de l'API
# c'est une variable d'environnement 
API_VERSION = os.environ.get('API_VERSION', '1.0.0')

# Endpoint pour obtenir la version de l'API
@app.route('/version')
def get_version():
    return API_VERSION

# Endpoints bidon
@app.route('/endpoint1')
def endpoint1():
    return 'Ceci est l\'endpoint bidon 1'

@app.route('/endpoint2')
def endpoint2():
    return 'Ceci est l\'endpoint bidon 2'

if __name__ == '__main__':
    app.run(debug=True)
