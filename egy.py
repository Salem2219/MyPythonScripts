import webbrowser
import sys
import pyperclip
import imdb
from ABS import remove_nonletter

#BUG: Non English letters are not replaced by English ones.



if len(sys.argv) > 1:
    # Get address from command line.
    movie = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    movie = pyperclip.paste()


ia = imdb.IMDb()
year = ia.search_movie(movie)[0]['year']
movie = remove_nonletter(movie)
movie_addr = movie.split()
movie = '-'.join(movie_addr)
movie = movie.lower()


webbrowser.open('https://esco.egybest.network/movie/' +
                movie + '-' + str(year))