import os
from flask import Flask
from routes import initRoutes
from dotenv import load_dotenv
from waitress import serve

load_dotenv()

app = Flask(__name__)
initRoutes(app)

if __name__ == "__main__":
    if os.getenv("PY_ENV") == "Development":
        app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT")))
    else:
        serve(app, listen="*:"+os.getenv("PORT"))