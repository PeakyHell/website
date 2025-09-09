from flask import Blueprint, render_template, request, send_file, redirect, url_for, make_response
from yt_dlp import YoutubeDL
from tempfile import TemporaryDirectory
import os


youtube_downloader = Blueprint("Youtube Downloader", __name__)


# Routes
@youtube_downloader.get("/")
def get_yt_dl():
    error = request.cookies.get("yt-dl-error")
    return render_template("yt-dl.html", error=error)


@youtube_downloader.post("/")
def post_yt_dl():
    with TemporaryDirectory() as tmp_dir:

        output_file = os.path.join(tmp_dir, "download.mp4")

        yt_options = {
            # TODO : Implement cookies for authentication
            "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b", # Download the best mp4 video available, or the best video if no mp4 available
            "merge_output_format": "mp4",
            "outtmpl": output_file
        }

        with YoutubeDL(yt_options) as yt_dl:
            try:
                yt_dl.download(request.form["link"])
            except:
                res = make_response(redirect(url_for("Youtube Downloader.get_yt_dl")))
                res.set_cookie("yt-dl-error", "Could not download this video. Make sure the link is correct or retry later.")
                return res

        res = make_response(send_file(output_file, as_attachment=True))
        res.set_cookie("yt-dl-error", "")
        return res
