import webbrowser

class Movie(object):
	""" Movie class contains the following information

        Attributes:
            title: movie title
            storyline: movie storyline
            poster_image_url: movie poster url
            trailer_youtube_url: movie trailer url
			release_year: movie release year 
    """
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,release_year):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_year= release_year

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)