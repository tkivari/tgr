from flask import Flask
from controllers.tags import tag_api
from controllers.twitter import twitter_api
app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

app.register_blueprint(tag_api, url_prefix='/tags')
app.register_blueprint(twitter_api, url_prefix='/twitter')

@app.route('/')
def index():
  return ''

if __name__ == "__main__":
  app.run()