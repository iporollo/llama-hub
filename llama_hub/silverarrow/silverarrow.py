import requests


class SilverArrowAPI:
    def __init__(self, api_key, base_url):
        self.base_url = base_url
        self.api_key = api_key

    def store(self, texts):
        headers = {"X-API-KEY": self.api_key}
        data = {"texts": texts}
        response = requests.post(
            f"{self.base_url}/api/store", json=data, headers=headers
        )
        response.raise_for_status()
        return response.json()

    def search(self, query, n_results=10):
        headers = {"X-API-KEY": self.api_key}
        data = {"query": query, "n_results": n_results}
        response = requests.post(
            f"{self.base_url}/api/search", json=data, headers=headers
        )
        response.raise_for_status()
        return response.json()
