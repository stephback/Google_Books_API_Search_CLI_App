import os
import sys
import requests
import json
api_key = os.environ['API_KEY']

# Book finder application using Google Books API
# to search for books based on user input.
# The search returns a list of 5 books matching
# keywords, genres, or titles provided by user. User can
# select books from list to add to a new list
# called, "Reading List".Each result must
# include: title, author, publisher/company.
# Google Books API documentation:
# https://developers.google.com/books/docs/overview


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

    ## What happens if the user enters "hello" into command line?
    def query_user(self):
        user_cli_input = self.user_input.get_user_cli_input()
        if user_cli_input == 'search':
            self.search_books()
        elif user_cli_input == 'view':
            self.view_reading_list()
        elif user_cli_input == 'select':
            self.select_book()
        elif user_cli_input == 'exit':
            self.exit_program()
        else:
            self.print_app_results.print_statement(
                "Invalid option. Please choose from the following options: search, view, select, exit")

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
        selected_book = self.user_input.select_book()
        if self.user_input_params.check_book_id_num_selected(
                selected_book) and self.user_input_params.check_book_selected_book_data(selected_book):
            self.reading_list.add_to_reading_list(selected_book, self.book_finder.book_data)
            self.print_app_results.print_statement("Your current reading list: ")
            self.print_app_results.print_reading_list(
                self.reading_list.reading_list)  # Missed setting my class as reading_List so calling same reading_list x2
        else:
            self.print_app_results.print_statement(
                "Invalid selection. Please select book id #'s 1 - 5 to select a book.")
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
        executeProgram = ExecuteProgram(BookFinder(), ReadingList(), UserInput(), UserInputParams(), PrintAppResults())
        executeProgram.start_program()