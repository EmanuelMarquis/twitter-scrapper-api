import flask.app
from routes import index, user, tweet
def initRoutes(app : flask.app.Flask):
    index.init(app)
    user.init(app)
    tweet.init(app)