from flask import jsonify
from utils.run_met_search import run_met_search
from utils.paginate_array import paginate_array
import requests
import logging

def search_met_exhibits(keywords):
    try:
        search_results = run_met_search(keywords)

        objectID_array = search_results.get("objectIDs")
        total = search_results.get("total")

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
                return jsonify({'error': 'Failed to fetch exhibit data'})

        return jsonify({
            "exhibits": exhibits,
            "total_pages": total_pages
        }), 200
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500
