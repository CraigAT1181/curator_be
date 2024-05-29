from flask import Flask
from flask_cors import CORS, cross_origin
from cache import cache
import json
from dotenv import load_dotenv

from endpoints.metmuseum.fetch_met_exhibits import fetch_met_exhibits
from endpoints.metmuseum.fetch_met_exhibit import fetch_met_exhibit

load_dotenv()

app = Flask(__name__)
CORS(app)

cache.init_app(app)

app.config.from_object('config.config')

@app.route('/', methods=['GET'])
def get_endpoints():
    file = open('./endpoints.json')
    data = json.load(file)
    return data

@app.route('/met_exhibits', methods=['GET'])
@cross_origin()
def get_met_exhibits():
    exhibits = fetch_met_exhibits()
    
    return exhibits

@app.route('/met_exhibits/<object_ID>/objects', methods=['GET'])
@cross_origin()
def get_met_exhibit(object_ID):
    exhibit = fetch_met_exhibit(object_ID)
    
    return exhibit

if __name__ == "__main__":
    app.run()