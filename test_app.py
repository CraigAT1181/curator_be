import pytest
import json
from flask import Flask
from requests.models import Response
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# ---- MET ENDPOINTS ---- #

# -- successful requests -- #
def test_get_met_exhibits(client, mocker):
    mock_fetch_met_exhibits = mocker.patch('app.fetch_met_exhibits')
    
    mock_response = Flask.response_class(
        response=json.dumps({
            "exhibits": [
                {
                    "objectID": 1,
                    "title": "Exhibit 1"
                },
                {
                    "objectID": 2,
                    "title": "Exhibit 2"
                }
            ],
            "total_pages": 1
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_fetch_met_exhibits.return_value = mock_response

    response = client.get('/met_exhibits')
    
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['exhibits']) == 2
    assert data['exhibits'][0]['title'] == "Exhibit 1"
    assert data['exhibits'][1]['title'] == "Exhibit 2"

def test_get_met_exhibit(client, mocker):
    mock_fetch_met_exhibit = mocker.patch('app.fetch_met_exhibit')
    
    mock_response = Flask.response_class(
        response=json.dumps({
            "objectID": 1,
            "title": "Exhibit",
            "image": "image.jpg",
            "date": "Date",
            "objectBeginDate": "Begin Date",
            "objectEndDate": "End Date",
            "artist": "Artist",
            "objectType": "Object",
            "department": "Department",
            "period": "Period",
            "city": "City",
            "artistWiki": "Artist Wiki URL",
            "objectWiki": "Object Wiki URL",
            "galleryNumber": "Gallery",
            "museum": "Museum"
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_fetch_met_exhibit.return_value = mock_response

    response = client.get('/met_exhibits/1/objects')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["objectID"] == 1
    assert data["title"] == "Exhibit"
    assert data["image"] == "image.jpg"
    assert data["date"] == "Date"
    assert data["objectBeginDate"] == "Begin Date"
    assert data["objectEndDate"] == "End Date"
    assert data["artist"] == "Artist"
    assert data["objectType"] == "Object"
    assert data["department"] == "Department"
    assert data["period"] == "Period"
    assert data["city"] == "City"
    assert data["artistWiki"] == "Artist Wiki URL"
    assert data["objectWiki"] == "Object Wiki URL"
    assert data["galleryNumber"] == "Gallery"
    assert data["museum"] == "Museum"

def test_get_searched_met_exhibits(client, mocker):
    mock_search_met_exhibits = mocker.patch('app.search_met_exhibits')
    
    mock_response = Flask.response_class(
        response=json.dumps({
            "exhibits": [
                {
                    "objectID": 1,
                    "title": "Exhibit 1"
                },
                {
                    "objectID": 2,
                    "title": "Exhibit 2"
                }
            ],
            "total_pages": 1
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_search_met_exhibits.return_value = mock_response

    response = client.get('/met_exhibits/search')
    
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['exhibits']) == 2
    assert data['exhibits'][0]['title'] == "Exhibit 1"
    assert data['exhibits'][1]['title'] == "Exhibit 2"

# ---- CLEVELAND ENDPOINTS ---- #

# -- successful requests -- #
def test_get_cleveland_artworks(client, mocker):
    mock_fetch_cleveland_artworks = mocker.patch('app.fetch_cleveland_artworks')
    
    mock_response = Flask.response_class(
        response=json.dumps({
            "artworks": [
                {
                    "id": 1,
                    "title": "Artwork 1",
                    "date": "date 1",
                    "creators": [
                        "Creator 1"
                    ],
                    "image": {
                        "filename": "filename 1",
                        "filesize": "filesize 1",
                        "height": "height 1",
                        "url": "url 1",
                        "width": "width 1"
                    }
                },
                {
                    "id": 2,
                    "title": "Artwork 2",
                    "date": "date 2",
                    "creators": [
                        "Creator 2"
                    ],
                    "image": {
                        "filename": "filename 2",
                        "filesize": "filesize 2",
                        "height": "height 2",
                        "url": "url 2",
                        "width": "width 2"
                    }
                }
            ],
            "total_pages": 1
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_fetch_cleveland_artworks.return_value = mock_response

    response = client.get('/cleveland_artworks')

    assert response.status_code == 200
    data = response.get_json()
    assert len(data['artworks']) == 2
    assert data['artworks'][0]['title'] == "Artwork 1"
    assert data['artworks'][1]['title'] == "Artwork 2"

def test_get_single_cleveland_artwork(client, mocker):
    mock_fetch_single_artwork = mocker.patch('app.fetch_single_artwork')
    
    mock_response = Flask.response_class(
        response=json.dumps({
            "artwork": {
                "collection": "Collection",
                "creation_date": "Creation Date",
                "creators": ["Creator"],
                "department": "Department",
                "description": "Description",
                "did_you_know": "Interesting Fact",
                "image": {
                    "filename": "filename",
                    "filesize": "filesize",
                    "height": "height",
                    "url": "url",
                    "width": "width"
                },
                "museum": "Museum",
                "objectID": 1,  
                "title": "Title",
                "url": "URL"
            }
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_fetch_single_artwork.return_value = mock_response

    response = client.get('cleveland_artworks/94979/artworks')

    assert response.status_code == 200
    data = response.get_json()
    assert data['artwork']['title'] == "Title"
    assert data['artwork']['objectID'] == 1

def test_get_searched_cleveland_artworks(client, mocker):
    mock_search_cleveland_artworks = mocker.patch('app.search_cleveland_artworks')
    
    mock_response = Flask.response_class(
        response=json.dumps({
            "artworks": [
                {
                    "id": 1,
                    "title": "Artwork 1",
                    "date": "date 1",
                    "creators": [
                        "Creator 1"
                    ],
                    "image": {
                        "filename": "filename 1",
                        "filesize": "filesize 1",
                        "height": "height 1",
                        "url": "url 1",
                        "width": "width 1"
                    }
                },
                {
                    "id": 2,
                    "title": "Artwork 2",
                    "date": "date 2",
                    "creators": [
                        "Creator 2"
                    ],
                    "image": {
                        "filename": "filename 2",
                        "filesize": "filesize 2",
                        "height": "height 2",
                        "url": "url 2",
                        "width": "width 2"
                    }
                }
            ],
            "total_pages": 1
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_search_cleveland_artworks.return_value = mock_response

    response = client.get('/cleveland_artworks/search')

    assert response.status_code == 200
    data = response.get_json()
    assert len(data['artworks']) == 2
    assert data['artworks'][0]['title'] == "Artwork 1"
    assert data['artworks'][1]['title'] == "Artwork 2"