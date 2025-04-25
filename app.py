from flask import Flask, render_template
from db import news_list


news = Flask(__name__)


@news.route("/")
def index():
    return render_template("18_04.html", news_list=news_list)

@news.route("/news_page")
def news_page():
    return render_template("21_04.html")


news.run(debug=True)