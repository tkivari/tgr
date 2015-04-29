from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import loads, dumps
from bson import ObjectId
import pymongo

conn=pymongo.MongoClient()
col = conn.tgr

class User:
    
  def __init__(self, user=None):
    self.username = user["username"]
    self.email = user["email"]
    self.password = user["password"]

  def __repr__(self):
    return '<User %r>' % (self.username)

  def save():
    if not self.id:
      try:
        user_id = col.users.insert(user)
        self.id = str(user_id)
        return self.id
      except pymongo.errors.ConnectionFailure, e:
        return "Could not connect to MongoDB: %s" % e

  def get_id():
    return self.id

  def set_password(self, password):
    self.pw_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pw_hash, password)

  #def get_user_by_id(self, id):