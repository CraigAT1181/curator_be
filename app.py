from flask import Flask, request
from flask_cors import CORS, cross_origin
from cache import cache
import json
from dotenv import load_dotenv

# MET IMPORTS
from endpoints.metmuseum.fetch_met_exhibits import fetch_met_exhibits
from endpoints.metmuseum.fetch_met_exhibit import fetch_met_exhibit
from endpoints.metmuseum.search_met_exhibits import search_met_exhibits

# CLEVELAND IMPORTS
from endpoints.cleveland.fetch_cleveland_artworks import fetch_cleveland_artworks
from endpoints.cleveland.fetch_single_artwork import fetch_single_artwork
from endpoints.cleveland.search_cleveland_artworks import search_cleveland_artworks

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

    # ---------------- MET MUSEUM ENDPOINTS -----------------
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

    @app.route('/met_exhibits/search', methods=['GET'])
    @cross_origin()
    def get_searched_met_exhibits():
        keywords = request.get_json()
        artworks = search_met_exhibits(keywords)
        
        return artworks
    
    # --------------- CLEVELAND MUSEUM ENDPOINTS -------------
    @app.route('/cleveland_artworks', methods=['GET'])
    @cross_origin()
    def get_cleveland_artworks():
        artworks = fetch_cleveland_artworks()
        
        return artworks
    
    @app.route('/cleveland_artworks/<object_ID>/artworks', methods=['GET'])
    @cross_origin()
    def get_single_cleveland_artwork(object_ID):
        artwork = fetch_single_artwork(object_ID)

        return artwork
    
    @app.route('/cleveland_artworks/search', methods=['GET'])
    @cross_origin()
    def get_searched_cleveland_artworks():
        keywords = request.get_json()
        artworks = search_cleveland_artworks(keywords)
        
        return artworks

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()