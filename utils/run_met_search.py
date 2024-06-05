from cache import cache
import requests
import logging

@cache.cached(timeout=3600)
def run_met_search(keywords):
    try:
        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/search?q="
        response = requests.get(f"{base_url}{keywords}")

        if response.status_code == 200:
            json_response = response.json()

            total = json_response.get("total", 0)
            objectIDs = json_response.get("objectIDs", [])
            
            return {
                "objectIDs": objectIDs,
                "total": total
            }
        
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return []
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []