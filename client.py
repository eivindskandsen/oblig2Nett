import requests
members = []
response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Martin"})
print(response.json())
user_id = response.json()
response = requests.get('http://127.0.0.1:5000/' + "/api/users")
print(response.json())
response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Mart"})
print(response.json())
response = requests.get('http://127.0.0.1:5000/' + "/api/users")
print(response.json())
response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Marti"})
print(response.json())
response = requests.get('http://127.0.0.1:5000/' + "/api/users")
print(response.json())

response = requests.delete('http://127.0.0.1:5000/' + f"/api/user/{user_id}")
print(response)

response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Martin"})
print(response.json())

response = requests.get('http://127.0.0.1:5000/' + "/api/users")
print(response.json())


