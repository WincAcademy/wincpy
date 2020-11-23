import pytest

from main import app

@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b'<p>Home, sweet home.</p>'


def test_greet(client):
    response = client.get('/greet/')

    assert response.status_code == 200
    assert response.data == b'<h1>Hello, world!</h1>'

    response = client.get('/greet/bob')

    assert response.status_code == 200
    assert response.data == b'<h1>Hello, bob!</h1>'
