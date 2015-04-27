from flask import Blueprint
from flask import request, jsonify
from bson.json_util import loads, dumps
from bson import ObjectId
import pymongo
import tweepy

conn=pymongo.MongoClient()
col = conn.tgr

twitter_api = Blueprint('twitter_api', __name__)

@twitter_api.route('/<tag>', methods=['GET'])
def twitterGetTagData(tag_id = None):
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