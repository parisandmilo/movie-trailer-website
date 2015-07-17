__author__ = 'dklhy'

import webbrowser

class Movie():
    """Function allows storage of movie info"""

    VALID_RATINGS = ["G","PG", "PG-13","NC-16","M-18","R","Unrated"]

    def __init__(self, movie_title, movie_storyline, favourite_part, notable_actors, poster_url, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.favourite_part = favourite_part
        self.actors = notable_actors
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
