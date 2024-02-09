import flask.app
from routes import index, user, tweet, auth, dashboard

routes = [index, user, tweet, auth, dashboard]

def initRoutes(app : flask.app.Flask):
    for route in routes:
        route.init(app)