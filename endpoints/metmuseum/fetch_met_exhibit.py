from flask import jsonify
import requests
import logging
from concurrent.futures import ThreadPoolExecutor

def fetch_met_exhibit(object_ID):

    try:
        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

        exhibit_response = requests.get(base_url + str(object_ID))
        if exhibit_response.status_code == 200:
            exhibit_data = exhibit_response.json()
            return {
                "objectID": exhibit_data.get("objectID"),
                "image": exhibit_data.get("primaryImage"),
                "title": exhibit_data.get("title"),
                "date": exhibit_data.get("objectDate"),
                "machineBeginDate": exhibit_data.get("objectBeginDate"),
                "machineEndDate": exhibit_data.get("objectEndDate"),
                "artist": exhibit_data.get("artistDisplayName"),
                "objectType": exhibit_data.get("objectName"),
                "artistWiki": exhibit_data.get("artistWikidata_URL"),
                "objectWiki": exhibit_data.get("objectWikidata_URL"),
                "galleryNumber": exhibit_data.get("GalleryNumber")
            }
        else:
            logging.error(f"Failed to fetch exhibit data for object ID {object_ID}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500