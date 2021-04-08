import requests
#response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Martin"})
#print(response.json())
#print(response)

response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Mart"})
print(response.json())

response = requests.delete('http://127.0.0.1:5000/' + "/api/user/0")
print(response)

#response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Marty"})
#print(response.json())

#response = requests.get('http://127.0.0.1:5000/' + "/api/users")
#print(response.json())

#response = requests.get('http://127.0.0.1:5000/' + "/api/user/2")
#print(response.json())

response =requests.post('http://127.0.0.1:5000/' + "/api/rooms/0", {"room_id" : 0})

response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/message", {"chat": "Hallo", "user_id" : 0, "room": 0})
print(response.json())

response =requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/0/messages")
print(response.json())