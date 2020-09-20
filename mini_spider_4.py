import requests
from bs4 import BeautifulSoup
import re

# 解析我们要抓详情页面的地址

base_url = 'https://huabot.com'

def crawl_links(page):
    rsp = requests.get('https://huabot.com/p/{}'.format(page))

    soup = BeautifulSoup(rsp.text, features="html.parser")

    # 通过审查元素，我们发现内容在 div class card 面
    cards = soup.find_all('div', {'class': 'card'})

    links = []
    for card in cards:
        card_title = card.find('span', {'class': 'card-title'})
        if card_title:
            card_link = card_title.find('a')
            link = card_link.get('href')
            links.append(base_url + link)

    return links


print(crawl_links(1))
print(crawl_links(2))
