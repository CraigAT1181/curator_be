from flask import jsonify, request
from utils.fetch_all_met_object_IDs import fetch_all_met_object_IDs
import logging

def paginate_met_object_IDs():
    try:
        met_response_object = fetch_all_met_object_IDs()

        object_ID_array = met_response_object.get('objectIDs', [])
        
        page = int(request.args.get('page', 1))

        objects_per_page = int(request.args.get('objects_per_page', 8))

        start_index = (page - 1) * objects_per_page
        end_index = min(start_index + objects_per_page, len(object_ID_array))

        object_ids_block = object_ID_array[start_index:end_index]

        total_pages = (met_response_object.get("total", 0) + objects_per_page - 1) // objects_per_page

        print("Start Index:", start_index)
        print("End Index:", end_index)
        print("Object IDs Block:", object_ids_block)
        print("Total Pages:", total_pages)

        paginated_object = {
            'object_ids': object_ids_block,
            'total_pages': total_pages
        }
        
        return paginated_object
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500
