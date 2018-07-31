# IMDB-crawler
A web crawler that searches the list of Highest Rated IMDb "Top 1000" Titles by keyword and returns a list of relevant titles.

Functions:

crawl(url)
Takes as input the url string to crawl. By default it is the first page of Highest Rated IMDb "Top 1000" Titles.
Crawls the entire list and builds a dictionary of mapping keywords to movie titles.

search(query)
Takes as input the query string to search.
Will index the crawl results for each word in the query. Returns a list of relevant movie titles.


Instructions:

To run the program, open the terminal and navigate to the IMDBcrawler directory.
Type in python3 crawler.py and press 'Enter'.
The program will then crawl the IMDB website and fill a dictionary.
Once prompted, input a search query and press 'Enter' to search. This will print a list of all movies
related to the terms in the search query.
Input 'quit' or 'q' and press 'Enter' to end the program.


Simplifying assumptions:

I assume that users only search for top-billed actors. This is to avoid adding long lists of lesser-know cast members
to the movie-data dictionary.
I assume users spell all keywords correctly.


Ideas for future improvement:

To speed up web crawling, I would use threading. This way, I could crawl multiple web pages in parallel.
Additionally I would store the results of the crawl to avoid having to crawl on startup. With this addition, I would
add a parameter that kept track of when the data was last updated, and perform a crawl weekly in order to keep
the data up to date.
I would add more indexes for more robust querying. Additional indexes include keywords found in the movie discription,
movie content rating, complete cast, writers, etc.


