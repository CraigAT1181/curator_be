from flask import jsonify
from utils.fetch_met_ids import fetch_met_ids
from utils.paginate_array import paginate_array
import requests
import logging

def fetch_met_exhibits():
    try:
        met_request = fetch_met_ids()

        objectID_array = met_request.get("objectIDs")
        total = met_request.get("total")

        paginated_met_request = paginate_array(objectID_array, total)

        object_ids = paginated_met_request.get("block")
        total_pages = paginated_met_request.get("total_pages")

        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

        exhibits = []
        for object_id in object_ids:
            exhibit_response = requests.get(f"{base_url}{object_id}")
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
                    "objectWiki": exhibit_data.get("objectWikidata_URL"),
                    "museum": "metropolitan"
                }
                exhibits.append(exhibit)
            else:
                 return jsonify({'error': f'Failed to fetch exhibit data: {exhibit_response.status_code}'}), exhibit_response.status_code

        return jsonify({
            "exhibits": exhibits,
            "total_pages": total_pages
        }), 200
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500
