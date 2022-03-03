
def test_request_returns_404(client):
    assert client.get("/fake_url").status_code == 404


def test_request_return_404_error_message(client):
    print(client.get("/fake_url").data)
    assert client.get("/fake_url").data == b'{"error":{"reason":"page not found"}}\n'

