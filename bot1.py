import requests

user_id = int
def post_user(name):
    response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": name})
    user_id = response.json()
    print("your user ID is {}.".format(user_id))


def post_room(room):
    response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/{}".format(room), {"room_id": "{}".format(room)})
    print(response.json())


#def post_message(chat, user_id, room_id):


#def get_all_messages(room_id, user_id):


#def get_all_messages_room(room_id, user_id):


if __name__ == '__main__':
    post_user(input("Write your name"))
    post_room(input("Which room do you want to create? (Number)"))