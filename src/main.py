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

# API_VERSION est le contenu du fichier version qui se trouve dans le meme dossier que le scrip
API_VERSION = open(os.path.join(os.path.dirname(__file__), 'version')).read()

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
