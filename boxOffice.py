import random
import requests
import bs4
import subprocess

# crawl IMDB Top 250 and randomly select a movie


#BUG: The forign languages comes in its original language. It has to be converted to English first.


url = 'https://www.imdb.com/chart/boxoffice/'

movies = []


def getMovie(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for i in range(1, 10):

        elems = soup.select(
            f"#boxoffice > table > tbody > tr:nth-child(1) > td.titleColumn > a")
        movies.append(elems[0].text.strip())

    #main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.titleColumn > a
    #main > div > span > div > div > div.lister > table > tbody > tr:nth-child(2) > td.titleColumn > a
    return movies


#movies = getMovie(url)
#print(movies)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select(
    "#boxoffice > table > tbody > tr:nth-child(2) > td.titleColumn > a")

print(elems)
