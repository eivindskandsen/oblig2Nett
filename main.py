from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from tkinter import *

app = Flask(__name__)
api = Api(app)

chat_rooms = []
chat_room = {}
chat_room_users_array = []
chat = []
users = {}

chat_room_add = reqparse.RequestParser()
chat_room_add.add_argument("room_id", type=int, help="id is required..", required=True)

chat_room_users = reqparse.RequestParser()
chat_room_users.add_argument("room_id", type=int, help="room_id is required..", required=True)
chat_room_users.add_argument("user", type=int, help="user_id is required", required=True)

user_post = reqparse.RequestParser()
user_post.add_argument("name", type=str, help="Name is required!", required=True)

messages_add = reqparse.RequestParser()
messages_add.add_argument("chat", type=str, help="chat is required..", required=True)
messages_add.add_argument("user_id", type=int, help="user_id is required..", required=True)
messages_add.add_argument("room_id", type=int, help="room is required..", required=True)


class Rooms(Resource):

    def get(self, a_room):

        return chat_rooms

    # def get_one_room(self, chat_room_id):
    #   return chat_rooms[chat_room_id - 1]

    def post(self, a_room):
        args = chat_room_add.parse_args()

        if a_room != args.get("room_id"):
            return "Not excecuted"
        abort_if_exists(args, chat_rooms)

        chat_rooms.append(args)

        return chat_rooms[a_room], 201


class Room(Resource):

    def get(self, a_room):
        print(chat_rooms)
        return chat_rooms[a_room]


class Messages(Resource):

    def get(self, a_room, user_id):
        printer = []
        for x in chat:
            if x.get("room_id") == a_room:
                printer.append(x)

        for y in printer:
            if y.get("user_id") == user_id:
                return printer

        return "Not found in room"


class Messager(Resource):

    # Getting all messages from every room ur in

    def get(self, a_room, user_id):
        abort_if_not_found(user_id, users)
        abort_if_not_found(chat_rooms[a_room], chat_rooms)
        boolean=False
        print_array = []

        for x in chat:
            if x.get("user_id") == user_id:
                roomnumber = x.get("room_id")
                for y in chat:
                    if y.get("room_id") == roomnumber:
                        if y not in print_array:
                            print_array.append(y)

        # print(print_array)
        return print_array

    def post(self, a_room, user_id):

        args = messages_add.parse_args()
        chat.append(args)
        # print(chat)
        return args


class RoomUser(Resource):
    def get(self, a_room):
        return chat_room_users_array

    def post(self, a_room):
        args = chat_room_users.parse_args()
        # chat_room[a_room]=args
        abort_if_exists(args, chat_room_users_array)

        chat_room_users_array.append(args)

        return args  # chat_room_users_array[len(chat_room_users_array) - 1]


class Users(Resource):
    def get(self):
        printer = []
        for user in users:
            printer.append(users[user])
        return printer

    def post(self):
        user_id = len(users)
        if user_id in users:
            user_id += 1
        args = user_post.parse_args()
        users[user_id] = args
        return user_id, 201


class User(Resource):

    def get(self, user_id):
        abort_if_not_found(user_id, users)
        return users[user_id]

    def delete(self, user_id):
        abort_if_not_found(user_id, users)
        del users[user_id]
        return "User deleted", 202


def abort_if_not_found(iden, para):
    if iden not in para:
        abort(404, message="Not found")


def abort_if_exists(iden, para):
    if iden in para:
        abort(403, message="Already exists")


api.add_resource(Rooms, "/api/rooms/<int:a_room>")
api.add_resource(Room, "/api/room/<int:a_room>")
api.add_resource(User, "/api/user/<int:user_id>")
api.add_resource(Users, "/api/users")
api.add_resource(Messages, "/api/rooms/<int:a_room>/<int:user_id>/messages")
api.add_resource(Messager, "/api/rooms/<int:a_room>/<int:user_id>/messager")
api.add_resource(RoomUser, "/api/rooms/<int:a_room>/users")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
