__author__ = "Kalyan Chakravarthy"
__email__ = "chakravarthik27@gmail.com"
__status__ = "planning"

class searchengine:

    def __init__(self, search_string:str) -> None:
        self.search_string = search_string

    def parse_results(self):
        results = self.search_string
        return results