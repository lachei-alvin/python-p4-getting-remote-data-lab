# lib/GetRequester.py

import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to self.url and returns the raw response content (bytes).
        """
        response = requests.get(self.url)
        return response.content  # ✅ Must return the bytes for the test

    def load_json(self):
        """
        Calls get_response_body, decodes the JSON content, and returns
        a Python object (list/dict).
        """
        body = self.get_response_body()
        return json.loads(body)  # ✅ Must return the parsed JSON
