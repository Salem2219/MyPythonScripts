from bs4 import BeautifulSoup
import requests
import random
import sys

def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    #random.shuffle(movies)
    return movies



movies= []

for i in range(0, 10):
    movies.append(get_imd_movies("https://www.imdb.com/chart/boxoffice/")[i].text.strip())
    print(f"Loading {int(i/10*100)}%", end='\r')

print(movies)
