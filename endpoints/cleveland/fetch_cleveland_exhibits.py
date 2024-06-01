from flask import jsonify
import requests
import logging

def fetch_cleveland_exhibits():
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/?fields=id,title,creation_date,creators,images"
        response = requests.get(base_url)

        if response.status_code == 200:
            json_response = response.json()

            info = json_response.get("info")

            if info:
                total = info.get("total")
            else:
                return jsonify({"error": "No info key found."}), 500

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
                        "id": id,
                        "title": title,
                        "date": creation_date,
                        "image": image,
                        "creators": creators
                    }

                    artworks.append(artwork_info)
                
                return jsonify({
                    "artworks": artworks,
                    "total": total
                })
            else:
                return jsonify({"error": "No data key found."}), 500
    
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return jsonify({'error': 'Failed to fetch artworks.'}), response.status_code

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500