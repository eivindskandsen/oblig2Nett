import requests

user = -1
rooms = []

class post_user:
    index = 0
    navn = "Make user"

    def method(self, name):
        response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": name})
        global user
        user = response.json()
        print(response.json())


class post_room:
    index = 1
    navn = "Make room"

    def method(self, room):
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/{}".format(room), {"room_id": room})
        print(response.json())
        rooms.append(response.json())


class post_message:
    index = 2
    navn = "Post Message in room"

    def method(self,chat,room_id):
        user_id = user
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager",
                                 {"chat": chat, "user_id": user_id, "room_id": room_id})
        print(response.json())


class get_all_messages_room:
    index = 3
    navn = "Get all messages in a single room"

    def method(self, room_id):
        user_id = user
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/{}/{}/messages".format(room_id, user_id))
        print(response.json())


class get_all_messages_rooms:
    index = 4
    navn = "Get all messages in all the rooms ur in"

    def method(self):
        room_id = input("The room id: ")
        user_id = user
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/" + room_id + "/{}/messager".format(user_id))
        print(response.json())


class post_user_room:
    index = 5
    navn = "User joins a room"

    def method(self, room_id):
        #room_id = input("The room id: ")
        user_id = user
        response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/" + room_id + "/users",
                                 {"room_id": room_id, "user": user_id})
        print(response.json())


class get_all_users_room:
    index = 6
    navn = "Get all users in room"

    def method(self):
        room_id = input("The room id: ")
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/" + room_id + "/users")
        print(response.json())


class get_room:
    index = 7
    navn = "Get one room"

    def method(self):
        room_id = input("The room id: ")
        response = requests.get('http://127.0.0.1:5000/' + "/api/room/" + room_id)
        print(response.json())


class get_rooms:
    index = 8
    navn = "Get all rooms"

    def method(self):
        response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/0")
        print(response.json())


class delete_user:
    index = 9
    navn = "Delete user"

    def method(self):
        user_id = user
        response = requests.delete('http://127.0.0.1:5000/' + "/api/user/{}".format(user_id))
        print(response.json())


class get_users:
    index = 10
    navn = "Get all users"

    def method(self):
        response = requests.get('http://127.0.0.1:5000/' + "/api/users")
        print(response.json())


class get_user:
    index = 11
    navn = "Get your userID"

    def method(self):
        print(user)


if __name__ == '__main__':
    an_array = []

    a = post_user()
    b = post_room()
    c = post_message()
    d = get_all_messages_room()
    e = get_all_messages_rooms()
    f = post_user_room()
    g = get_all_users_room()
    h = get_room()
    i = get_rooms()
    j = delete_user()
    k = get_users()
    l = get_user()

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

    an_array[0].method("Elise")
    an_array[5].method("0")
    #an_array[1].method(0)
    an_array[1].method("2")

    #an_array[5].method("0")
    an_array[5].method("1")

    an_array[2].method("Hello, I'm Elise", 0)
    an_array[2].method("I just write stuff because I can", 0)
    an_array[2].method("And no one can stop me", 0)
    an_array[2].method("MOHAHAHAHAHAHA", 0)

    an_array[2].method("Hello, I'm Elise", 1)
    an_array[2].method("I just write stuff because I can in room 1", 1)
    an_array[2].method("And no one can stop me lol", 1)
    an_array[2].method("MOHAHAHAHAHAHA", 1)

    an_array[3].method(0)
    an_array[3].method(1)