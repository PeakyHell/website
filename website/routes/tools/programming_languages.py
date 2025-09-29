from flask import Blueprint, render_template
import os

lang = Blueprint("Programming Languages", __name__)


# Routes
@lang.get("/")
def get_lang():
    documentation_markdown = ""

    return render_template("tools/programming_languages.html",
                           markdown = documentation_markdown)
