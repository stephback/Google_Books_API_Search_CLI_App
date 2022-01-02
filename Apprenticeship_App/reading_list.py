
# Save selected book to reading list using book id number
class ReadingList:

    def __init__(self, save_reading_list=()):
        self.save_reading_list = save_reading_list

    def save_reading_list(self, book_selected, book_data):
        add_book = book_data[int(book_selected)]
        book_id_num = len(self.save_reading_list) + 1
        self.save_reading_list.update({book_id_num: add_book})
