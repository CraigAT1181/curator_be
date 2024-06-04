# import pytest
# import requests_mock
# from utils.fetch_all_met_object_IDs import fetch_all_met_object_IDs

# @pytest.fixture
# def mocked_response():
#     with requests_mock.Mocker() as mocker:
#         mock_response = {
#             "total": 1000,
#             "objectIDs": list(range(1, 1001))
#         }
#         mocker.get('https://collectionapi.metmuseum.org/public/collection/v1/objects', json=mock_response)
#         yield mocker

# def test_fetch_all_met_object_IDs(mocked_response):
#     result = fetch_all_met_object_IDs()
    
#     assert len(result['objectIDs']) == 1000