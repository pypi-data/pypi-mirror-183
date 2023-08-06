from client import API_Call
client = API_Call("https://the-one-api.dev/", "/v2/book/", "GET")
response = client.api_request()
all_books = client.serialize_book_names()