from google_books_api_search_cli_app.user_input import UserInput
user_input = UserInput()

# Tests if user input title of book or "N/A" and/or entered on prompt
def test_search_by_title():
    assert user_input.search_by_title(user_input.title) is True


# Tests if user input genre of book or "N/A" and/or entered on prompt
def test_search_by_genre():
    assert user_input.search_by_title(user_input.genre) is True


# Tests if user input keywords of book or "N/A" and/or entered on prompt
def test_search_by_keywords():
      assert user_input.search_by_title(user_input.keywords) is True


# Tests if user input book id to select book
def test_select_book():
    assert user_input.select_book(user_input.book_selected) is True

# No test for get_user_input since test_user_input_params tests for valid input

