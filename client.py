import requests

response=requests.post( 'http://127.0.0.1:5000/' + "rooms/0", {"id_name": 0, "chat": [], "members": []})

print(response.json())