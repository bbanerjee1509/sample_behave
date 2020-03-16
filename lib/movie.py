# file:/lib/country_api.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
class Movie(object):

    def __init__(self):
        self.response_json_map = {}

    @classmethod
    def set_movie(self, movie_name):
        self.movie_name = movie_name

    def send_api(self):
        url = 'http://www.omdbapi.com/?t=' + self.movie_name + '&apikey=9534a8be'
        response_omdb = requests.get(url, verify=True)
        data_omdb = response_omdb.json()
        self.response_json_map['http_response_code'] = response_omdb.status_code
        self.response_json_map['Title'] = data_omdb['Title']
        self.response_json_map['Year'] = data_omdb['Year']
