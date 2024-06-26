from flask import jsonify
from utils.run_cleveland_search import run_cleveland_search
from utils.paginate_array import paginate_array
import logging

def search_cleveland_artworks():
    try:
        search_results = run_cleveland_search()

        if search_results:
            data = search_results.get("artworks")
            total = search_results.get("total")

            paginated_data_array = paginate_array(data, total)

            artwork_array = paginated_data_array.get("block")
            total_pages = paginated_data_array.get("total_pages")

            artworks = []
            for artwork in artwork_array:
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
                "total_pages": total_pages
            }), 200

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"Error": "An unexpected error occurred."}), 500
