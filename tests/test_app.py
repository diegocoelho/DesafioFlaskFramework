

def test_request_returns_404(client):
    assert client.get("/fake_url").status_code == 404


def test_request_return_404_error_message(client):
    assert client.get("/fake_url").data == b'{"error":{"reason":"page not found"}}\n'


def test_user_is_not_registered(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post('/auth/register', json=data)
    assert response.content_type == 'application/json'
    assert response.json['message'] == 'User created' #TODO resolver keyerror
    assert response.json['username'] == 'testuser'


def test_user_is_taken(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post('/auth/register', json=data)
    assert response.content_type == 'application/json'
    assert response.json['error'] == 'username is already taken'

