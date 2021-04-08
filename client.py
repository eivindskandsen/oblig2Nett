import requests

def start():
#response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Martin"})
#print(response.json())
#print(response)

    #response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Mart"})
    #print(response.json())

    #response=requests.post('http://127.0.0.1:5000/'+ /api
#response = requests.delete('http://127.0.0.1:5000/' + "/api/user/0")
#print(response)

#response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": "Marty"})
#print(response.json())

#response = requests.get('http://127.0.0.1:5000/' + "/api/users")
#print(response.json())

#response = requests.get('http://127.0.0.1:5000/' + "/api/user/2")
#print(response.json())

    #response =requests.post('http://127.0.0.1:5000/' + "/api/rooms/0", {"room_id" : 0})
    #print(response)

    #response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/message", {"chat": "Hallo", "user_id" : 0, "room": 0})
    #print(response.json())

    #response =requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/0/messages")
    #print(response.json())

    ##TESTING##

## rooms
    response= requests.post('http://127.0.0.1:5000/' +"/api/rooms/0", {"room_id":0})
    print(response.json())

    response= requests.post('http://127.0.0.1:5000/' +"/api/rooms/1", {"room_id":1})
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/rooms/0")
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/room/0")
    print(response.json())
## ok

## users
    response=requests.post('http://127.0.0.1:5000/' +"/api/users", {"name": "Eple"})
    print(response.json())

    response=requests.post('http://127.0.0.1:5000/' +"/api/users", {"name": "Tomat"})
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/users")
    print(response.json())

## OK

    response=requests.get('http://127.0.0.1:5000/' +"/api/user/0")
    print(response.json())

    response=requests.delete('http://127.0.0.1:5000/' +"/api/user/2")
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/user/2")
    print(response.json())

##ok

## Room-users


    response=requests.post('http://127.0.0.1:5000/' +"/api/rooms/0/users", {"room_id": 0, "user": 0})
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/rooms/0/users")
    print(response.json())

## ok

### Messages

    response=requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager", {"chat": "halo", "user_id":0, "room_id": 0})
    print(response.json())

    response=requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager", {"chat": "halo", "user_id":0, "room_id": 1})
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager")
    print(response.json())

if __name__ == '__main__':
    start()