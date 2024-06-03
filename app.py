from flask import Flask
from flask_cors import CORS, cross_origin
from cache import cache
import json
from dotenv import load_dotenv

from endpoints.metmuseum.fetch_met_exhibits import fetch_met_exhibits
from endpoints.metmuseum.fetch_met_exhibit import fetch_met_exhibit

from utils.paginate_cleveland_artworks import paginate_cleveland_artworks
from endpoints.cleveland.fetch_single_artwork import fetch_single_artwork

load_dotenv()

def create_app(config_name='default'):
    app = Flask(__name__)
    CORS(app)

    cache.init_app(app)

    app.config.from_object('config.config')

    @app.route('/', methods=['GET'])
    def get_endpoints():
        file = open('./endpoints.json')
        data = json.load(file)
        return data

    # MET MUSEUM ENDPOINTS
     
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
    
    # CLEVELAND MUSEUM ENDPOINTS

    @app.route('/cleveland_artworks', methods=['GET'])
    @cross_origin()
    def get_cleveland_artworks():
        artworks = paginate_cleveland_artworks()
        
        return artworks
    
    @app.route('/cleveland_artworks/<object_ID>/artworks', methods=['GET'])
    @cross_origin()
    def get_single_cleveland_artwork(object_ID):
        artwork = fetch_single_artwork(object_ID)

        return artwork

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()