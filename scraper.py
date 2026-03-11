# Web scraping logic

import requests

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        return response.text
