def test_root_response(client):
    """Root endpoint returns simple response with running confirmation"""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
