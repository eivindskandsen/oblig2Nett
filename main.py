from flask import Flask
from flask_restful import Api, Recource, reqparse, abort
import flask_restful
app=Flask(__name__)
api=Api(app)

chat_rooms=[]



class actions(Recource):

    def get_all_rooms(self, ):
    def get_one_room(self):
    def add_one_room(self,):


    def get_all_room_users(self):
    def add_user_room(self):


    def get_all_messages(self):


    def add_message_room(self):
    def get_all_messages_room(self):




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
