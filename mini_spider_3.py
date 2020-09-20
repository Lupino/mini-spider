import requests
from bs4 import BeautifulSoup
import re

# 解析我们要抓详情页面的地址

base_url = 'https://huabot.com'

rsp = requests.get('https://huabot.com/p/1')

soup = BeautifulSoup(rsp.text, features="html.parser")

# 通过审查元素，我们发现内容在 div class card 面
cards = soup.find_all('div', {'class': 'card'})

# 通过简要分析我们注意到包含内容的 card 有 data-title 这个属性
links = []
for card in cards:
    card_title = card.find('span', {'class': 'card-title'})
    if card_title:
        card_link = card_title.find('a')
        link = card_link.get('href')
        links.append(base_url + link)

print(links)
