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
            "title": "Exhibit 1",
            "primaryImage": "image1.jpg",
            "objectDate": "Date 1",
            "objectBeginDate": "Begin Date 1",
            "objectEndDate": "End Date 1",
            "artistDisplayName": "Artist 1",
            "objectName": "Object 1",
            "artistWikidata_URL": "Artist Wiki URL 1",
            "objectWikidata_URL": "Object Wiki URL 1",
            "GalleryNumber": "Gallery 1"
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_fetch_met_exhibit.return_value = mock_response

    response = client.get('/met_exhibits/1/objects')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['objectID'] == 1
    assert data['title'] == "Exhibit 1"
    assert data['primaryImage'] == "image1.jpg"
    assert data['objectDate'] == "Date 1"
    assert data['objectBeginDate'] == "Begin Date 1"
    assert data['objectEndDate'] == "End Date 1"
    assert data['artistDisplayName'] == "Artist 1"
    assert data['objectName'] == "Object 1"
    assert data['artistWikidata_URL'] == "Artist Wiki URL 1"
    assert data['objectWikidata_URL'] == "Object Wiki URL 1"
    assert data['GalleryNumber'] == "Gallery 1"

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
                "collection": "Collection 1",
                "creation_date": "Creation Date 1",
                "creators": ["Creator 1"],
                "department": "Department 1",
                "description": "Description 1",
                "did_you_know": "Interesting Fact 1",
                "image": {
                    "filename": "filename 1",
                    "filesize": "filesize 1",
                    "height": "height 1",
                    "url": "url 1",
                    "width": "width 1"
                },
                "museum": "Museum 1",
                "objectID": 1,  
                "title": "Title 1",
                "url": "URL 1"
            }
        }),
        status=200,
        mimetype='application/json'
    )
    
    mock_fetch_single_artwork.return_value = mock_response

    response = client.get('cleveland_artworks/94979/artworks')

    assert response.status_code == 200
    data = response.get_json()
    assert data['artwork']['title'] == "Title 1"
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