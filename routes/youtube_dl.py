from dotenv import dotenv_values
from flask import Blueprint, render_template, request, send_file
from yt_dlp import YoutubeDL
from tempfile import TemporaryDirectory
import os


youtube_downloader = Blueprint("Youtube Downloader", __name__)


# Routes
@youtube_downloader.get("/")
def get_yt_dl():
    return render_template("yt-dl.html")


@youtube_downloader.post("/")
def post_yt_dl():
    with TemporaryDirectory() as tmp_dir:

        output_file = os.path.join(tmp_dir, "download.mp4")

        yt_options = {
            "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b", # Download the best mp4 video available, or the best video if no mp4 available
            "merge_output_format": "mp4",
            "outtmpl": output_file,
        }

        with YoutubeDL(yt_options) as yt_dl:
            yt_dl.download(request.form["link"])

        return send_file(output_file, as_attachment=True)
