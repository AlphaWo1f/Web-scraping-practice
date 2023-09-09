from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.amazon.ca/s?k=gaming+mice'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def getnextpage(soup):
    page = soup.find('span;', {'class': 's-pagination-strip'})
    if not page.find('span', {'class': 's-pagination-item s-pagination-next s-pagination-disabled'}):
        url = 'https://www.amazon.ca' + str(page.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})).find('a')['href']
        return url
    else:
        return None


while True:
    soup = getdata(url)
    url = getnextpage(soup)
    if not url:
        break
    print(url)
