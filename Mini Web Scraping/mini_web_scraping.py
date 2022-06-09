'''
Extract from a web scraping sandbox book titles which has more than 3 stars as rating
'''
import bs4
import requests

# url without page number
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# List of titles with 4 or 5 stars
titles_high_rating=[]

# Iterating pages
for page in range (1,11): # number of pages to scrap

    # Create soup for every page
    page_url = url_base.format(page)
    results = requests.get(page_url)
    soup = bs4.BeautifulSoup(results.text, 'lxml')

    # Select data from books
    l_books=soup.select('.product_pod')

    # Iterating books
    for book in l_books:

        # Check 4 or 5 stars
        if len( book.select('.star-rating.Four') )!= 0 or len ( book.select('.star-rating.Five') ):
            
            # Save title
            title = book.select('a')[1]['title']

            # Add title to list
            titles_high_rating.append(title)

# Print results
print('-'*50)
print('\nThe following titles have a minimum rating of 4 stars out of 5 possible\n')
print('-'*50)
print()
for t in titles_high_rating:
    print(t)
