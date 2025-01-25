import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response
    
    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()
        return response
    
    def put(self, endpoint, data=None):
        response = requests.put(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()
        return response
    
    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response
