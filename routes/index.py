import flask.app

def init(app: flask.app.Flask):
    @app.route("/")
    def index():
        return "Hello World!"
