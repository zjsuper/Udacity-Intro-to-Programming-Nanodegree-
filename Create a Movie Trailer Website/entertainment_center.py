# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes
# my favorite movies
moviesexample = ["The Girl on the Train", "Deadpool","Suicide Squad"]
#trailer of the movies
Trailers = ["https://www.youtube.com/watch?v=y5yk-HGqKmM",
"https://www.youtube.com/watch?v=gtTfd6tISfw",
"https://www.youtube.com/watch?v=BKMgB01MU-w"]
#posters of the movies
posters = ["http://cdn3-www.comingsoon.net/assets/uploads/gallery/the-girl-on-the-train/girlontrainposter.jpg",
"http://www.arageek.com/wp-content/uploads/deadpool-poster-8.jpg",
"http://static.srcdn.com/wp-content/uploads/suicide-squad-movie-2016-poster.jpeg"]
The_Girl_on_the_Train = media.Movie("The Girl on the Train",
									"A girl and a murder.",
									"http://cdn3-www.comingsoon.net/assets/uploads/gallery/the-girl-on-the-train/girlontrainposter.jpg",
									"https://www.youtube.com/watch?v=y5yk-HGqKmM")

Deadpool = media.Movie("Deadpool",
					   "A super hero called Deathpool.",
					   "http://www.arageek.com/wp-content/uploads/deadpool-poster-8.jpg",
					   "https://www.youtube.com/watch?v=gtTfd6tISfw")
Suicide_Squad = media.Movie("Suicide Squad",
							"A super hero team",
							"http://static.srcdn.com/wp-content/uploads/suicide-squad-movie-2016-poster.jpeg",
							"https://www.youtube.com/watch?v=BKMgB01MU-w")

#list of movies
movies = [The_Girl_on_the_Train,Deadpool,Suicide_Squad]

#open movie page
fresh_tomatoes.open_movies_page(movies)

