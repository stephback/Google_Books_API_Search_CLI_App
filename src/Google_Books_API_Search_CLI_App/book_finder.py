#!/usr/bin/env python3

import json
import requests
import os

api_url = "https://www.googleapis.com/books/v1/volumes?q="
api_key = os.environ.get("API_KEY")


# This class connects to api using api_key to retrieve requested data from user input
class BookFinder:

    def __init__(self, book_data={},
                 response_info={}):
        self.book_data = book_data
        self.response_info = response_info

    # Search Google Books API based on user input queries (title, genre, keywords)
    def find_queried_books(self, title, genre, keywords):
        if title == "N/A":
            response_info = requests.get(api_url + genre + ":" + keywords + api_key)
            self.book_data = json.loads(response_info.text)
        elif genre == "N/A":
            response_info = requests.get(api_url + keywords + api_key)
            self.book_data = json.loads(response_info.text)
        else:
            response_info = requests.get(api_url + genre + ":" + keywords + ":" + title + api_key)
            self.book_data = json.loads(response_info.text)
        return self.response_info

    # Select 5 books from search results
    def select_five_books(self, book_data):
        i = 1
        for i in range(5):
            try:
                title = book_data["items"][i]["volumeId"]["title"]
            except:
                title = "Title not found."
            try:
                genre = book_data["items"][i]["volumeId"]["genre"]
            except:
                genre = "Genre not found."
            try:
                keywords = book_data["items"][i]["volumeId"]["keywords"]
            except:
                keywords = "Keywords not found."

            self.book_data.update({i: [title, genre, keywords]})
            i += 1
            return self.book_data
