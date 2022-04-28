import re


# Regular Expressions
def find_phone_num(message):
    phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phone_num_regex.findall(message)
    return mo


def remove_nonletter(title: str):
    regex = re.compile(r'\W')
    t = regex.findall(title)
    for i in t:
        if i != ' ':
            title = title.replace(i, '')
    return title


def xmas(text):
    xmas_regex = re.compile(r'\d+\s\w+')
    return xmas_regex.findall(text)


def vowels(message):
    vowel_regex = re.compile(r'[aeiou]', re.I)
    print(vowel_regex.findall(message))


def begins_with_hello(messge):
    begins_with_helo_regex = re.compile(r'^Hello')
    return begins_with_helo_regex.search(messge).group()


def end_with_world(message):
    end_with_world_regex = re.compile(r'world!$')
    return end_with_world_regex.search(message).group()


def allDigit(text):
    all_digits_regex = re.compile(r'^\d+$')
    return all_digits_regex.search(text).group()


def at(text):
    atRegex = re.compile(r'.{1,2}at')
    return atRegex.findall(text)


def name(text):
    nameRegex = re.compile('First Name: (.*) Last Name: (.*)')
    return nameRegex.findall(text)


def nongreedy(text):
    nongreedy_regex = re.compile(r'<(.*?)>')
    return nongreedy_regex.findall(text)


def dotStar(text):
    dot_star = re.compile(r'.*', re.DOTALL)
    return dot_star.search(text).group()


def names(text):
    names_regex = re.compile('Agent \w+')
    return names_regex.sub('REDACTED', text)

def names2(text):
    names_regex = re.compile('Agent (\w)\w*')
    return names_regex.sub('Agent \1****', text)


