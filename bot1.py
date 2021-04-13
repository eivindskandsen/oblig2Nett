import requests

user_id = 1
def post_user(name):
    response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": name})
    user_id = response.json()
    print("your user ID is {}.".format(user_id))


def post_room(room):
    response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/{}".format(room), {"room_id": "{}".format(room)})
    print(response.json())


def post_message(chat, user_id, room_id):
    response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/{}/{}/messager".format(room_id, user_id), {"chat": chat,"user_id":user_id, "room_id":room_id})

def get_all_messages(room_id, user_id):
    response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/" + room_id + "/" + user_id + "/messages")
    print(response.json())


#def get_all_messages_room(room_id, user_id):


if __name__ == '__main__':

    post_user("Ulf")
    post_room(4)
    post_message("Hei, alle sammen", user_id, 4)
    get_all_messages(4,user_id)