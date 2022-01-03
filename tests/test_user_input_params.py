from google_books_api_search_cli_app.user_input_params import UserInputParams
user_input_params = UserInputParams()


# Tests if user input is an empty string
def test_check_empty_search_true():
    assert user_input_params.check_empty_search("") is True

def test_check_empty_search_false():
    assert user_input_params.check_empty_search("Wonky") is False


# Tests if user keyword input is valid
def test_check_valid_search_true():
    assert user_input_params.check_valid_search("inauthor") is True

def test_check_valid_search_false():
    assert user_input_params.check_valid_search("") is False


# Tests if user selected valid book id to "select" book
def test_check_book_id_num_selected_true():
    assert user_input_params.check_book_id_num_selected(4) is True

def test_check_book_id_num_selected_false():
    assert user_input_params.check_book_id_num_selected("two") is False


# Tests if book successfully selected by user
def test_check_book_selected_in_book_data_true():
    assert user_input_params.check_book_selected_in_book_data(2) is True

def test_check_book_selected_in_book_data_false():
    assert user_input_params.check_book_selected_in_book_data(0) is False


# Tests if reading list is empty
def test_check_empty_reading_list_true():
    assert user_input_params.check_empty_reading_list(None) is True

def test_check_empty_reading_list_false():
    assert user_input_params.check_empty_reading_list(2) is False
