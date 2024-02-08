import os
from supabase import create_client

class Authenticator:
    def __init__(self):
        self._client = create_client(
            os.getenv("PROJECT_URL"),
            os.getenv("PROJECT_KEY"),
        )

    def signInWithGoogle(self):
        return self._client.auth.sign_in_with_oauth({
            "provider": "google",
            "options": {
                "redirect_to": os.getenv("SIGN_IN_REDIRECT_TO")
            }
        })

    def signOut(self):
        self._client.auth.sign_out()