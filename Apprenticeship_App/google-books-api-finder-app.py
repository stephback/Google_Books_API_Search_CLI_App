import sys

import requests
import json


# Book finder application using Google Books API
# to search for books based on user input.
# The search returns a list of 5 books matching
# keywords, genres, or titles provided by user. User can
# select books from list to add to a new list
# called, "Reading List".Each result must
# include: title, author, publisher/company.
# Google Books API documentation:
# https://developers.google.com/books/docs/overview
import self as self


class BookFinder:

    def __init__(self, book_data=(),
                 response_info=()):  # replaced book_data={} with book_data=() b/c {} is mutable and broke code.
        self.book_data = book_data
        self.response_info = response_info

        # intended to use token.API_KEY in Get requests below:
        # self.token = token.API_KEY

        # reusable request object. Session and HTTP header auth not needed for GET request.
        # self.session = Session()

    # Search Google Books API based on user input queries (title, genre, keywords)
    def find_queried_books(self, title, genre, keywords):
        if len(title) == 0:
            response = requests.get(
                '/books/v1/volumes?q=' + genre + ':' + keywords + '&key=AIzaSyA40_OJgYUMpwc3_gbarp4iWt7N9Q7qCpQ')
            self.book_data = json.loads(response.text)
        elif len(genre) == 0:
            response = requests.get('/books/v1/volumes?q=' + keywords + '&key=AIzaSyA40_OJgYUMpwc3_gbarp4iWt7N9Q7qCpQ')
            self.book_data = json.loads(response.text)
        else:
            response = requests.get(
                '/books/v1/volumes?q=' + genre + ':' + keywords + ':' + title + '&key=AIzaSyA40_OJgYUMpwc3_gbarp4iWt7N9Q7qCpQ')
            self.book_data = json.loads(response.text)
        return self.response_info

    # Select 5 books from search results
    def select_five_books(self, book_data):
        j = 1  # define j to add selected book until 5 books selected
        for i in range(5):
            try:
                title = book_data["items"][i]["volumeId"]["title"]
            except:
                title = "title not found."  # except throwing "too broad" error. How is this handled w/o disabling interpreter?
            try:
                genre = book_data["items"][i]["volumeId"]["genre"]
            except:
                genre = "genre not found."
            try:
                keywords = book_data["items"][i]["volumeId"]["keywords"]
            except:
                keywords = "keywords not found."
            else:
                self.book_data.update()
                j += 1
            return self.book_data


# Save selected book to reading list using book id number
class ReadingList:

    def __init__(self, save_reading_list=()):
        self.save_reading_list = save_reading_list

    def save_reading_list(self, book_selected, book_data):
        add_book = book_data[int(book_selected)]
        book_id_num = len(self.save_reading_list) + 1
        self.save_reading_list.update({book_id_num: add_book})


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
        response = input("Please select from the following options: "
                         "1. 'search' - to search for a book."
                         "2. 'select' - to select book and add to reading list."
                         "3. 'view'   - to view your current reading list."
                         "4. 'exit'   - to exit the program.")
        return response.casefold()  # casefold() should not interfere with response?


class UserInputParams:
    def __init__(self):
        pass

    def check_empty_search(self, response_info):
        if len(response_info) == 0 or None:
            return True
        else:
            return False

    def check_valid_search(self, keywords):
        if keywords in ['intitle', 'inauthor', 'inpublisher', 'insubject']:
            return True
        else:
            return False

    def check_book_id_num_selected(self, book_selected):
        try:
            if type(int(book_selected)) is int:
                return True
        except ValueError:
            return False

    def check_book_selected_in_book_data(self, book_selected):
        if int(book_selected) in [1, 2, 3, 4, 5]:
            return True
        else:
            return False

    def check_empty_reading_list(self, save_reading_list):
        if len(save_reading_list) == 0 or None:
            return True
        else:
            return False


