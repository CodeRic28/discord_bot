import requests


# response = requests.get("https://www.googleapis.com/books/v1/volumes?q=search+terms")

# title_inp = input("search term: ")
def info(search):
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={search}&"
        f"key=AIzaSyA8Tkh-qUupbgy9dgsP-HkppFTJ-UNeGPk")
    data = response.json()
    items = data['items'][0]
    thumbnail = items['volumeInfo']['imageLinks']['thumbnail']
    book_title = "**Title: **" + str(items['volumeInfo']['title'])
    author = "**Author: **" + str(items['volumeInfo']['authors'][0])
    try:
        publisher = "**Publisher: **" + str(items['volumeInfo']['publisher'])
    except: publisher = "Publisher not found"
    lang = "**Language: **" + str(items['volumeInfo']['language'])
    try:
        desc = "```python" + '\n' + "Description: " + '\n' + str(items['volumeInfo']['description']) + "```"
    except: desc = "Description not found"
    try:
        avg_rate = "**Average Rating: **" + str(items['volumeInfo']['averageRating'])
    except: avg_rate = "Rating not found"
    try:
        rate_count = "**Total Ratings: **" + str(items['volumeInfo']['ratingsCount'])
    except: rate_count = "Rate count not found"
    try:
        mature_rate = "**Maturity Rating: **" + str(items['volumeInfo']['maturityRating'])
    except: mature_rate = "Mature Rating not found"
    try:
        cat = items['volumeInfo']['categories']
        category = "**Category**: "
        items = ", ".join(cat)
        cat = category + items
    except: cat = "Category not found"

    return thumbnail, book_title, author, cat, publisher, lang, mature_rate, avg_rate, rate_count, desc

def other(search):
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={search}&"
        f"key=AIzaSyA8Tkh-qUupbgy9dgsP-HkppFTJ-UNeGPk")
    data = response.json()
    items = data['items'][0]
    thumbnail = items['volumeInfo']['imageLinks']['thumbnail']
    return thumbnail

# print(info('count of monte cristo'))