from flask import jsonify
from cache import cache
import requests
import logging

@cache.cached(timeout=3600)
def fetch_all_met_object_IDs():
    try:
        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        response = requests.get(base_url)

        if response.status_code == 200:
            data = response.json()
            
            result = {
                "total": data.get("total", 0),
                "objectIDs": data.get("objectIDs", [])
            }

            return result
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return jsonify({"error": "Failed to fetch object IDs", "status_code": response.status_code}), response.status_code
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500