from flask import jsonify
import requests
import logging

def search_cleveland_artworks(keywords):
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/?q="
        response = requests.get(f"{base_url}{keywords}")

        if response.status_code == 200:
            json_response = response.json()

            info = json_response.get("info")

            if info:
                total = info.get("total")
            else:
                logging.error("No info key found.")
                return None, "No info key found."

            data = json_response.get("data")

            if data:
                artworks = []
                for artwork in data:
                    id = artwork.get("id")
                    title = artwork.get("title")
                    creation_date = artwork.get("creation_date")
                    images = artwork.get("images")
                    image = images.get("web")
                    creator_details = artwork.get("creators")
                    creators = []
                    for person in creator_details:
                        creator = person.get("description")
                        creators.append(creator)
                
                    artwork_info = {
                        "objectID": id,
                        "title": title,
                        "date": creation_date,
                        "image": image,
                        "creators": creators,
                        "museum": "cleveland"
                    }

                    artworks.append(artwork_info)
                
                return jsonify({
                    "artworks": artworks,
                    "total": total
                })
            else:
                return jsonify({"message": "Couldn't find any results."})
    
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return jsonify({"Error": "Request was unsuccessful."}), {response.status_code}

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"Error": "An unexpected error occurred."}), 500
