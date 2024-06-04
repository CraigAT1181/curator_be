from flask import request
import logging

def paginate_array(array, total):
    try:
        page = int(request.args.get('page', 1))
        objects_per_page = int(request.args.get('objects_per_page', 8))

        start_index = (page - 1) * objects_per_page
        end_index = min(start_index + objects_per_page, len(array))

        paginated_block = array[start_index:end_index]

        total_pages = (total + objects_per_page - 1) // objects_per_page

        paginated_object = {
            'block': paginated_block,
            'total_pages': total_pages
        }

        return paginated_object
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None, "An unexpected error occurred."

