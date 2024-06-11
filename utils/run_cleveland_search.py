from flask import request
import requests
import logging

def run_cleveland_search():
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/"
        params = {
            "q": request.args.get("keywords")
        }
        response = requests.get(base_url, params=params)

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