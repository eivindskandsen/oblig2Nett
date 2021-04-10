import requests

def start():


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

    response=requests.post('http://127.0.0.1:5000/' + "/api/rooms/1/0/messager", {"chat": "halo", "user_id":0, "room_id": 1})
    print(response.json())

# Messager Finds all messsages in all rooms user are in
    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager")
    print(response.json())

#


    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/0/messages")
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/1/0/messages")
    print(response.json())

## ok


class post_user:
    index=0
    navn="Make user"
    def method(self):
        name=input("skriv navn: ")
        response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": name})
        print(response.json())

class post_room:
    index=1
    navn="Make room"
    def method(self):
        room=input("Write room number: ")
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0", {"room_id": room})
        print(response.json())

class post_message:
    index=2
    navn="Post Message in room"
    def method(self):
        chat=input("Hva er meldingen: ")
        user_id=input("Your user id: ")
        room_id=input("Your room number to post in: ")
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager",
                             {"chat": chat, "user_id": user_id, "room_id": room_id})
        print(response.json())

class get_all_messages_rooms:
    index=3
    navn="Get all messages in all the room ur in"
    def method(self):
        room_id=input("Room id: ")
        user_id=input("User id: ")
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/"+room_id+"/"+user_id+"/messages")
        print(response.json())

class get_all_messages_room:
    index=4
    navn="Get all messages in a single room"
    def method(self):
        room_id=input("The room id: ")
        user_id=input("The user id: ")
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/"+room_id+"/"+user_id+"/messager")
        print(response.json())


if __name__ == '__main__':
    #start()

    an_array=[]

    a = post_user()
    b= post_room()
    c=post_message()
    d=get_all_messages_rooms()
    e=get_all_messages_room()


    an_array.append(a)
    an_array.append(b)
    an_array.append(c)
    an_array.append(d)
    an_array.append(e)

    while True:

        for x in an_array:
            print("Index: "+str(x.index)+", "+x.navn)


        inputten = input("Hva vil du gjøre, skriv tall i forhold til index: ")
        int_inputten=int(inputten)

        an_array[int_inputten].method()

        print("---")