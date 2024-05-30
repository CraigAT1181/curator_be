import pytest
import json
from flask import Flask
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# ---- MET ENDPOINTS ---- #

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