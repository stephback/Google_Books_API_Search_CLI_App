#!/usr/bin/env python3

import sys

from App.book_finder import BookFinder
from App.print_app_results import PrintAppResults
from App.reading_list import ReadingList
from App.user_input import UserInput
from App.user_input_params import UserInputParams


# Book finder application using Google Books API
# to search for books based on user input.
# The search returns a list of 5 books matching
# keywords, genres, or titles provided by user. User can
# select books from list to add to a new list
# called, "Reading List".Each result must
# include: title, author, publisher/company.
# Google Books API documentation:
# https://developers.google.com/books/docs/overview

# This class connects all .py files within application and executes the program
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

    # What happens if the user enters "hello" into command line?
    def query_user(self):
        user_input = self.user_input.get_user_input()  # find get_user_input() method
        if user_input == "search":
            self.find_queried_books()
        elif user_input == "view":
            self.view_reading_list()
        elif user_input == "select":
            self.select_books()
        elif user_input == "exit":
            self.exit_program()
        else:
            self.print_app_results.print_statement(
                "Invalid option. Please choose from the following options: search, view, select, exit")
            self.query_user()

    def exit_program(self):
        self.print_app_results.print_statement("Thank you for using the Google Books Search. Have a great day!")
        sys.exit()

    def find_queried_books(self):
        title = self.user_input.search_by_title()
        keyword = self.user_input.search_by_keywords()
        genre = self.user_input.search_by_genre()
        if title == "N/A":
            title = "N/A"
        elif title != "N/A" and not self.user_input_params.check_valid_search(title):
            self.print_app_results.print_statement("Invalid input. Please try again.")
            self.find_queried_books()
        else:
            title = self.user_input.search_title()
        data = self.book_finder.find_queried_books(title, genre, keyword)
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
        book_selected = self.user_input.select_book()
        if self.user_input_params.check_book_id_num_selected(
                book_selected) and self.user_input_params.check_book_selected_book_data(book_selected):
            self.reading_list.save_reading_list(book_selected, self.book_finder.book_data)
            self.print_app_results.print_statement("Your current reading list: ")
            self.print_app_results.print_reading_list(
                self.reading_list.save_reading_list)
        else:
            self.print_app_results.print_statement(
                "Invalid selection. Please select book id #'s 1 - 5 to select a book.")
        self.query_user()

    def view_reading_list(self):
        save_reading_list = self.reading_list.save_reading_list
        if self.user_input_params.check_empty_reading_list(save_reading_list):
            self.print_app_results.print_statement("Your reading list is empty.")
        else:
            self.print_app_results.print_statement("Your current reading list: ")
            self.print_app_results.print_reading_list(save_reading_list)
        self.query_user()


if __name__ == "__main__":
    executeProgram = ExecuteProgram(BookFinder(), ReadingList(),
                                    UserInput(), UserInputParams(),
                                    PrintAppResults())
executeProgram.start_program()
