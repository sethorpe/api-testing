import pytest
from src.api_client import APIClient

#Fixture for API Client
@pytest.fixture(scope='module')
def api_client():
    base_url = "https://jsonplaceholder.typicode.com"
    return APIClient(base_url)

# Tests GET /posts endpoint
def test_get_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Expected response to be a list"
    assert len(data) > 0, "Expected at least one post"

# Test GET /posts/:id endpoint
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["id"] == post_id, f"Expectec post ID to be {post_id}"

# Test POST /posts endpoint
def test_create_post(api_client):
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = api_client.post("/posts", data=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == new_post['title']
    assert data['body'] == new_post['body']
    assert data['userId'] == new_post['userId']

# Test DELETE /posts/:id endpoint
def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json() == {}