class PrintAppResults:
    def __init__(self):
        pass

    def print_book_data(self, book_data):
        j = 1  # define j to iterate through to create book id # and print fields
        for item in book_data:
            print('Book id #' + str(j) + ':')
            print('Title: ' + book_data[j][0])
            print('Authors: ')
            if type(book_data[j][1]) == list:
                for author in book_data[j][1]:
                    print(author)
            else:
                print(book_data[j][1])
            print('Publisher: ' + book_data[j][2])
            print("#####")
            j += 1

    def print_reading_list(self, save_reading_list):
        j = 1
        for item in save_reading_list:
            print('Book id #' + str(j) + ':')
            print('Title: ' + save_reading_list[j][0])
            print('Authors: ')
            if type(save_reading_list[j][1]) == list:
                for author in save_reading_list[j][1]:
                    print(author)
            else:
                print(save_reading_list[j][1])
            print('Publisher: ' + save_reading_list[j][2])
            print("#####")
            j += 1


class ExecuteProgram:

    def __init__(self, book_finder, reading_list, user_input, user_input_params, print_app_results):
        self.book_finder = book_finder
        self.reading_list = reading_list
        self.user_input = user_input
        self.user_input_params = user_input_params
        self.print_app_results = print_app_results

    def start_program(self):
        self.print_app_results.print_statement("Greetings! Welcome to the Google Books Search! "
                                               "To exit the program at any time, type 'exit'.")
        self.query_user()

    def query_user(self):
        user_cli_input = self.user_input.get_user_cli_input()
        if user_cli_input == 'search':
            self.search_books()
        elif user_cli_input =='view':
            self.view_reading_list()
        elif user_cli_input == 'select':
            self.select_book()
        elif user_cli_input == 'exit':
            self.exit_program()
        else:
            self.print_app_results.print_statement("Invalid option. Please choose from the following options: search, view, select, exit")

    def exit_program(self):
        self.print_app_results.print_statement("Thank you for using the Google Books Search. Have a great day!")
        sys.exit()

    def search_books(self):
        title = self.user_input.get_search_title()
        keyword = self.user_input.get_search_keyword()
        genre = self.user_input.get_search_genre()
        if title == 0:
            title = 0
        elif title != 0 and not self.user_input_params.check_valid_search(title):
            self.print_app_results.print_statement("Invalid input. Please try again.")
            self.search_books()
        else:
            title = self.user_input.get_search_title()
        data = self.book_finder.search_for_books(title, genre, keyword)
        book_data = self.book_finder.select_five_books(data)
        if self.user_input_params(book_data):
            self.print_app_results.print_statement("Invalid input. Please try again.")
        else:
            self.print_app_results.print_book_data(book_data)
        self.query_user()

    def select_books(self):
        if self.user_input_params.check_empty_search(self.book_finder.book_data):
            self.print_app_results.print_statement("Please search for books to add to your reading list.")
            self.query_user()
        selected_book = self. user_input.select_book()
        if self.user_input_params.check_book_id_num_selected(selected_book) and self.user_input_params.check_book_selected_book_data(selected_book):
            self.reading_list.add_to_reading_list(selected_book, self.book_finder.book_data)
            self.print_app_results.print_statement("Your current reading list: ")
            self.print_app_results.print_reading_list(self.reading_list.reading_list) # Missed setting my class as reading_List so calling same reading_list x2
        else:
            self.print_app_results.print_statement("Invalid selection. Please select book id #'s 1 - 5 to select a book.")
        self.query_user()

    def view_reading_list(self):
        reading_list = self.reading_list.reading_list
        if self.user_input_params.check_empty_reading_list(reading_list):
            self.print_app_results.print_statement("Your reading list is empty.")
        else:
            self.print_app_results.print_statement("Your current reading list: ")
            self.print_app_results.print_reading_list(reading_list)
        self.query_user()
    if __name__ == '__main__':
        executeprogram = ExecuteProgram(BookFinder(), ReadingList(), UserInput(), UserInputParams(), PrintAppResults())
        executeprogram.start_program()
# For some reason, my ExecuteProgram class is not being recognized on line 259
