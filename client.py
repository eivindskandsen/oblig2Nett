import requests

response=requests.post( 'http://127.0.0.1:5000/' + "/api/rooms/0", {"room_id": 0, "chat": "0", "members": "0"})

print(response.json())

response=requests.get('http://127.0.0.1:5000/'+ "/api/rooms/0")
print(response.json())