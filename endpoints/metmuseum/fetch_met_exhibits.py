from flask import jsonify
from utils.paginate_met_object_IDs import paginate_met_object_IDs
import requests
import logging

def fetch_met_exhibits():
    try:
        paginated_met_response = paginate_met_object_IDs()

        object_IDs = paginated_met_response.get("object_ids")
        total_pages = paginated_met_response.get("total_pages")

        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

        exhibits = []
        for object_ID in object_IDs:
            exhibit_response = requests.get(base_url + str(object_ID))
            if exhibit_response.status_code == 200:
                exhibit_data = exhibit_response.json()
                exhibit = {
                    "objectID": exhibit_data.get("objectID"),
                    "image": exhibit_data.get("primaryImage"),
                    "title": exhibit_data.get("title"),
                    "date": exhibit_data.get("objectDate"),
                    "machineBeginDate": exhibit_data.get("objectBeginDate"),
                    "machineEndDate": exhibit_data.get("objectEndDate"),
                    "artist": exhibit_data.get("artistDisplayName"),
                    "objectType": exhibit_data.get("objectName"),
                    "artistWiki": exhibit_data.get("artistWikidata_URL"),
                    "objectWiki": exhibit_data.get("objectWikidata_URL")
                }
                exhibits.append(exhibit)
            else:
                return jsonify({'error': 'Failed to fetch exhibit data'})

        return jsonify({
            "exhibits": exhibits,
            "total_pages": total_pages
        })
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500
