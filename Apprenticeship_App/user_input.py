
# Books queried by title, author, and publisher through user input
class UserInput:

    def __init__(self, title="", genre="", keywords=""):
        self.title = title
        self.genre = genre
        self.keywords = keywords

    # Use .casefold() to remove case sensitivity of user input strings when compared to Google Books API search strings
    def search_by_title(self):
        title = input("Please enter the book title. If title unavailable, please leave field blank and hit enter.")
        return title.casefold()

    def search_by_genre(self):
        genre = input("Please enter book genre. If genre does not match, please leave field blank and hit enter.")
        return genre.casefold()

    def search_by_keywords(self):
        keywords = input(
            "Please enter keywords for book. If keyword does not match, please leave field blank and hit enter.")
        return keywords.casefold()

    def select_book(self):
        book_selected = input("Please enter the book number you would like to select.")
        return book_selected.casefold()

    def get_user_input(self):
        response_info = input("Please select from the following options: "
                         "1. 'search' - to search for a book."
                         "2. 'select' - to select book and add to reading list."
                         "3. 'view'   - to view your current reading list."
                         "4. 'exit'   - to exit the program.")
        return response_info.casefold()  # casefold() should not interfere with response?

