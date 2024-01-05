import flask, json, io
from twitter_scraper_selenium import get_profile_details
def init(app: flask.app.Flask):
    @app.route("/user/<string:username>")
    def user(username):
        filename = "get_profile_details"
        get_profile_details(
            twitter_username=username,
            filename=filename,
        )
        data = json.load(open(filename + ".json"))
        return data