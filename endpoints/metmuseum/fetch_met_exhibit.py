from flask import jsonify
import requests
import logging

def fetch_met_exhibit(object_ID):

    try:
        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
        response = requests.get(f"{base_url}{object_ID}")

        if response.status_code == 200:
            exhibit_data = response.json()
            
            return jsonify({
                "objectID": exhibit_data.get("objectID"),
                "image": exhibit_data.get("primaryImage"),
                "title": exhibit_data.get("title"),
                "date": exhibit_data.get("objectDate"),
                "machineBeginDate": exhibit_data.get("objectBeginDate"),
                "machineEndDate": exhibit_data.get("objectEndDate"),
                "artist": exhibit_data.get("artistDisplayName"),
                "objectType": exhibit_data.get("objectName"),
                "department": exhibit_data.get("department"),
                "period": exhibit_data.get("period"),
                "city": exhibit_data.get("city"),
                "artistWiki": exhibit_data.get("artistWikidata_URL"),
                "objectWiki": exhibit_data.get("objectWikidata_URL"),
                "galleryNumber": exhibit_data.get("GalleryNumber"),
                "museum": "metropolitan"
            }), 200
        else:
            logging.error(f"Failed to fetch exhibit data for object ID {object_ID}")
            return jsonify({"message": f"Failed to fetch artwork data. HTTP Status Code: {response.status_code}"}), response.status_code


    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500