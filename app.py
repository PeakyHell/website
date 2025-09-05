from flask import Flask, Blueprint
from routes.home import home
from routes.youtube_dl import youtube_downloader


# App configuration
app = Flask(__name__)


# Blueprints
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(youtube_downloader, url_prefix="/yt-dl")


# Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
