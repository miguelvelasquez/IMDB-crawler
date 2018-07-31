import re
import urllib.request
from bs4 import BeautifulSoup



movie_data = {}
non_keywords = ["the, of, and, or, but, if, a"]
domain = 'https://www.imdb.com'

list_url = 'https://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=simple'


def crawl(url=list_url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    get_movies(soup)
    next = soup.find("a", {"class": "lister-page-next next-page"})
    if next:
        nexturl = next.get('href')
        crawl(domain + '/search/title' + nexturl)


def get_movies(soup):
    movies = soup.findAll("span", {"class": "lister-item-header"})
    for movie in movies:
        link = movie.a
        url = domain + link.get('href')
        title = link.text
        store_title(title)
        scrape_movie_data(url, title)


def store_title(title):
    title_words = re.sub(r'[^\w\s]', '', title).lower().split()
    for word in title_words:
        if word not in non_keywords:
            put_index(word.lower(), title)


def put_index(index, title):
    if index not in movie_data:
        movie_data[index] = [title]
    else:
        val = movie_data[index]
        if title not in val:
            val.append(title)


def scrape_movie_data(url, title):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    year = soup.find("span", {"id": "titleYear"}).a.text
    if year:
        put_index(year.lower(), title)

    rating = soup.find("span", {"itemprop": "ratingValue"}).text
    if rating:
        put_index(rating.lower(), title)

    genre = soup.findAll("span", {"itemprop": "genre"})
    if genre:
        for g in genre:
            put_index(g.text.lower(), title)

    director = soup.find("span", {"itemprop": "director"}).a.span.text
    if director:
        names = director.split()
        for name in names:
            put_index(name.lower(), title)

    cast = soup.findAll("td", {"itemprop": "actor"})
    if cast:
        for actor in cast:
            names = actor.span.text.split()
            for name in names:
                put_index(name.lower(), title)


def search(query):
    terms = re.sub(r'[^\w\s]', '', query).lower().split()
    results = None
    for term in terms:
        if term not in movie_data:
            continue
        term_results = movie_data[term]
        if not results:
            results = term_results
        else:
            results = [res for res in results if res in term_results]
    return results


if __name__ == '__main__':
    print("Crawling IMDB and filling dictionary...")
    crawl()
    print("Crawl complete!")
    while True:
        query = input("Enter a your query here and press enter to search: ")
        if query == "quit" or query == "q":
            break
        results = search(query)
        print(results)



