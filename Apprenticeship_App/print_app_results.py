#!/usr/bin/env python3


class PrintAppResults:
    def __init__(self):
        pass

    def print_book_data(self, book_data):
        i = 1
        for item in book_data:
            print("Book id #" + str(i) + ':\n')
            print("Title: " + book_data[i][0])
            print("Authors: \n")
        if type(book_data[i][1]) == list:
            for author in book_data[i][1]:
                print(author)
        else:
            print(book_data[i][1])
            print("Publisher: " + book_data[i][2])
            print("*****")
        i += 1

    def print_reading_list(self, save_reading_list):
        j = 1

        for item in save_reading_list:
            print("Book id #" + str(j) + ":\n")
            print("Title: " + save_reading_list[j][0])
            print("Authors: \n")
        if type(save_reading_list[j][1]) == list:
            for author in save_reading_list[j][1]:
                print(author)
        else:
            print(save_reading_list[j][1])
            print("Publisher: " + save_reading_list[j][2])
            print("*****")
        j += 1

    def print_statement(self, statement):
        print("************" * 8)
        print(statement)
        print("************" * 8)
        print("")   # provides space between CLI prompts

