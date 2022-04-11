import requests
import sys
import pyperclip



# create a function
# pass the url


if len(sys.argv) > 1:
    # Get address from command line.
    url = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    url = pyperclip.paste()


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

print(url_ok(url))
