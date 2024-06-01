import requests
import logging

def fetch_cleveland_artworks():
    try:
        base_url = "https://openaccess-api.clevelandart.org/api/artworks/?fields=id,title,creation_date,creators,images"
        response = requests.get(base_url)

        if response.status_code == 200:
            json_response = response.json()

            info = json_response.get("info")

            if info:
                total = info.get("total")
            else:
                logging.error("No info key found.")
                return None, "No info key found."

            data = json_response.get("data")

            if data:
                artworks = []
                for artwork in data:
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
                        "id": id,
                        "title": title,
                        "date": creation_date,
                        "image": image,
                        "creators": creators
                    }

                    artworks.append(artwork_info)
                
                return {
                    "artworks": artworks,
                    "total": total
                }, None
            else:
                logging.error("No data key found.")
                return None, "No data key found."
    
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            return None, 'Failed to fetch artworks.'

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None, "An unexpected error occurred."
