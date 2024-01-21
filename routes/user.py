import flask, json, os
from modules.scrapping import scrape_profile

def init(app: flask.app.Flask, ):
        
    @app.route("/user/<string:username>")
    def user(username):
        return scrape_profile(username)