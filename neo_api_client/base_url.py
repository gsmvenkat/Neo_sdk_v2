import requests
from six.moves.urllib.parse import urlencode

from neo_api_client.urls import BASE_URL


class BaseUrl:
    def __init__(self, ucc):
        self.ucc = ucc

    def get_base_url(self):
        URL = BASE_URL
        headers = {}
        query_params = {
            'id': self.ucc
        }
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        URL += '?' + urlencode(query_params)
        base_url = requests.get(url=URL, headers=headers)
        base_url = base_url.json().get('data').get('baseURL') + '/'
        print(base_url)
        return base_url

