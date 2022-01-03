#!/usr/bin/env python3


class PrintAppResults:
    def __init__(self):

 ## This is broken and I don't know why ln 8
    def print_book_data(self, book_data):
        i = 1
        for item in book_data:
            print('Book id #' + str(i) + ':')
            print('Title: ' + book_data[i][0])
            print('Authors: ')
        if type(book_data[i][1]) == list:
            for author in book_data[i][1]:
                print(author)
        else:
            print(book_data[i][1])
            print('Publisher: ' + book_data[i][2])
            print("#####")
        i += 1

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

