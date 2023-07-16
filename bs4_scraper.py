import requests
from bs4 import BeautifulSoup
import random

auth_list = []
t_count, a_count = 0, -1
books_list = []
quotes_list = []
urls = ['https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once',
        'https://www.goodreads.com/quotes', 'https://www.goodreads.com/list/show/15.Best_Historical_Fiction',
        'https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_',
        'https://www.goodreads.com/list/show/47.Best_Dystopian_and_Post_Apocalyptic_Fiction',
        'https://www.goodreads.com/list/show/3.Best_Science_Fiction_Fantasy_Books']
for url in urls:
    html = requests.get(url).text #opening up connection, grabbing the page
    soup = BeautifulSoup(html, 'html.parser') #html parsing
    auth_name = soup.findAll("div", attrs={"class": "authorName__container"}, recursive=True)
    titles = soup.findAll("a", attrs={"class": "bookTitle"}, recursive=True)
    quotes = soup.findAll("div", attrs={"class": "quoteText"}, recursive=True)

    for title in titles:
        if title != '':
            t_count += 1
            a_count += 1
        name = title.span.get_text()
        books_list.append(name)
    for auth in auth_name:
        a_name = auth.a.span.get_text()
        auth_list.append(a_name)
    for quote in quotes:
        quote_text = quote.get_text()
        quotes_list.append(quote_text)


books = list(zip(books_list, auth_list))

#Print out a random quote from quotes_list
'''num = random.randint(0, len(quotes_list)) -1
text = quotes_list[num]
print(text)'''

# num = random.randint(0, len(books_list)) -1
# print(books_list)
# print(auth_list)
# print(auth_list.index("Gone with the Wind"))
# print(books_list.index('Margaret Mitchell'))
# print(auth_list)
