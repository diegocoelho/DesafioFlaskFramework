

def test_request_returns_404(client):
    response = client.get("/fake_url")
    assert response.status_code == 404
    assert 'error' in response.json and response.json['error']['reason'] == 'page not found'


def test_user_register(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post('/auth/register', json=data)
    assert response.content_type == 'application/json'
    assert 'message' in response.json and response.json['message'] == 'User created'
    assert 'username' in response.json and response.json['username'] == 'testuser'


def test_user_is_taken(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post('/auth/register', json=data)
    assert response.content_type == 'application/json'
    assert 'error' in response.json and response.json['error']['reason'] == 'username is already taken'


def test_login_successful(client):
    username = 'testuser'
    data = {
        'username': username,
        'password': 'testpass'
    }
    response = client.post('/auth/login', json=data)

    assert response.content_type == 'application/json'
    assert 'user' in response.json and 'access' in response.json['user']
    assert 'username' in response.json['user'] and response.json['user']['username'] == username


def test_login_unsuccessful(client):
    data = {
        'username': 'fakeuser',
        'password': 'fakepass'
    }
    response = client.post('/auth/login', json=data)

    assert response.content_type == 'application/json'
    assert 'error' in response.json and response.json['error']['reason'] == 'wrong credentials'


def test_hello_endpoint(client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert 'message' in response.json and response.json['message'] == 'Desafio Flask - Framework'


def test_first_five_unauthorized(client):
    data = {
        'username': 'testuser',
        'password': 'wrongpass'
    }
    response = client.get('/api/records', json=data)
    assert response.status_code == 401


def test_first_five_successful(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post('/auth/login', json=data)
    assert 'user' in response.json and 'access' in response.json['user']
    token = response.json['user']['access']
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    response = client.get('/api/records', headers=headers)
    assert response.status_code == 200
    assert len(response.json) == 5
    assert 'title' in response.json[0] and response.json[0]['id'] is 1
    assert 'title' in response.json[-1] and response.json[-1]['id'] is 5


def test_records_pagination(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post('/auth/login', json=data)
    assert 'user' in response.json and 'access' in response.json['user']
    token = response.json['user']['access']
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    response = client.get('/api/records?page=10&limit=2', headers=headers)
    assert response.status_code == 200
    assert len(response.json) == 2
    assert 'title' in response.json[0] and response.json[0]['id'] is 19
    assert 'title' in response.json[-1] and response.json[-1]['id'] is 20
