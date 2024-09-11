import requests
import bs4
import re

def get_markup(url):
        return requests.get(url).text

def get_capacity(markup, code):
    soup = bs4.BeautifulSoup(markup, "html5lib")

    # Find class code exists
    row = soup.find('td', class_='data', string=code)

    # Get capacity
    if row:
        parent = row.find_parent('tr')
        capacity = parent.find('td', class_="data", string=lambda text: re.match(r"^\d+/\d+", text.strip()))
        if capacity:
            return capacity.text.strip()

    return "Class code not found"