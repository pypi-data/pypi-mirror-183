import requests

class API_Call:
    """
    An API_Call allows you to use the existing API endpoints and it can also assist on serializing data.
    :type base_url: string
    :param base_url: Base url for The One Api Dev
    :type url: string
    :param url: 
    :type method: string
    :param method: GET, POST or other accepted type of method.
    :type access_token: string
    :param access_token: API Key The One API Dev. 

    """
    def __init__(self, base_url="https://the-one-api.dev/v2/",
                 url="", method=None, access_token=None):
        self.base_url = base_url
        self.url = url
        self.method = method
        self.access_token = access_token

    def api_request(self) -> requests.models.Response:
        """
        :return: HttpResponse object from requests library
        """
        response = requests.request(self.method, self.base_url+self.url)
        return(response)


    def serialize_book_names(self) -> str:
        """ 
        :return: list of the book names as string
        :example:
        >>> result = "The Fellowship Of The Ring, The Two Towers, The Return Of The King"
        """

        URL = "https://the-one-api.dev/v2/book/"
        response = requests.get(URL)
        if response.status_code == 200:
            serialized_response = response.json()
            all_books = ", ".join([book['name'] for book in serialized_response['docs']])
            return(all_books)
        return("We failed to reach a successful response from the server. Refer to additional tests to find the cause.")

