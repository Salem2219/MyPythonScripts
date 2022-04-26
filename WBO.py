import csv
import webbrowser
import imdb
import requests
import bs4


def create_url(movie):
    bad_chars = [';', ':', '!', "*", "(", ")", "'", '.']
    ia = imdb.IMDb()
    year = ia.search_movie(movie)[0]['year']
    for i in bad_chars:
        movie = movie.replace(i, '')
    movie_addr = movie.split()
    movie = '-'.join(movie_addr)
    movie = movie.lower()

    return 'https://esco.egybest.network/movie/' + movie + '-' + str(year)


def url_ok(url):
    # exception block
    try:

        # pass the url into
        # request.hear
        response = requests.head(url)

        # check the status code
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e


def getQuality(ProductUrl):
    res = requests.get(ProductUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(
        "#watch_dl > table > tbody > tr:nth-child(1) > td:nth-child(1)")
    Good_Qualities = ['BluRay', 'WEB-DL', 'DVDRip', 'HDTV']
    return elems[0].text.strip() in Good_Qualities


def insert_to_watched(movie):
    moviesFile = open(r'C:\Projects\MyPythonScripts\watched.csv', 'a', newline='')
    moviesWriter = csv.writer(moviesFile)
    moviesWriter.writerow([movie])
    moviesFile.close()


movies = []
watched = []


def get_movies():
    moviesFile = open(r'C:\Projects\MyPythonScripts\movies.csv')
    moviesReader = csv.reader(moviesFile)
    moviesData = list(moviesReader)
    for movie in moviesData:
        movies.append(movie[0])
    # print('The exist_movies:', movies)
    moviesFile.close()


# Get the movies from movies.csv
get_movies()


def get_watched():
    watchedFile = open(r'C:\Projects\MyPythonScripts\watched.csv')
    watchedReader = csv.reader(watchedFile)
    watchedData = list(watchedReader)
    for movie in watchedData:
        watched.append(movie[0])
    # print('The watched_movies:', watched)
    watchedFile.close()


# Get the watched movies
get_watched()


for movie in watched:
    movies.remove(movie)
# Check the availability for each movie in movies.
for movie in movies:
    print('Name:', movie)
    url = create_url(movie)
    print('check_url:', url_ok(url))
    if url_ok(url):
        print('Good Quality:', getQuality(url))
        if getQuality(url):
            webbrowser.open(url)
            insert_to_watched(movie)
    print('-----------------------------------------')
