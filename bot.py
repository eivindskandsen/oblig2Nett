import requests

#def start():

def post_user(name):
    response = requests.post('http://127.0.0.1:5000/' + "/api/users", {"name": name})
    print(response.json())
    #print(response.json())

def post_room(room):
    response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0", {"room_id": room})
    print(response.json())


def post_message(chat, user_id, room_id):
    response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager",
                             {"chat": chat, "user_id": user_id, "room_id": room_id})
    print(response.json())

    #response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/1/0/messager",
      #                       {"chat": "første melding rom 1", "user_id": 0, "room_id": 1})
    #print(response.json())

    #response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/0/0/messager",
     #                        {"chat": "andre melding rom 0", "user_id": 0, "room_id": 0})
    #print(response.json())

    #response = requests.post('http://127.0.0.1:5000/' + "/api/rooms/1/0/messager",
     #                        {"chat": "andre melding rom 1", "user_id": 0, "room_id": 1})
    #print(response.json())

def get_all_messages_rooms(room_id, user_id):
    response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/"+room_id+"/"+user_id+"/messages")
    print(response.json())

def get_all_messages_room(room_id, user_id):
    response = requests.get('http://127.0.0.1:5000/' + "/api/rooms/"+room_id+"/"+user_id+"/messager")
    print(response.json())


if __name__ == '__main__':

    post_user("Eivind")

    an_array=[]


