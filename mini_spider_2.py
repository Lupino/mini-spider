import requests
from bs4 import BeautifulSoup
import re


def crawl_entry(url):
    # 解析我们要抓页面的内容
    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text, features="html.parser")

    # 通过审查元素，我们发现内容在 div class card 面
    cards = soup.find_all('div', {'class': 'card'})

    # 通过简要分析我们注意到包含内容的 card 有 data-title 这个属性
    got_card = None
    for card in cards:
        if card.get('data-title'):
            got_card = card

    title = got_card.get('data-title').strip()
    summary = got_card.get('data-summary').strip()

    # 正文内容在 card-content 里面

    card_content = got_card.find('div', {'class': 'card-content'})

    # 清空 card-title
    card_title = card_content.find('span', {'class': 'card-title'})
    card_title.extract()

    # 清空分享按钮
    bd_share = card_content.find('div', {'class': 'bdsharebuttonbox'})
    bd_share.extract()

    # 清空图片属性
    imgs = card_content.find_all('img')
    for img in imgs:
        if not img.get('src'):
            img.extract()
        img.attrs.pop('alt', None)
        img.attrs.pop('title', None)

    # 渲染出内容
    content = str(card_content.renderContents(), 'utf8')

    # 清空无用的img 标签
    content = content.replace('</img>', '')
    content = re.sub('[\n\r]+', '\n', content)

    if content.startswith('<br/>'):
        content = content[5:]
    content = content.strip()

    return {
        'title': title,
        'summary': summary,
        'content': content,
        'url': url
    }

print(crawl_entry('https://huabot.com/t/46899.html'))
print(crawl_entry('https://huabot.com/t/40072.html'))
