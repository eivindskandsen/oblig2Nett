import requests

responce=requests.post( "http://127.0.0.1:5000/" + "room/1", {"id_name"= 1, "chat"=[], "members"=[]})