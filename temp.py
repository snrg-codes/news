from db import news_list
from pprint import pprint

def get_news(news_title):
    t_list = []
    for news in news_list:
        t_list.append(news['title'])
    id_news = t_list.index(news_title)
    return news_list[id_news]

a = get_news("Third news")
print(a)


