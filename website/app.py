from flask import Flask, Blueprint
from routes.home import home
from routes.youtube_dl import youtube_downloader
from werkzeug.middleware.proxy_fix import ProxyFix


# App configuration
app = Flask(
    import_name=__name__,
    template_folder="templates"
)


# Tell Flask it is behind a Proxy
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# Blueprints
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(youtube_downloader, url_prefix="/yt-dl")
