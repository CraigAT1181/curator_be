from cache import cache
import requests
import logging

@cache.cached(timeout=3600)
def run_cleveland_search(keywords):
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/?q="
        response = requests.get(f"{base_url}{keywords}")

        if response.status_code == 200:
            json_response = response.json()
            
            info = json_response.get("info")

            total = info.get("total", 0)
            data = json_response.get("data", [])

            return {
                "artworks": data,
                "total": total
            }
            
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return []
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []