from flask import Blueprint
from flask import request, jsonify
from bson.json_util import loads, dumps
from bson import ObjectId
import pymongo
import time


conn=pymongo.MongoClient()
col = conn.tgr

tag_api = Blueprint('tag_api', __name__)

@tag_api.route('/', methods=['POST'])
def createTag():
  try:
    tag = {
            "user_id": request.args.get('user_id'),
            "tag": request.args.get('tag'),
            "created": time.time()
          }
    tag_id = col.tags.insert(tag)
    response = {"success": True, "id": str(tag_id)}
    return jsonify(response)
  except pymongo.errors.ConnectionFailure, e:
    return "Could not connect to MongoDB: %s" % e

@tag_api.route('/<tag_id>', methods=['GET','PUT','DELETE'])
def actOnTag(tag_id = None):
  if request.method == 'GET':
    try:
      _id = ObjectId(tag_id)
    except:
      response = {"success": False, "message": "Couldn't find tag with id: " + tag_id}
      return jsonify(response)
    tag = col.tags.find_one({"_id": _id})
    if tag:
      return dumps(tag)
    else:
      response = {
        "success": False,
        "message": "tag " + tag_id + " not found."
      }
      return jsonify(response), 404