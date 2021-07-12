import pytest
import json
from flask_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_base(client):
    """[summary]
        it test check the base endpoint and check if the status cod of 
        the base endpint comes 200 or not
    """
    response= client.get('/')
    assert response.status_code == 200

def test_rasa(client):
    """[summary]
        this test check the status code of endpoint '/get' if the status
        code is 200 or not
    """
    payload= {'msg':'hii'}
    response= client.get('/get',json=payload)
    assert response.status_code == 200