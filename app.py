from flask import Flask, request
from TwitterAPI import TwitterAPI
import pymongo
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/")
if __name__ == "__main__":
    app.run()