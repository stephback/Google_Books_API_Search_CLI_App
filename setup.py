from setuptools import setup, find_packages

setup(
    name= 'Google_Books_API_Search_CLI_App',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"}
)
