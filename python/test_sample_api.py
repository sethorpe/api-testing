import requests

def test_get_posts():

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # Assert the response returned a 200 status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Convert response body to JSON
    data = response.json()

    # Check that we actually received some posts
    assert len(data) > 0, "Expected one or more posts, got none."