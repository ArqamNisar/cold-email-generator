import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APOLLO_API_KEY")
BASE_URL = "https://api.apollo.io/api/v1"


class ApolloClient:
    def __init__(self):
        self.headers = {
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "X-Api-Key": API_KEY
        }

    def search_people(self, payload: dict):
        url = f"{BASE_URL}/mixed_people/search"
        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()