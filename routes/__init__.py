import flask.app
from routes import index, user
def initRoutes(app : flask.app.Flask):
    index.init(app)
    user.init(app)