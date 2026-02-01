import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response)
print(response.json())

data = {'userId': 3, 'id': 47, 'title': 'for test'}
response = requests.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())