from flask import request
import requests
import logging

def run_met_search():
    try:
        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        params = {
            "isOnView": "true",
            "isHighlight": "true",
            "hasImages": "true",
            "q": request.args.get("keywords")
        }
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            json_response = response.json()
            total = json_response.get("total", 0)
            objectIDs = json_response.get("objectIDs")
            
            if objectIDs is None:
                objectIDs = []

            return {
                "objectIDs": objectIDs,
                "total": total
            }

        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return {"error": f"Failed to fetch data, status code: {response.status_code}"}
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": f"An unexpected error occurred: {e}"}
