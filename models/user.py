from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import loads, dumps
from bson import ObjectId
import pymongo

conn=pymongo.MongoClient()
col = conn.tgr

class User(object):
    
  def __init__(self, user=None):
    for key in user:
      setattr(self, key, user[key])

  def __repr__(self):
    return '<User %r>' % (self.username)

  def save(self):
    if not hasattr(self, "id"):
      try:
        self.id = str(col.users.insert(self.__dict__))
        
      except pymongo.errors.ConnectionFailure, e:
        return "Could not connect to MongoDB: %s" % e

  def set_password(self, password):
    self.pw_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pw_hash, password)