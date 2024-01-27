import requests
from bs4 import BeautifulSoup
from pprint import pprint
import schedule
import time


def get_top5_hackernews_article() -> list[dict]:


    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.select('.titleline > a')
    scores = soup.select('.score')

    data = []
    for link, score in zip(links, scores):

        article_name = link.text
        article_url = link.attrs['href']
        article_score = score.text

        data.append({
            'url':article_url,
            'name':article_name,
            'score':int(article_score.split()[0])
        })


    top_5 =  sorted(data, key= lambda x: x['score'], reverse=True)[:5]

    pprint(top_5)

    return top_5


schedule.every(5).seconds.do(get_top5_hackernews_article)

while True:
    schedule.run_pending()
    time.sleep(1)


