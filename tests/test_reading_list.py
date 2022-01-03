from google_books_api_search_cli_app.book_finder import BookFinder
from google_books_api_search_cli_app.reading_list import ReadingList

book_data = BookFinder().book_data
save_reading_list = ReadingList()

# Tests reading list functionality: adding and/or replacing(updating) reading list
def test_save_reading_list():
    book_data.update({5: ["Wonky Donkey", "Craig Smith", "Scholastic New Zealand Ltd"]})
    save_reading_list.add_book(5, book_data)
    assert len(save_reading_list) is 5

