import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
json={"userID":1,}
response = requests.post(api_url,json)
response.json()
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}