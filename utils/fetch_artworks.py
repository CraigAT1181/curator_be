from cache import cache
import requests
import logging

@cache.cached(timeout=3600)
def fetch_artworks():
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/?fields=id,title,creation_date,creators,images"
        response = requests.get(base_url)

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
            return {"error": f"Failed to fetch data, status code: {response.status_code}"}
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": f"An unexpected error occurred: {e}"}