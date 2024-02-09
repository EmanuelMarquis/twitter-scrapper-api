import flask.app

def init(app: flask.app.Flask):
    @app.route("/dashboard")
    def dashboard():
        return "Dashboard!"