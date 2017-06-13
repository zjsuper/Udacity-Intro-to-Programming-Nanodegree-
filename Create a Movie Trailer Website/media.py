import webbrowser
#define the Movie class
class Movie():
	def __init__(self,movie_title, movie_storyline,poster_image, trailer_youtube):#create space for object
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
# open the trailer page
	def show_trailer(self): 
		webbrowser.open(self.trailer_youtube_url)