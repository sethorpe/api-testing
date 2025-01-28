import requests
from .logging_util import log_api_calls

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @log_api_calls
    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response
    
    @log_api_calls
    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()
        return response
    
    @log_api_calls
    def put(self, endpoint, data=None):
        response = requests.put(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()
        return response
    
    @log_api_calls
    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response