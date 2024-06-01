from flask import jsonify, request
from endpoints.cleveland.fetch_cleveland_artworks import fetch_cleveland_artworks
import logging

def paginate_cleveland_artworks():
    try:
        data, error = fetch_cleveland_artworks()

        if error:
            return jsonify({"message": error}), 500

        artworks = data.get("artworks", [])
        
        page = int(request.args.get('page', 1))
        objects_per_page = int(request.args.get('objects_per_page', 8))

        start_index = (page - 1) * objects_per_page
        end_index = min(start_index + objects_per_page, len(artworks))

        artwork_block = artworks[start_index:end_index]

        total_pages = (data.get("total", 0) + objects_per_page - 1) // objects_per_page

        paginated_object = {
            'artworks': artwork_block,
            'total_pages': total_pages
        }
        
        return jsonify(paginated_object)
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500
