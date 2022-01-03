import requests

from google_books_api_search_cli_app.book_finder import BookFinder, api_url, api_key

book_finder = BookFinder()


# Tests API connection
def test_find_queried_books_connection_success():
    title = "wonky donkey"
    genre = "childrens"
    keywords = "wonky"
    url_status = requests.get(api_url + genre + "+" + keywords + ":" + title + api_key)
    assert url_status.status_code == 200  # 200 = successful connection

# Tests five books selected from queried books
def test_select_five_books():
    title = "wonky donkey"
    genre = "childrens"
    keywords = "wonky"
    search_data = book_finder.find_queried_books(title, genre, keywords)
    book_data = book_finder.select_five_books(search_data)
    assert len(book_data) == 5
