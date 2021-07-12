import pytest,json
from flask_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_base(client):
    rv=client.get('/')
    assert rv.status_code==200

def test_rasa(client):
    payload={'msg':'hii'}
    rv=client.get('/get',json=payload)
    assert rv.status_code==200