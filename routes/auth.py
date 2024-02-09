from flask import app, redirect
from modules import authentication
import os

def init(app: app.Flask):
    authService = authentication.Authenticator()

    @app.route("/auth")
    def auth():
        return redirect(authService.signInWithGoogle(os.getenv("SIGN_IN_REDIRECT_TO")).url)