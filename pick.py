import imdb
import random, subprocess, csv

# creating instance of IMDb
ia = imdb.IMDb()

# getting top 250 movies
search = ia.get_top250_movies()
movies = []

for movie in search:
    movies.append(movie['title'])

random_movie = random.sample(movies, 1)

subprocess.Popen(['egy.bat', random_movie[0]])