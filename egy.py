import webbrowser
import sys
import pyperclip
import imdb

#BUG: Non English letters are not replaced by English ones.


bad_chars = [';', ':', '!', "*", "(", ")","'", '.']

if len(sys.argv) > 1:
    # Get address from command line.
    movie = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    movie = pyperclip.paste()


ia = imdb.IMDb()
year = ia.search_movie(movie)[0]['year']
for i in bad_chars:
    movie = movie.replace(i, '')
movie_addr = movie.split()
movie = '-'.join(movie_addr)
movie = movie.lower()


webbrowser.open('https://esco.egybest.network/movie/' +
                movie + '-' + str(year))