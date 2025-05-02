def get_news(news_list, news_title):
    t_list = []
    for news in news_list:
        t_list.append(news['title'])
    id_news = t_list.index(news_title)
    return news_list[id_news]