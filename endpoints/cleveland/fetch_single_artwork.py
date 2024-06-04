from flask import jsonify
import requests
import logging

def fetch_single_artwork(object_ID):
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/"
        response = requests.get(f"{base_url}{object_ID}")
        
        if response.status_code == 200:
            json_response = response.json()

            data = json_response.get("data")

            id = data.get("id")
            title = data.get("title")
            creation_date = data.get("creation_date")
            images = data.get("images")
            image = images.get("web")
            creator_details = data.get("creators")
            creators = []
            for person in creator_details:
                creator = person.get("description")
                creators.append(creator)
            collection = data.get("collection")
            department = data.get("department")
            description = data.get("description")
            did_you_know = data.get("did_you_know")
            url = data.get("url")
            
            return jsonify({
                "artwork": {
                    "objectID": id,
                    "title": title,
                    "creation_date": creation_date,
                    "image": image,
                    "creators": creators,
                    "collection": collection,
                    "department": department,
                    "description": description,
                    "did_you_know": did_you_know,
                    "url": url,
                    "museum": "cleveland"
                }
            }), 200
        else:
            logging.error(f"Failed to fetch exhibit data for object ID {object_ID}")
            return jsonify({"error": f"Failed to fetch artwork data. HTTP Status Code: {response.status_code}"}), response.status_code

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500
