from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import flask_restful
app=Flask(__name__)
api=Api(app)

chat_rooms=[]
chat_room={}

chat_room_add = reqparse.RequestParser()
chat_room_add.add_argument("room_id", type=int, help="id is required..", required=True)
chat_room_add.add_argument("chat",type=[], help="chat array is required", required=True)
chat_room_add.add_argument("members",type=[],help="member array is required", required=True)





class Rooms(Resource):

    def get_all_rooms(self):
        return chat_rooms
    def get_one_room(self, chat_room_id):
        return chat_rooms[chat_room_id-1]

    def add_one_room(self):
        args = chat_room_add.parse_args()
        chat_room.append(args)

class Room(Resource):


    def get_all_room_users(self):
        return
    def add_user_room(self):
        return
class Messages(Resource):
    def get_all_messages(self):
        return

    def add_message_room(self):
        return
    def get_all_messages_room(self):
        return

api.add_resource(Rooms, "/api/rooms")



class chatrooms:
    conversation_list=[]






def abort_if_not_found(id, chatroom):
    if id not in chatroom:
        abort(404, message="Not found")

def abort_if_exists(id, chatroom):
    if id in chatroom:
        abort(404, message="Already exists")










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
