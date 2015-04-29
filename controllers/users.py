from flask import Blueprint
from models.user import User
from flask import request, jsonify
from bson.json_util import loads, dumps
import time

users_api = Blueprint('users_api', __name__)

@users_api.route('', methods=['POST'])
def createUser():
  user = User({
          "username": request.args.get('username'),
          "email": request.args.get('email'),
          "password": request.args.get('password'),
          "created": time.time()
        })
  user.save

  response = { "success": True, "id": user.get_id }
  return dumps(response)
  
@users_api.route('/<user_id>', methods=['GET','PUT','DELETE'])
def getUser(user_id = None):
  if request.method == 'GET':
    try:
      _id = ObjectId(user_id)
    except:
      response = {"success": False, "message": "Couldn't create ObjectId with id: " + user_id}
      return dumps(response)
    user = col.users.find_one({"_id": _id})
    if user:
      return dumps(user)
    else:
      response = {
        "success": False,
        "message": "user " + user_id + " not found."
      }
      return dumps(response), 404