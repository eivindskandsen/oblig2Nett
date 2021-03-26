from flask import Flask
from flask_restful import Api, Recource, reqparse, abort
import flask_restful
app = Flask(__name__)
api = Api(app)

chat_rooms = []
#parser = reqparse.RequestParser()
#parser.add_argument("et eller annet", type=int/str, help="er eller annet required...", required=True)


class actions(Recource):

    def get_all_rooms(self, ):
        return

    def get_one_room(self, id):
        abort_if_not_found(id)
        return chat_rooms[id]

    def add_one_room(self, id):
        abort_if_exists(id)
        #args = "parser".parse_args()
        #chat_rooms[id] = args
        return


    def get_all_room_users(self):
        return

    def add_user_room(self):
        return



    def get_all_messages(self):
        return



    def add_message_room(self):
        return

    def get_all_messages_room(self):
        return




class chatrooms:
    conversation_list=[]






def abort_if_not_found(id):
    if id not in chat_rooms:
        abort(404, message="Not found")

def abort_if_exists(id):
    if id in chat_rooms:
        abort(404, message="Already exists")










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
