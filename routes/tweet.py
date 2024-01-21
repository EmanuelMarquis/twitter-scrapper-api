import flask, json, os
from modules.scrapping import scrape_tweet_from

def init(app: flask.app.Flask):
        
    @app.route("/tweet/<username>/<tweetID>")
    def tweet(username, tweetID):
        return scrape_tweet_from(username, tweetID)