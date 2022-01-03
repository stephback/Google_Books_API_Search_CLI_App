#!/usr/bin/env python3


class UserInputParams:
    def __init__(self):
        pass

    def check_empty_search(self, response_info):
        if len(response_info) == 0 or None:
            return True
        elif response_info[1] == ["Title not found.", "Genre not found.", "Keywords not found."]:
            return True
        else:
            return False

    def check_valid_search(self, keywords):
        if keywords in ["intitle", "inauthor", "inpublisher", "insubject"]:
            return True
        else:
            return False

    def check_book_id_num_selected(self, selected_book):
        try:
            if type(int(selected_book)) is int:
                return True
        except ValueError:
            return False

    def check_book_selected_in_book_data(self, selected_book):
        if int(selected_book) in [1, 2, 3, 4, 5]:
            return True
        else:
            return False

    def check_empty_reading_list(self, save_reading_list):
        if len(save_reading_list) == 0:
            return True
        else:
            return False

