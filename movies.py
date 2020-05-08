from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/"
html = urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
print(soup)
'''
table = soup.find(id="Top-Box-Office")

movies = table.find_all(class_="middle_col")

for movie in movies:
    title = movie.get_text()
    print(title, end=' ')
    link = movie.a.get('href')
    url = 'https://www.rottentomatoes.com' + link
    print(url)
'''