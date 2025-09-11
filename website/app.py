from flask import Flask, Blueprint
from routes.home import home
from routes.youtube_dl import youtube_downloader
from modules.secrets import client


# App configuration
app = Flask(
    import_name=__name__,
    template_folder="templates"
)


# Blueprints
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(youtube_downloader, url_prefix="/yt-dl")


# Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
