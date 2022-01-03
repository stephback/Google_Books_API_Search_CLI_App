# Google Books API Search CLI App

This book finder application uses Google Books API to search for books based on user input in the command line interface. 

The search returns a list of 5 books matching keywords, genres, or titles provided by user. 

User can select books from list to add to a new list called, "Reading List".

Each result must include: title, author, publisher/company.

## Technologies:
### Python 3.8
 https://www.python.org/about/

### Google Books API documentation:
 https://developers.google.com/books/docs/overview

### PyTest
 https://docs.pytest.org/en/6.2.x/index.html


## Installation:
1. Install python and pip on your computer. To check the current version of Python installed on your computer; open your command line interface and  run the command:

        python3 --version
    Python versions 3.4 and above include pip installation. For earlier Python versions, install pip using your command line interface and run the command:

        pip -- version
        python3 pip install virtualenv

    ### **Download Python:** [Here](https://www.python.org/downloads/)

    ### **Access Python documentation:** [Here](https://docs.python.org/3/index.html)


2. Once python is installed, clone the latest version of this project using the following command in the command line interface:
   
       git clone https://github.com/stephback/Google_Books_API_Search_CLI_App.git

3. Locate local directory with cloned project in command line interface. Once located, find the file named: 

       execute_program_app.py 

4. Once **execute_program_app.py** is located, run the command:

       python3 execute_program_app.py
5. Follow prompts on command line interface. 
## Future implementations:
* Currently, this project lacks tests for the following modules:
  * execute_program_app.py
  * print_app_results.py
* There are TypeError bugs present in the book_finder module due to url, api_key, and query categories consisting of strings and objects. This is causing the api connection to fail.
* In the future, add functionality to view multiple books and save multiple books to reading list.
* Add functionality that handles errors and user input errors better.

