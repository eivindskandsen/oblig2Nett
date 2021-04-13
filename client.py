import requests
import socket

user=str(666)


def socket():

    return

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

    response=requests.delete('http://127.0.0.1:5000/' +"/api/user/1")
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/user/1")
    print(response.json())

##ok

## Room-users


    response=requests.post('http://127.0.0.1:5000/' +"/api/rooms/0/users", {"room_id": 0, "user": 0})
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' +"/api/rooms/0/users")
    print(response.json())

## ok

### Messages
    global user
    response=requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/"+user+"/messager", {"chat": "halo", "user_id":0, "room_id": 0})
    print(response.json())

    response=requests.post('http://127.0.0.1:5000/' + "/api/rooms/1/"+user+"/messager", {"chat": "halo", "user_id":0, "room_id": 1})
    print(response.json())

# Messager Finds all messsages in all rooms user are in
    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/"+user+"/messager")
    print(response.json())

#


    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/0/0/messages")
    print(response.json())

    response=requests.get('http://127.0.0.1:5000/' + "/api/rooms/1/0/messages")
    print(response.json())

## ok
    response = requests.get('http://127.0.0.1:5000/' + "/api/uses/Eple")

class post_user:
    index=0
    navn="Make user"
    def method(self):
        name=input("Write Name: ")
        response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": name})
        global user
        user=response.json()
        print(user)
        print(response.json())

class post_room:
    index=1
    navn="Make room"
    def method(self):
        room=input("Write room number: ")
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/"+room, {"room_id": room})
        print(response.json())

class post_message:
    index=2
    navn="Post Message in room"
    def method(self):
        chat=input("Whats the message: ")
        #user_id=input("Your user id: ")
        room_id=input("Your room number to post in: ")
        global user
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/"+str(user)+"/messager",
                             {"chat": chat, "user_id": user, "room_id": room_id})
        print(response.json())

class get_all_messages_room:
    index=3
    navn="Get all messages in a single room"
    def method(self):
        room_id=input("Room id: ")
        global user
        #user_id=input("User id: ")
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/{}/{}/messages".format(room_id, user))
        print(response.json())

class get_all_messages_rooms:
    index=4
    navn="Get all messages in all the rooms ur in"
    def method(self):
        room_id=input("The room id of one room ur in: ")
        #user_id=input("The user id: ")
        global user
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/{}/{}/messager".format(room_id, user))
        print(response.json())


class post_user_room:
    index=5
    navn="User joins a room"
    def method(self):
        room_id=input("The room id: ")
        #user_id=input("The user id: ")
        global user
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/" + room_id + "/users", {"room_id": int(room_id), "user": user} )
        print(response.json())


class get_all_users_room:
    index=6
    navn="Get all users in room"
    def method(self):
        room_id=input("The room id: ")
        response = requests.get('http://127.0.0.1:5000/'  + "/api/rooms/"+room_id+"/users")
        print(response.json())


class get_room:
    index=7
    navn="Get one room"
    def method(self):
        room_id=input("The room id: ")
        response = requests.get('http://127.0.0.1:5000/'  +"/api/room/"+room_id)
        print(response.json())


class get_rooms:
    index=8
    navn="Get all rooms"
    def method(self):
        response = requests.get('http://127.0.0.1:5000/' +"/api/rooms/0")
        print(response.json())

class delete_user:
    index=9
    navn="Delete user"
    def method(self):
        user_id=input("User id: ")
        response = requests.delete('http://127.0.0.1:5000/' + "/api/user/"+user_id)
        print(response.json())

class get_users:
    index=10
    navn="Get all users"
    def method(self):
        response = requests.get('http://127.0.0.1:5000/' + "/api/users")
        print(response.json())

class get_user:
    index=11
    navn="Get your userID"
    def method(self):
        print(user)


if __name__ == '__main__':
    start()

    print("---")
    #inputten ="Hei"
    an_array=[]

    a = post_user()
    b= post_room()
    c=post_message()
    d=get_all_messages_room()
    e=get_all_messages_rooms()
    f=post_user_room()
    g=get_all_users_room()
    h=get_room()
    i=get_rooms()
    j=delete_user()
    k=get_users()
    l=get_user()


    an_array.append(a)
    an_array.append(b)
    an_array.append(c)
    an_array.append(d)
    an_array.append(e)
    an_array.append(f)
    an_array.append(g)
    an_array.append(h)
    an_array.append(i)
    an_array.append(j)
    an_array.append(k)
    an_array.append(l)

    while True:

        for x in an_array:
            print("Index: "+str(x.index)+", "+x.navn)


        inputten = input("What do u want to do, write a number from indexes: ")
        if inputten=="Exit":
            break

        int_inputten=int(inputten)



        an_array[int_inputten].method()

        print("---")