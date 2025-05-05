from flask import Flask, render_template
from db import news_list
from functions import get_news

news = Flask(__name__)

@news.route("/")
def index():
    return render_template("18_04.html", news_list=news_list)

@news.route("/news_page/<news_title>")
def news_page(news_title):
    data  = get_news(news_list, news_title)
    return render_template("21_04.html", news=data)


news.run(debug=True)