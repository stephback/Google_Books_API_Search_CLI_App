#!/usr/bin/env python3


import json
import requests
import os

api_url = "https://www.googleapis.com/books/v1/volumes?q="
api_key = os.environ.get("API_KEY")


class BookFinder:

    def __init__(self, book_data=(),
                 response_info=()):  # replaced book_data={} with book_data=() b/c {} is mutable and broke code.
        self.book_data = book_data
        self.response_info = response_info

    # Search Google Books API based on user input queries (title, genre, keywords)
    def find_queried_books(self, title, genre, keywords):
        if len(title) == 0:
            response_info = requests.get(api_url + genre + ":" + keywords + api_key)
            self.book_data = json.loads(response_info.text)
        elif len(genre) == 0:
            response_info = requests.get(api_url + keywords + api_key)
            self.book_data = json.loads(response_info.text)
        else:
            response_info = requests.get(api_url + genre + ":" + keywords + ":" + title + api_key)
            self.book_data = json.loads(response_info.text)
        return self.response_info

    # Select 5 books from search results
    def select_five_books(self, book_data):
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
                i += 1
            return self.book_data

