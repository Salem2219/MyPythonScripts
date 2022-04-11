import bs4
import requests
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    url = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    url = pyperclip.paste()


def getQuality(ProductUrl):
    res = requests.get(ProductUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(
        "#watch_dl > table > tbody > tr:nth-child(1) > td:nth-child(1)")
    return elems[0].text.strip()


quailty = getQuality(url)

print(quailty)
