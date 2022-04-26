from bs4 import BeautifulSoup
import requests
import csv

movies = []
exist_movies = []
new_movies = []


def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    return movies


# Get the movies from Box Office in a list
for i in range(0, 10):
    movies.append(get_imd_movies("https://www.imdb.com/chart/boxoffice/")[i].text.strip())
    print(f"Loading {int(i / 10 * 100)}%", end='\r')
print("The movies:", movies)


def get_movies():
    moviesFile = open(r'C:\Projects\MyPythonScripts\movies.csv')
    moviesReader = csv.reader(moviesFile)
    moviesData = list(moviesReader)
    for movie in moviesData:
        exist_movies.append(movie[0])
    print('The exist_movies:', exist_movies)
    moviesFile.close()


# Get the movies from movies.csv
get_movies()

# If the movie is new insert it into a list.
for movie in movies:
    if movie not in exist_movies:
        new_movies.append(movie)

# Write the new movies list in the movies.csv and print them in the screen.
print('The new movies:', new_movies)
moviesFile = open(r'C:\Projects\MyPythonScripts\movies.csv', 'a', newline='')
moviesWriter = csv.writer(moviesFile)
for movie in new_movies:
    moviesWriter.writerow([movie])
moviesFile.close()
